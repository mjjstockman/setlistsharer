from django.shortcuts import render
from .models import Gig


def gigs(request):
    gigs = Gig.objects.all()
    context = {
        'gigs': gigs,
    }
    return render(request, 'home/index.html', context)