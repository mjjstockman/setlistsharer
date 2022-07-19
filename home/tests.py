from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from .views import gigs


# class TestUrls(SimpleTestCase):
          
#     def test_home_url(self):
#         url = reverse('index')
#         self.assertEqual(resolve(url).func, gigs)


# class TestViews(TestCase):   

#     def setUp(self):
#         self.client = Client() 
#         self.index_url = reverse('index')

#     def test_home_view(self):
#         response = self.client.get(self.index_url)
#         self.assertTemplateUsed(response, 'home/index.html')
#         self.assertTemplateUsed(response, 'base.html')


# if __name__ == '__main__':
#     unittest.main()