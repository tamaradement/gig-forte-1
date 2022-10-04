from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import CustomUser
from gigs.models import Gig
from .filters import MusicianFilter
from .models import CallList
from .emails import send_add_alert, invite_new_user
from .forms import NewMusicianForm, GigsByYear

class CallListView(LoginRequiredMixin, TemplateView):
    template_name = "musicians/call_list.html"

    def get(self, request):
        call_list = CallList.objects.get_or_create(bandleader=request.user)
        created = CallList.objects.get(bandleader=request.user)
        musicians = created.musicians.all()
        context = {'musicians': musicians}
        return render(request, self.template_name, context)

class SearchView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "musicians/search_musicians.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = MusicianFilter(self.request.GET, queryset=self.get_queryset())
        return context

def AddMusicianView(request, pk):
    musician_to_add = get_object_or_404(CustomUser, id=request.POST.get('user_id'))
    get_or_create_call_list = CallList.objects.get_or_create(bandleader=request.user)
    call_list = CallList.objects.get(bandleader=request.user)
    call_list.add_musician(musician_to_add)
    send_add_alert(request.user, musician_to_add)
    return HttpResponseRedirect(reverse('call_list'))

def RemoveMusicianView(request, pk):
    call_list = CallList.objects.get(bandleader=request.user)
    musicians = call_list.musicians.all()
    musician_to_remove = ''
    for musician in musicians:
        if musician.id == int(request.POST.get('musician_id')):
            musician_to_remove = CustomUser.objects.get(username=musician)
    call_list.terminate_relationship(musician_to_remove)  
    return HttpResponseRedirect(reverse('call_list'))


def InviteMusicianView(request):
    context = {}
    context['form'] = NewMusicianForm()
    if request.method == "POST":
        invite_new_user(request)
    return render(request, "musicians/invite_musician.html", context)

def ComputeMusicianExpensesByYear(request):
    context = {}
    context['form'] = GigsByYear()
    if request.method == "POST":
        year = request.POST['year']
        gigs = Gig.objects.filter(event_date__year=year).filter(bandleader=request.user)

        gross_income = 0
        total_payouts = 0

        for gig in gigs:
            # Compute payout for current gig.
            payout = len(gig.acccepts.all()) * gig.pay
            gross_income = gross_income + payout
            
            # If the bandleader was also personnel, adjust payout.
            if gig.bandleader in gig.acccepts.all():
                payout = payout - gig.pay
            
            total_payouts = total_payouts + payout

        context['gigs'] = gigs
        context['gross_income'] = gross_income
        context['total_payouts'] = total_payouts
        context['year'] = year

    return render(request, "musicians/compute_expenses.html", context)


        
        