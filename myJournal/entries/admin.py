# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import EntryTitle, Entry


# Register your models here.


admin.site.register(EntryTitle)
admin.site.register(Entry)
