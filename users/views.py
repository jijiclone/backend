from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView
from .models import Items, Member
from .serializers import ItemSerializer, MemberSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# This add another item to the the Items model
class ItemCreateView(CreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        # instantiate a user to an item
        serializer.save(user=self.request.user)


# This list the items in the Items model
class ItemListView(ListAPIView):
    queryset = Items.objects.order_by("-date_added")
    serializer_class = ItemSerializer
    lookup_field = "id"


# This retrieves an item from the Items model
class ItemDetailView(RetrieveAPIView):
    queryset = Items.objects.order_by("-date_added")
    serializer_class = ItemSerializer
    lookup_field = "id"


# This deletes an item from the Items model
class ItemDestroyView(DestroyAPIView):
    queryset = Items.objects.order_by("-date_added")
    serializer_class = ItemSerializer
    lookup_field = "id"


# This returns the featured item in the Items model
class ItemsFeaturedView(ListAPIView):
    queryset = Items.objects.all().filter(featured=True)
    serializer_class = ItemSerializer
    lookup_field = "id"


# This returns the items created by the request user
class MyItemListView(ListAPIView):
    def get_queryset(self):
        return Items.objects.filter(user=self.request.user).order_by("-date_added")
    serializer_class = ItemSerializer
    lookup_field = "id"


# This creates a member 
class CreateMemberView(APIView):
    def post(self, request):
        item = get_object_or_404(Items, id=request.data)
        created = Member.objects.create(user=request.user, item=item)

        if created:
            # Increase the number of intrests on an item
            item.interest += 1
            item.save()
            return Response("Member added", status=status.HTTP_201_CREATED)
        return Response("An error occurred", status=status.HTTP_400_BAD_REQUEST)


# Returns he list of members that showed interest in an item
class ListMemberView(APIView):
    # permission_classes = [~IsAuthenticated]
    def get(self, request):
        # gets the list of members that showed interest in an item
        item = get_object_or_404(Items, id=self.request.query_params["id"]).get_members
        my_list  = []
        for i in item:
            # appends the list of members to an empty list
            my_list.append(
                {
                    "email": i.user.email,
                    "first_name": i.user.first_name,
                    "last_name": i.user.last_name,
                    "state": i.user.state
                }
            )
        content = {"my_list": my_list}
        return Response(content["my_list"])
