from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Tune, Setlist
from .filters import TuneFilter
from .forms import SetlistForm

# Tune views:


class TuneListView(ListView):
    model = Tune
    template_name = "tunes/tune_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = TuneFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TuneDetailView(DetailView):
    model = Tune
    template_name = "tunes/tune_detail.html"


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
    template_name = "tunes/tune_edit.html"


class TuneDeleteView(DeleteView):
    model = Tune
    template_name = "tunes/tune_delete.html"
    success_url = reverse_lazy("tune_list")


class TuneCreateView(CreateView):
    model = Tune
    template_name = "tunes/tune_new.html"
    fields = (
        "title",
        "composer",
        "key",
        "notes",
        "genre",
        "pdf",
        "performer",
    )


# Setlist views:


class SetlistCollection(ListView):
    model = Setlist
    template_name = "setlists/setlist_collection.html"


class SetlistDetailView(DetailView):
    model = Setlist
    template_name = "setlists/setlist_detail.html"


class SetlistUpdateView(UpdateView):
    model = Setlist
    template_name = "setlists/setlist_edit.html"
    form_class = SetlistForm

    def get_form_kwargs(self):
        kwargs = super(SetlistUpdateView, self).get_form_kwargs()
        kwargs["performer"] = self.request.user
        return kwargs


class SetlistDeleteView(DeleteView):
    model = Setlist
    template_name = "setlists/setlist_delete.html"
    success_url = reverse_lazy("setlist_collection")


class SetlistCreateView(CreateView):
    model = Setlist
    template_name = "setlists/setlist_new.html"
    form_class = SetlistForm

    def get_form_kwargs(self):
        kwargs = super(SetlistCreateView, self).get_form_kwargs()
        kwargs["performer"] = self.request.user
        return kwargs
