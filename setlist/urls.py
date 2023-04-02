from django.urls import path
from addimage.views import add_image
from .views import add, edit, detail, delete, agree, like
from . import views


urlpatterns = [
    path('add/<str:pk>/', add, name='add_setlist'),
    path('edit/<str:pk>/', edit, name='edit_setlist'),
    path('detail/<str:pk>/', detail, name='detail_setlist'),
    path('delete/<str:pk>/', delete, name='delete_setlist'),
    # path('agree/<str:pk>/', agree, name='agree'),
    # path('like/<str:pk>/', like, name='like'),
    # path('agree/<str:pk>', views.SetlistAgree.as_view(), name='setlist_agree'),
    # path('disagree/<str:pk>/', disagree, name='disagree'),
    path('like/<str:pk>/', like, name='like'),
    path('add-image/<str:pk>/', add_image, name='add_image'),
]

