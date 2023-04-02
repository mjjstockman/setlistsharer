from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from home.views import Gig
from .forms import SetlistAddForm, SetlistEditForm
from .models import Setlist


@login_required
def add(request, pk):
    """Adds a setlist to the database for the admin to consider
    """
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


@login_required
def edit(request, pk):
    """Allows authors to edit their setlists
    """
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
    """View setlist details
    """
    setlist = Setlist.objects.get(id=pk)
    context = {
        'setlist': setlist,
    }
    return render(request, 'setlist/detail.html', context)


@login_required
def delete(request, pk):
    """Allows the setlist author to delete the setlist
    """
    setlist = Setlist.objects.get(id=pk)

    if request.method == 'POST':
        setlist.delete()
        return redirect('/')

    context = {
        'setlist': setlist,
    }
    return render(request, 'setlist/delete.html', context)


@login_required
def like(request, pk):
    """Allows user to like or remove a setlist like
    """
    setlist = get_object_or_404(Setlist, id=pk)
    if setlist.agree.filter(id=request.user.id).exists():
        setlist.agree.remove(request.user)
    else:
        setlist.agree.add(request.user)

    return HttpResponseRedirect(reverse("detail_setlist", args=[pk]))
