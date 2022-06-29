# from django.contrib import admin
from django.urls import path
from .views import add, edit, detail, delete, agree, disagree
from addimage.views import add_image

urlpatterns = [
    # path('', get_setlists, name='setlist'),
    path('add/<str:pk>/', add, name='add_setlist'),
    path('edit/<str:pk>/', edit, name='edit_setlist'),
    path('detail/<str:pk>/', detail, name='detail_setlist'),
    path('delete/<str:pk>/', delete, name='delete_setlist'),
    path('agree/<str:pk>/', agree, name='agree'),
    path('disagree/<str:pk>/', disagree, name='disagree'),
    path('add-image/', add_image, name='add_image'),
]
