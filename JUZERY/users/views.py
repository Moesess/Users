# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, CreateView
from models import User, Group
from django.shortcuts import render_to_response
# Create your views here.


class HomeView(TemplateView):
    """
    Widok odpowiadający za wyświetlanie strony głównej
    """
    template_name = "homepage.html"
    title = "Home"


class GroupAdd(CreateView):
    """
    Widok odpowiadający za dodawanie grup
    """
    template_name = "add_form.html"
    model = Group
    fields = ['name', 'permission_level']
    success_url = 'home'


class UserAdd(CreateView):
    """
    Widok odpowiadający za dodawanie użytkowników
    """
    template_name = "add_form.html"
    model = User
    fields = ['first_name', 'last_name', 'password', 'group']
    success_url = 'home'
    title = "Add User"



