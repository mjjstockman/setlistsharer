from django.urls import path
from .views import gigs



urlpatterns = [
    path('', gigs, name='index'),  
]