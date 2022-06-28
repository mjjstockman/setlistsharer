from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from home.views import Gig
from .forms import SetlistAddForm, SetlistEditForm
from .models import Setlist




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
    return render(request, 'setlist/add.html', context)


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
    return render(request, 'setlist/add.html', context)


@login_required
def detail(request, pk):
    setlist = Setlist.objects.get(id=pk)
    context = {
        'setlist': setlist,
    }
    return render(request, 'setlist/detail.html', context)


def delete(request, pk):
    setlist = Setlist.objects.get(id=pk)

    if request.method == 'POST':
        setlist.delete()
        return redirect('/')
        
    context = {
        'setlist': setlist,
    }
    return render(request, 'setlist/delete.html', context)
