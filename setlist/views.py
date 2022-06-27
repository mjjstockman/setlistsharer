from django.shortcuts import render, redirect

# Create your views here.
from home.views import Gig
from .forms import SetlistAddForm, SetlistEditForm
from .models import Setlist
from home.views import Gig


def add(request, pk):  
    gig = Gig.objects.get(id=pk)
    author = request.user
    initial = {
        'gig': gig,
        'author': author,
    }

    form = SetlistAddForm(initial=initial)
    if request.method == 'POST':
        form = SetlistAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'add.html', context)


def edit(request, pk):
    setlist = Setlist.objects.get(id=pk)
    form = SetlistEditForm(instance=setlist)

    if request.method == 'POST':
        form = SetlistEditForm(request.POST, instance=setlist)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }    
    return render(request, 'add.html', context)