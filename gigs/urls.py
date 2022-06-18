from django.urls import path
from .views import (
    GigListView,
    GigDetailView,
    GigUpdateView,
    GigDeleteView,
    GigCreateView,
    GigHistory,
    VenueList,
    VenueDetailView,
    VenueUpdateView,
    VenueDeleteView,
    VenueCreateView,
)

urlpatterns = [
    # Gigs
    path("<int:pk>/", GigDetailView.as_view(), name="gig_detail"),
    path("<int:pk>/edit/", GigUpdateView.as_view(), name="gig_edit"),
    path("<int:pk>/delete/", GigDeleteView.as_view(), name="gig_delete"),
    path("new/", GigCreateView.as_view(), name="gig_new"),
    path("history", GigHistory.as_view(), name="gig_history"),
    path("", GigListView.as_view(), name="gig_list"),
    # Venues
    path("venues/<int:pk>/", VenueDetailView.as_view(), name="venue_detail"),
    path("venues/<int:pk>/delete", VenueUpdateView.as_view(), name="venue_edit"),
    path("venues/<int:pk>/edit", VenueDeleteView.as_view(), name="venue_delete"),
    path("venues/new/", VenueCreateView.as_view(), name="venue_new"),
    path("venues/", VenueList.as_view(), name="venue_list"),
]
