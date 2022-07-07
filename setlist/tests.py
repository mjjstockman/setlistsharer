from django.test import TestCase
from datetime import datetime
# from django.test import SimpleTestCase, TestCase, Client
# from django.core.urlresolvers import reverse
from django.test import Client
from django.urls import reverse, resolve
from django.test import SimpleTestCase
# from .models import Gig
# from .views import gigs
# Create your tests here.


# class TestUrls(SimpleTestCase):        
#     def test_home_url(self):
#         url = reverse('index')
#         self.assertEqual(resolve(url).func, gigs)



class TestViews(TestCase):   

    def setUp(self):
        self.user = User.objects.create(username='myname', password='batTab21', email='a@a.com')
        self.venue = Venue.objects.create(name='Rock City', city='Nottingham')
        self.song = Song.objects.create(title='A Song')
        self.release = Release.objects.create(title='An Album', songs='A Song')
        self.setlist = Setlist.objects.create(gig='A Song')
        self.song = Song.objects.create(title='A Song')
        self.song = Song.objects.create(title='A Song')
        self.song = Song.objects.create(title='A Song')
        self.song = Song.objects.create(title='A Song')



    #     self.client = Client() 
    #     self.setlist_detail_url = reverse('setlist/detail/1')

    # def test_setlist_detail(self):
    #     response = self.client.get(self.setlist_detail_url)
    #     self.assertTemplateUsed(response, 'setlist/detail.html')
    #     self.assertTemplateUsed(response, 'base.html')



# from django.test import TestCase

# Create your tests here.
# from django.test import TestCase
# from django.test import SimpleTestCase, TestCase, Client
# from django.test import Client
# from django.urls import reverse, resolve
# from .models import Gig
# from .views import edit
# Create your tests here.

#  path('add/<str:pk>/', add, name='add_setlist'),
#     path('edit/<str:pk>/', edit, name='edit_setlist'),
#     path('detail/<str:pk>/', detail, name='detail_setlist'),
#     path('delete/<str:pk>/', delete, name='delete_setlist'),
#     path('agree/<str:pk>/', agree, name='agree'),
#     path('disagree/<str:pk>/', disagree, name='disagree'),
#     path('add-image/<str:pk>/', add_image, name='add_image'),

# class TestUrls(SimpleTestCase):        
#     def test_setlist_edit_url(self):
#         url = reverse('edit/1', args=[1])
#         self.assertEqual(resolve(url).func, edit)

# if __name__ == '__main__':
#     unittest.main()