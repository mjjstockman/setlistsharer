from django import forms
from home.models import Gig


class AddImageForm(forms.ModelForm):
    """Uses Gig model to create form with a image field
    """
    class Meta:
        model = Gig
        fields = ['image']
