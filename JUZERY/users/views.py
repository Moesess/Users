# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from models import User, Group
from django.urls import reverse_lazy
from forms import LoginForm, UserForm
from django.views.generic.edit import FormView
from errors import *
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
        context.update({'title': "Add Group",
                        'name_accusative': "Grupę"})
        return context


class UserAdd(CreateView):
    """
    Widok odpowiadający za dodawanie użytkowników
    """
    template_name = "add_form.html"
    model = User
    fields = ['login','first_name', 'last_name', 'password', 'group']
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(UserAdd, self).get_context_data(**kwargs)
        context.update({'title': "Add User",
                        'name_accusative': "Użytkownika"})
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
    """
    Widok odpowiadający za edytowanie grupy
    """
    model = Group
    fields = ['name', 'permission_level']
    template_name = "edit_form.html"
    success_url = reverse_lazy("list_user")


class UserEdit(UpdateView):
    """
    Widok odpowiadający za Edytowanie użytkownika
    """
    model = User
    fields = ['login', 'first_name', 'last_name', 'password', 'group']
    template_name = "edit_form.html"
    success_url = reverse_lazy("list_user")


class RegisterPanel(CreateView):
    """
    Widok odpowiadający za generowanie Formularza rejestracji i dodawania użytkownika
    """
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


class LoginPanel(FormView):
    """
    Widok odpowiadający za generowanie formularza Logowania i za samo logowanie
    """
    model = User
    form_class = LoginForm
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginPanel, self).get_context_data(**kwargs)
        context.update({'title': "Login"})
        return context

    def form_valid(self, form):
        print "gut"
        return super(LoginPanel, self).form_valid(form)

    def form_invalid(self, form):
        print "nicht gut"
        return super(LoginPanel, self).form_invalid(form)
