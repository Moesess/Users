# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    name_singular = "Użytkownik"
    name_accusative = "Użytkownika"
    name_plural = "Użytkownicy"
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    group = models.ForeignKey(
        'Group',
        related_name="group",
        on_delete=models.CASCADE,
    )


class Group(models.Model):
    name_singular = "Grupa"
    name_accusative = "Grupę"
    name_plural = "Grupy"
    permissions = [('user', '1'), ('moderator', '2'), ('admin', '3')]
    name = models.CharField(max_length=30)
    permission_level = models.CharField(max_length=30, choices=permissions, default=1)

    def __str__(self):
        return self.name
