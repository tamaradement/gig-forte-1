from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Gig


class GigListView(ListView):
    model = Gig
    template_name = "gigs/gig_list.html"


class GigDetailView(DetailView):
    model = Gig
    template_name = "gigs/gig_detail.html"


class GigUpdateView(UpdateView):
    model = Gig
    fields = ("title", "bandleader")
    template_name = "gigs/gig_edit.html"


class GigDeleteView(DeleteView):
    model = Gig
    template_name = "gigs/gig_delete.html"
    success_url = reverse_lazy("gig_list")


class GigCreateView(CreateView):
    model = Gig
    template_name = "gigs/gig_new.html"
    fields = ("title", "bandleader")
