# from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client
from django.urls import reverse, resolve
from .models import Gig
from .views import gigs
# Create your tests here.


class TestViews(SimpleTestCase):        
    def test_home_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, gigs)

if __name__ == '__main__':
    unittest.main()