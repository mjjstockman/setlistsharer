from django import forms
from .models import Setlist


class SetlistAddForm(forms.ModelForm):
    class Meta:
        model = Setlist
        fields = ['gig', 'song', 'author']
        widgets = {
            'gig': forms.HiddenInput(),
            'author': forms.HiddenInput(),
            }


class SetlistEditForm(forms.ModelForm):
    class Meta:
        model = Setlist
        fields = ['gig', 'song']
        widgets = {
            'gig': forms.HiddenInput(),
            }


