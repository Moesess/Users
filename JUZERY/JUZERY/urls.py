"""JUZERY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from users.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^user/add/$', UserAdd.as_view(), name='add_user'),
    url(r'^group/add/$', GroupAdd.as_view(), name='add_group'),
    url(r'^user/list/$', UserList.as_view(), name='list_user'),
    url(r'^register$', RegisterPanel.as_view(), name='register'),
    url(r'^login$', LoginPanel.as_view(), name='login'),
    url(r'^user/delete/(?P<name>[-\w]+)/(?P<pk>[0-9]+)/$', UserDelete.as_view(), name='delete_user'),
    url(r'^group/delete/(?P<name>[-\w]+)/(?P<pk>[0-9]+)/$', GroupDelete.as_view(), name='delete_group'),
    url(r'^user/edit/(?P<name>[-\w]+)/(?P<pk>[0-9]+)/$', UserEdit.as_view(), name='edit_user'),
    url(r'^group/edit/(?P<name>[-\w]+)/(?P<pk>[0-9]+)/$', GroupEdit.as_view(), name='edit_group'),
]
