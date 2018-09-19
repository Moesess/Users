# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, CreateView
from models import User, Group
# Create your views here.


class HomeView(TemplateView):
    """
    Widok odpowiadający za wyświetlanie strony głównej
    """
    template_name = "homepage.html"


class GroupAdd(CreateView):
    template_name = "user_add.html"
    model = Group
    fields = ['name', 'permission_level']
    success_url = 'home'


class UserAdd(CreateView):
    """
    Widok odpowiadający za wyświetlanie strony dodawania użytkownika
    """
    template_name = "user_add.html"
    model = User
    fields = ['first_name', 'last_name', 'group']
    success_url = 'home'
