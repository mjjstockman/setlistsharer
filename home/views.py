import random
from django.shortcuts import render
from setlist.models import Setlist
from .models import Gig


# Create your views here.

def gigs(request):
    """Gets all gig objects from the database
    creates a method to select a random number for gigs with no image
    """
    gigs = Gig.objects.all().order_by('date')
    image_num = range(0, 14)
    context = {
        'gigs': gigs,
        'image_num': image_num
    }
    return render(request, 'home/index.html', context)
