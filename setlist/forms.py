from django import forms
from .models import Setlist


class SetlistAddForm(forms.ModelForm):
    """Uses Setlist model to create form gigs, song and author fields
    The gig and author fields are taken from the views and hidden from 
    the user 
    """
    class Meta:
        model = Setlist
        fields = ['gig', 'song', 'author']
        widgets = {
            'gig': forms.HiddenInput(),
            'author': forms.HiddenInput(),
            }


class SetlistEditForm(forms.ModelForm):
    """Uses Setlist model to create form gigs and songs to be edited
    The gig field is taken from the views and hidden from 
    the user 
    """
    class Meta:
        model = Setlist
        fields = ['gig', 'song']
        widgets = {
            'gig': forms.HiddenInput(),
            }
