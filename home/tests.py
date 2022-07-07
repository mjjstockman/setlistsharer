from django.test import TestCase
from datetime import datetime
# from django.test import SimpleTestCase, TestCase, Client
# from django.core.urlresolvers import reverse
from django.test import Client
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from .models import Gig
from .views import gigs
# Create your tests here.


class TestUrls(SimpleTestCase):
          
    def test_home_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, gigs)



class TestViews(TestCase):   

    def setUp(self):
        self.client = Client() 
        self.index_url = reverse('index')

    def test_home_view(self):
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'base.html')




# class TestGig(TestCase):
#     def test_create_gig(self):
#         gig1 = Gig(datetime(2022, 7, 3), 'Sidney')


# class TestViews(TestCase):
#     def test_get_home_page(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'base.html')
        # self.assertTemplateUsed(response, 'index.html')


# class TestViews(TestCase):
  

    # def test_gig_detail(self):
    #     obj = self.create_gig(venue="Sidney")
    #     detail_url = reverse("gig:gig_detail", kwargs={'id': obj.id})
    #     response = self.client.get(detail_url)
    #     self.assertTrue(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()