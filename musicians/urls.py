from django.urls import path
from .views import (
    CallListView,
    SearchView,
    AddMusicianView,
    RemoveMusicianView,
    InviteMusicianView
)

urlpatterns = [
    path("", CallListView.as_view(), name="call_list"),
    path("invite", InviteMusicianView, name="invite_musician"),
    path("search/", SearchView.as_view(), name="search_musicians"),
    path("<int:pk>/add", AddMusicianView, name='add_musician'),
    path("<int:pk>/remove", RemoveMusicianView, name='remove_musician'),

]