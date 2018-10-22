# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, CreateView, ListView
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
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(GroupAdd, self).get_context_data(**kwargs)
        context.update({'title': "Add Group"})
        return context


class UserAdd(CreateView):
    """
    Widok odpowiadający za dodawanie użytkowników
    """
    template_name = "add_form.html"
    model = User
    fields = ['first_name', 'last_name', 'password', 'group']
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(UserAdd, self).get_context_data(**kwargs)
        context.update({'title': "Add User"})
        return context


class UserList(ListView):
    template_name = "user_list.html"
    model = User
    model = Group

    def get_context_data(self, *args, **kwargs):
        context = {'title': "Users List",
                   'user': User.objects.all(),
                   'group': Group.objects.all()}
        return context


