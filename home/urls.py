from django.urls import path
from .views import gigs

# Path to the home page
urlpatterns = [
    path('', gigs, name='index'),
]
