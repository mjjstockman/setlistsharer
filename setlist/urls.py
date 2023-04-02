from django.urls import path
from addimage.views import add_image
from .views import add, edit, detail, delete, like
from . import views


urlpatterns = [
    path('add/<str:pk>/', add, name='add_setlist'),
    path('edit/<str:pk>/', edit, name='edit_setlist'),
    path('detail/<str:pk>/', detail, name='detail_setlist'),
    path('delete/<str:pk>/', delete, name='delete_setlist'),
    path('like/<str:pk>/', like, name='like'),
    path('add-image/<str:pk>/', add_image, name='add_image'),
]

