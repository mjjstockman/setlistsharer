from django.shortcuts import render

# Create your views here.
from .forms import SetlistForm


def add(request):
    form = SetlistForm()


    context = {
        'form': form
    }
    return render(request, 'add.html', context)