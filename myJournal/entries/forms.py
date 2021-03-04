from django import forms

from .models import EntryTitle, Entry


class EntryTitleForm(forms.ModelForm):

    class Meta:
        model = EntryTitle
        fields = ['text', 'public']
        labels = {'text': '', 'public': 'Post Publicly'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
