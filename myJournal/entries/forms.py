from django import forms

from .models import EntryTitle


class EntryTitleForm(forms.ModelForm):
    class Meta:
        model = EntryTitle
        fields = ['text']
        labels = {'text': ''}
