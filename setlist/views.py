from django.shortcuts import render, redirect

# Create your views here.
from .forms import SetlistForm


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
