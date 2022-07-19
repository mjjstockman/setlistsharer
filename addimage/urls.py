from django.urls import path
from .views import add_image


urlpatterns = [
    path('', add_image, name='add-image'),
]
