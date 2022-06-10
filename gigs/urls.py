from django.urls import path
from .views import (
    GigListView,
    GigDetailView,
    GigUpdateView,
    GigDeleteView,
    GigCreateView,
)

urlpatterns = [
    path("<int:pk>/", GigDetailView.as_view(), name="gig_detail"),
    path("<int:pk>/edit/", GigUpdateView.as_view(), name="gig_edit"),
    path("<int:pk>/delete/", GigDeleteView.as_view(), name="gig_delete"),
    path("new/", GigCreateView.as_view(), name="gig_new"),
    path("", GigListView.as_view(), name="gig_list"),
]
