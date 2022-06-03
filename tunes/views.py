from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Tune, Setlist


class TuneListView(ListView):
    model = Tune
    template_name = "tune_list.html"


class TuneDetailView(DetailView):
    model = Tune
    template_name = "tune_detail.html"


class TuneUpdateView(UpdateView):
    model = Tune
    fields = (
        "title",
        "composer",
        "key",
        "notes",
        "genre",
        "pdf",
    )
    template_name = "tune_edit.html"


class TuneDeleteView(DeleteView):
    model = Tune
    template_name = "tune_delete.html"
    success_url = reverse_lazy("tune_list")


class TuneCreateView(CreateView):
    model = Tune
    template_name = "tune_new.html"
    fields = (
        "title",
        "composer",
        "key",
        "notes",
        "genre",
        "pdf",
        "performer",
    )


# ==========
# Setlists
# ==========


class SetlistCollection(ListView):
    model = Setlist
    template_name = "setlist_collection.html"


class SetlistDetailView(DetailView):
    model = Setlist
    template_name = "setlist_detail.html"
