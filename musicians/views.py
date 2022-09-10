from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import CustomUser
from .filters import MusicianFilter
from .models import CallList

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
    call_list = CallList.objects.get(bandleader=request.user)
    call_list.add_musician(musician_to_add)
    return HttpResponseRedirect(reverse('call_list'))

        
        