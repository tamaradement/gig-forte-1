from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Gig
from .forms import GigCreateForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
import datetime


class GigListView(ListView):
    model = Gig
    template_name = "gigs/gig_list.html"

    def get_queryset(self):
        return Gig.objects.filter(event_date__gte=datetime.date.today())


class GigHistory(ListView):
    model = Gig
    template_name = "gigs/gig_history.html"

    def get_queryset(self):
        return Gig.objects.filter(event_date__lte=datetime.date.today())


class GigDetailView(DetailView):
    model = Gig
    template_name = "gigs/gig_detail.html"


class GigUpdateView(UpdateView):
    model = Gig
    fields = ("title", "event_date", "bandleader")
    template_name = "gigs/gig_edit.html"


class GigDeleteView(DeleteView):
    model = Gig
    template_name = "gigs/gig_delete.html"
    success_url = reverse_lazy("gig_list")


class GigCreateView(CreateView):
    model = Gig
    template_name = "gigs/gig_new.html"
    # fields = ("title", "event_date", "bandleader")
    form_class = GigCreateForm

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields["event_date"].widget = DateTimePickerInput()
    #     return form
