from django.urls import path
from .views import (
    CallListView,
    SearchView,
    AddMusicianView,
    RemoveMusicianView,
    InviteMusicianView,
    ComputeMusicianExpensesByYear,
)

urlpatterns = [
    path("", CallListView.as_view(), name="call_list"),
    path("invite", InviteMusicianView, name="invite_musician"),
    path("compute_expenses", ComputeMusicianExpensesByYear, name="compute_expenses"),
    path("search/", SearchView.as_view(), name="search_musicians"),
    path("<int:pk>/add", AddMusicianView, name='add_musician'),
    path("<int:pk>/remove", RemoveMusicianView, name='remove_musician'),

]