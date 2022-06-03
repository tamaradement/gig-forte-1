from django.urls import path
from .views import (
    TuneListView,
    TuneDetailView,
    TuneUpdateView,
    TuneDeleteView,
    TuneCreateView,
    SetlistCollection,
    SetlistDetailView,
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
    path("setlists", SetlistCollection.as_view(), name="setlist_collection"),
]
