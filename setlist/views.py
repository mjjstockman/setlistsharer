from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
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
def agree(request, pk):
    """A user can agree with a setlist

    TODO: merge agree/disagree logic 
    """
    setlist = Setlist.objects.get(id=pk)
    disagree = False

    for disagree in setlist.disagree.all():
        if disagree == request.user:
            disagree = True
            break

    if disagree:
        setlist.disagree.remove(request.user)

    agree = False

    for agree in setlist.agree.all():
        if agree == request.user:
            agree = True
            break

    if not agree:
        setlist.agree.add(request.user)

    if agree:
        setlist.agree.remove(request.user)

    return redirect(request.META['HTTP_REFERER'])


@login_required
def disagree(request, pk):
    """A user can disagree with a setlist

    TODO: merge agree/disagree logic 
    """
    setlist = get_object_or_404(Setlist, id=request.POST.get('setlist_id'))

    agree = False

    for agree in setlist.agree.all():
        if agree == request.user:
            agree = True
            break

    if agree:
        setlist.agree.remove(request.user)

    disagree = False

    for disagree in setlist.disagree.all():
        if disagree == request.user:
            disagree = True
            break

    if not disagree:
        setlist.disagree.add(request.user)

    if disagree:
        setlist.disagree.remove(request.user)

    return redirect(request.META['HTTP_REFERER'])