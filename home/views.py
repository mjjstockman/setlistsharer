import random
from django.shortcuts import render
from setlist.models import Setlist
from .models import Gig
# from .forms import 

# Create your views here.

def gigs(request):
    gigs = Gig.objects.all().order_by('date')
    random_num = random.randrange(0, 14)
    

    context = {
        'gigs': gigs,
        'random_num': random_num
    }
    return render(request, 'home/index.html', context)

