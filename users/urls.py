from django.urls import path, include
from .views import (ItemCreateView, ItemListView, 
ItemDetailView, ItemDestroyView, ItemsFeaturedView, ListMemberView, CreateMemberView, MyItemListView)


urlpatterns = [
    path("api/", ItemListView.as_view()),
    path("api/create/", ItemCreateView.as_view()),
    path("api/<int:id>/", ItemDetailView.as_view()),
    path("api/delete/<int:id>/", ItemDestroyView.as_view()),
    path("api/featured/", ItemsFeaturedView.as_view()),
    path("api/list/", MyItemListView.as_view()),
    path("api/create_member/", CreateMemberView.as_view()),
    path("api/list_members/", ListMemberView.as_view()),
]