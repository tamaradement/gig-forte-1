from django.urls import path
from .views import (
    CallListView,
    SearchView,
    AddMusicianView
)

urlpatterns = [
    path("", CallListView.as_view(), name="call_list"),
    path("search/", SearchView.as_view(), name="search_musicians"),
    path("<int:pk>/add", AddMusicianView, name='add_musician'),

]