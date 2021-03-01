# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('entries:index'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('entries:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)