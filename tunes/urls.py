from django.urls import path
from .views import (
    TuneListView,
    TuneDetailView,
    TuneUpdateView,
    TuneDeleteView,
    TuneCreateView,
    SetlistCollection,
    SetlistDetailView,
    SetlistUpdateView,
    SetlistDeleteView,
    SetlistCreateView,
    TuneListApi,
    TuneDetailApi,
)

urlpatterns = [
    # Tunes
    path("<int:pk>/", TuneDetailView.as_view(), name="tune_detail"),
    path("<int:pk>/edit/", TuneUpdateView.as_view(), name="tune_edit"),
    path("<int:pk>/delete/", TuneDeleteView.as_view(), name="tune_delete"),
    path("new/", TuneCreateView.as_view(), name="tune_new"),
    path("", TuneListView.as_view(), name="tune_list"),
    # Setlists
    path("setlists/<int:pk>/", SetlistDetailView.as_view(), name="setlist_detail"),
    path("setlists/<int:pk>/edit/", SetlistUpdateView.as_view(), name="setlist_edit"),
    path(
        "setlists/<int:pk>/delete/", SetlistDeleteView.as_view(), name="setlist_delete"
    ),
    path("setlists", SetlistCollection.as_view(), name="setlist_collection"),
    path("setlists/new/", SetlistCreateView.as_view(), name="setlist_new"),
    # Api views
    path("tunes_api/", TuneListApi.as_view(), name="tunes_api"),
    path("tunes_api/<int:pk>/", TuneDetailApi.as_view(), name='tunes_api_detail'),
]
