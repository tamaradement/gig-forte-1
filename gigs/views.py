from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Gig, Venue
from .forms import GigCreateForm
from django.http import HttpResponseRedirect
import datetime

def AcceptGigView(request, pk):
    gig = get_object_or_404(Gig, id=request.POST.get('gig_id'))
    gig.acccepts.add(request.user)
    gig.personnel.remove(request.user)
    return HttpResponseRedirect(reverse('gig_detail', args=[str(pk)]))

def DeclineGigView(request, pk):
    gig = get_object_or_404(Gig, id=request.POST.get('gig_id'))
    gig.declines.add(request.user)
    gig.personnel.remove(request.user)
    if gig.acccepts.filter(id=request.user.id).exists():
        gig.acccepts.remove(request.user)
    return HttpResponseRedirect(reverse('gig_invitations'))


class GigListView(LoginRequiredMixin, ListView):
    model = Gig
    template_name = "gigs/gig_list.html"

    def get_queryset(self):
        user_is_personnel = Gig.objects.filter(acccepts=self.request.user).exclude  (event_date__lte=datetime.date.today()).distinct() 

        user_is_bandleader = Gig.objects.filter(bandleader=self.request.user).exclude(event_date__lte=datetime.date.today()).distinct() 

        combined_list = user_is_personnel.union(user_is_bandleader).order_by('event_date')

        return combined_list  

class GigInvitations(LoginRequiredMixin, ListView):
    model = Gig
    template_name = "gigs/gig_invitations.html"

    def get_queryset(self):
        user_is_personnel = Gig.objects.filter(personnel=self.request.user).exclude  (event_date__lte=datetime.date.today()).exclude(bandleader=self.request.user).distinct()

        return user_is_personnel.order_by('-created')
       
    
class GigHistory(LoginRequiredMixin, ListView):
    model = Gig
    template_name = "gigs/gig_history.html"


    def get_queryset(self):
        user_is_personnel = Gig.objects.filter(acccepts=self.request.user).exclude  (event_date__gte=datetime.date.today()).distinct() 

        user_is_bandleader = Gig.objects.filter(bandleader=self.request.user).exclude(event_date__gte=datetime.date.today()).distinct() 

        combined_list = user_is_personnel.union(user_is_bandleader).order_by('-event_date')
        
        return combined_list 


class GigDetailView(LoginRequiredMixin, DetailView):
    model = Gig
    template_name = "gigs/gig_detail.html"


class GigUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gig
    template_name = "gigs/gig_edit.html"
    form_class = GigCreateForm

    def test_func(self):
        obj = self.get_object()
        return obj.bandleader == self.request.user


class GigDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gig
    template_name = "gigs/gig_delete.html"
    success_url = reverse_lazy("gig_list")

    def test_func(self):
        obj = self.get_object()
        return obj.bandleader == self.request.user


class GigCreateView(LoginRequiredMixin, CreateView):
    model = Gig
    template_name = "gigs/gig_new.html"
    form_class = GigCreateForm

    def form_valid(self, form):
        form.instance.bandleader = self.request.user
        return super().form_valid(form)


# Venue views


class VenueList(LoginRequiredMixin, ListView):
    model = Venue
    template_name = "venues/venue_list.html"


class VenueDetailView(LoginRequiredMixin, DetailView):
    model = Venue
    template_name = "venues/venue_detail.html"


class VenueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Venue
    fields = (
        "name",
        "address_1",
        "address_2",
        "city",
        "state",
        "zip_code",
        "website",
    )
    template_name = "venues/venue_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.performer == self.request.user


class VenueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Venue
    template_name = "venues/venue_delete.html"
    success_url = reverse_lazy("venue_list")

    def test_func(self):
        obj = self.get_object()
        return obj.performer == self.request.user


class VenueCreateView(LoginRequiredMixin, CreateView):
    model = Venue
    fields = (
        "name",
        "address_1",
        "address_2",
        "city",
        "state",
        "zip_code",
        "website",
    )
    template_name = "venues/venue_new.html"

    def form_valid(self, form):
        form.instance.performer = self.request.user
        return super().form_valid(form)
