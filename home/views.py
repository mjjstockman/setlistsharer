import random
from django.shortcuts import render
from setlist.models import Setlist
from .models import Gig
# from .forms import 

# Create your views here.

def gigs(request):
    gigs = Gig.objects.all().order_by('date')
    image_num = range(0, 14)
    context = {
        'gigs': gigs,
        'image_num': image_num
    }
    return render(request, 'home/index.html', context)

