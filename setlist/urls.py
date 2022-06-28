# from django.contrib import admin
from django.urls import path
from .views import add, edit, detail

urlpatterns = [
    # path('', get_setlists, name='setlist'),
    path('add/<str:pk>/', add, name='add_setlist'),
    path('edit/<str:pk>/', edit, name='edit_setlist'),
    path('detail/<str:pk>/', detail, name='detail_setlist'),
    # path('delete/<str:pk>/', delete, name='delete_setlist'),
]
