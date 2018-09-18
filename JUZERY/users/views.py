# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render

# Create your views here.


class HomeView(TemplateView):
    """
    Widok odpowiadający za wyświetlanie strony głównej
    """
    template_name = "homepage.html"


class UserAdd(TemplateView):
    """
    Widok odpowiadający za wyświetlanie strony dodawania użytkownika
    """
    template_name = "user_add.html"
