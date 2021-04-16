from djoser.serializers import UserCreateSerializer
from .models import User, Items, Member
from rest_framework import serializers


class UserCreateSerializer(UserCreateSerializer): # The djoser user serializer
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = "__all__"
        # fields = ("id", "email", "firstname", "lastname", "profile_pic", "state")


class ItemSerializer(serializers.ModelSerializer): # The Item serializer
    class Meta:
        model = Items
        fields = "__all__"
        lookup_field = "id"


class MemberSerializer(serializers.ModelSerializer): # The member serializer
    class Meta:
        model = Member
        fields = "__all__"
        lookup_field = "id"