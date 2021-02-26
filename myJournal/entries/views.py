# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import EntryTitle
# Create your views here.


def index(request):
    """The home page for Journal"""
    return render(request, 'entries/index.html')


def titles(request):
    titles1 = EntryTitle.objects.order_by('date_added')
    context = {'titles': titles1}
    return render(request, 'entries/titles.html', context)
