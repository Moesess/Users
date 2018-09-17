# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


class HomeView(TemplateView):
    template_name = "homepage.html"
