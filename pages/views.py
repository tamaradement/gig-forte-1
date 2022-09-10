from unittest.mock import _CallList
from django.views.generic import TemplateView
from musicians.models import CallList
from accounts.models import CustomUser
from django.shortcuts import render, get_object_or_404


class HomePageView(TemplateView):
    template_name = "home.html"








