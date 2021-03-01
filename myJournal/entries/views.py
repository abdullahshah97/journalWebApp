# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import EntryTitle, Entry
from .forms import EntryTitleForm, EntryForm


# Create your views here.


def index(request):
    """The home page for Journal"""
    return render(request, 'entries/index.html')


@login_required
def titles(request):
    titles1 = EntryTitle.objects.filter(owner=request.user).order_by('date_added')
    context = {'titles': titles1}
    return render(request, 'entries/titles.html', context)


@login_required
def title(request, titles_id):
    title2 = EntryTitle.objects.get(id=titles_id)
    entries = title2.entry_set.order_by('-date_added')
    context = {'title': title2, 'entries': entries}
    return render(request, 'entries/title.html', context)


@login_required
def new_title(request):
    if request.method != 'POST':
        form = EntryTitleForm()
    else:
        form = EntryTitleForm(request.POST)
        if form.is_valid():
            new_title = form.save(commit=False)
            new_title.owner = request.user
            new_title.save()
            return HttpResponseRedirect(reverse('entries:titles'))

    context = {'form': form}
    return render(request, 'entries/new_title.html', context)


@login_required
def new_entry(request, title_id):
    title = EntryTitle.objects.get(id=title_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.title = title
            new_entry.save()
            return HttpResponseRedirect(reverse('entries:title', args=[title_id]))

    context = {'title': title, 'form': form}
    return render(request, 'entries/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    title = entry.title

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('entries:title', args=[title.id]))
    context = {'entry': entry, 'title': title, 'form': form}
    return render(request, 'entries/edit_entry.html', context)
