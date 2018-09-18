# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
    )


class Group(models.Model):
    name = models.CharField(max_length=30)
    permission_level = models.IntegerField(max_length=1)
