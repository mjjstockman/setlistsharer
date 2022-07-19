from django.urls import path
from addimage.views import add_image
from .views import add, edit, detail, delete, agree, disagree


urlpatterns = [
    path('add/<str:pk>/', add, name='add_setlist'),
    path('edit/<str:pk>/', edit, name='edit_setlist'),
    path('detail/<str:pk>/', detail, name='detail_setlist'),
    path('delete/<str:pk>/', delete, name='delete_setlist'),
    path('agree/<str:pk>/', agree, name='agree'),
    path('disagree/<str:pk>/', disagree, name='disagree'),
    path('add-image/<str:pk>/', add_image, name='add_image'),
]

