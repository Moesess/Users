# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.


class User(models.Model):
    name_singular = "Użytkownik"
    name_accusative = "Użytkownika"
    name_plural = "Użytkownicy"
    login = models.CharField(max_length=30, unique=True, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    group = models.ForeignKey(
        'Group',
        default='1',
        related_name="group",
        on_delete=models.CASCADE,
    )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('first_name', 'last_name', 'password')


class Group(models.Model):
    name_singular = "Grupa"
    name_accusative = "Grupę"
    name_plural = "Grupy"
    permissions = [('user', '1'), ('moderator', '2'), ('admin', '3')]
    name = models.CharField(max_length=30)
    permission_level = models.CharField(max_length=30, choices=permissions, default=1)

    def __str__(self):
        return self.name
