from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Tune, Setlist
from .filters import TuneFilter
from .forms import SetlistForm
from django.conf import settings

# Tune views:


class TuneListView(LoginRequiredMixin, ListView):
    model = Tune
    template_name = "tunes/tune_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = TuneFilter(self.request.GET, queryset=self.get_queryset())
        context['AWS_STORAGE_BUCKET_NAME'] = settings.AWS_STORAGE_BUCKET_NAME
        return context


class TuneDetailView(LoginRequiredMixin, DetailView):
    model = Tune
    template_name = "tunes/tune_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TuneDetailView, self).get_context_data(**kwargs)
        context['AWS_STORAGE_BUCKET_NAME'] = settings.AWS_STORAGE_BUCKET_NAME
        print(context)

        return context


class TuneUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        obj = self.get_object()
        return obj.performer == self.request.user


class TuneDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tune
    template_name = "tunes/tune_delete.html"
    success_url = reverse_lazy("tune_list")

    def test_func(self):
        obj = self.get_object()
        return obj.performer == self.request.user


class TuneCreateView(LoginRequiredMixin, CreateView):
    model = Tune
    template_name = "tunes/tune_new.html"
    fields = (
        "title",
        "composer",
        "key",
        "notes",
        "genre",
        "pdf",
    )

    def form_valid(self, form):
        form.instance.performer = self.request.user
        return super().form_valid(form)


# Setlist views:


class SetlistCollection(LoginRequiredMixin, ListView):
    model = Setlist
    template_name = "setlists/setlist_collection.html"


class SetlistDetailView(LoginRequiredMixin, DetailView):
    model = Setlist
    template_name = "setlists/setlist_detail.html"


class SetlistUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Setlist
    template_name = "setlists/setlist_edit.html"
    form_class = SetlistForm

    def test_func(self):
        obj = self.get_object()
        return obj.performer == self.request.user

    def get_form_kwargs(self):
        kwargs = super(SetlistUpdateView, self).get_form_kwargs()
        kwargs["performer"] = self.request.user
        return kwargs


class SetlistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Setlist
    template_name = "setlists/setlist_delete.html"
    success_url = reverse_lazy("setlist_collection")

    def test_func(self):
        obj = self.get_object()
        return obj.performer == self.request.user


class SetlistCreateView(LoginRequiredMixin, CreateView):
    model = Setlist
    template_name = "setlists/setlist_new.html"
    form_class = SetlistForm

    def form_valid(self, SetlistForm):
        SetlistForm.instance.performer = self.request.user
        return super().form_valid(SetlistForm)

    def get_form_kwargs(self):
        kwargs = super(SetlistCreateView, self).get_form_kwargs()
        kwargs["performer"] = self.request.user
        return kwargs
