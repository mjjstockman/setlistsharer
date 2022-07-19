from django.urls import path
from .views import add_image

# Path to add an image
urlpatterns = [
    path('', add_image, name='add-image'),
]
