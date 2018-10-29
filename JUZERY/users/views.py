# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from models import User, Group
from django.urls import reverse_lazy
from forms import UserForm
from django.views.generic.edit import FormView
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
    """
    Widok odpowiadający za wyświetlanie listy użytkowników
    """
    template_name = "user_list.html"
    model = User

    def get_context_data(self, *args, **kwargs):
        context = {'title': "Users List",
                   'user': User.objects.all(),
                   'group': Group.objects.all()}
        return context


class Details(DetailView):
    """
    Widok odpowiadający za wyświetlanie detali modelu
    """
    template_name = "details.html"
    model = User

    def get_context_data(self, **kwargs):
        context = {'title': User.first_name + " details",
                   'user': User.objects.all(),
                   'group': Group.objects.all()}
        return context


class UserDelete(DeleteView):
    """
    Widok odpowiadający za usuwanie Użytkownika
    """
    template_name = "confirm_delete.html"
    model = User
    success_url = reverse_lazy('home')


class GroupDelete(DeleteView):
    """
    Widok odpowiadający za usuwanie Grupy
    """
    template_name = "confirm_delete.html"
    model = Group
    success_url = reverse_lazy("home")


class GroupEdit(UpdateView):
    model = Group
    fields = ['name', 'permission_level']
    template_name = "edit_form.html"
    success_url = reverse_lazy("list_user")


class UserEdit(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'password', 'group']
    template_name = "edit_form.html"
    success_url = reverse_lazy("list_user")


class RegisterPanel(CreateView):
    model = User
    form_class = UserForm
    template_name = "register.html"
    success_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super(RegisterPanel, self).get_context_data(**kwargs)
        context.update({'title': "Register"})
        return context

    # def form_valid(self, form):
    #     form.save()
    #     return super(RegisterPanel, self).form_valid(form)
