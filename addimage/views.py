from django.shortcuts import render, redirect
from cloudinary.forms import cl_init_js_callbacks
from django.contrib.auth.decorators import login_required
from home.models import Gig
from .forms import AddImageForm



@login_required
def add_image(request, pk):
    gig = Gig.objects.get(id=pk)

    
    form = AddImageForm(request.POST, request.FILES, instance=gig)
    if request.method == 'POST':
        if form.is_valid():
            gig.image_status = 1
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'addimage/add-image.html', context)