# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import EntryTitle
from .forms import EntryTitleForm

# Create your views here.


def index(request):
    """The home page for Journal"""
    return render(request, 'entries/index.html')


def titles(request):
    titles1 = EntryTitle.objects.order_by('date_added')
    context = {'titles': titles1}
    return render(request, 'entries/titles.html', context)


def title(request, titles_id):
    title2 = EntryTitle.objects.get(id=titles_id)
    entries = title2.entry_set.order_by('-date_added')
    context = {'title': title2, 'entries': entries}
    return render(request, 'entries/title.html', context)


def new_title(request):
    if request.method != 'POST':
        form = EntryTitleForm()
    else:
        form = EntryTitleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('entries:titles'))

    context = {'form' : form}
    return render(request, 'entries/new_title.html', context)
