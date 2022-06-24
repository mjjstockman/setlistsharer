from django.shortcuts import render, redirect

# Create your views here.
from .forms import SetlistForm
from home.views import Gig


def add(request, pk):  
    gig = Gig.objects.get(id=pk)
    author = request.user
    initial = {
        'gig': gig,
        'author': author,
    }

    form = SetlistForm(initial=initial)
    if request.method == 'POST':
        form = SetlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'add.html', context)


def edit(request, pk):
    setlist = Setlist.objects.get(id=pk)
    form = SetlistForm(instance=setlist)

    if request.method == 'POST':
        form = SetlistForm(request.POST, instance=setlist)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'setlist/add.html', context)