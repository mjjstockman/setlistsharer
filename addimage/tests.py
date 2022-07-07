from django.test import TestCase
from datetime import datetime
# from django.test import SimpleTestCase, TestCase, Client
# from django.core.urlresolvers import reverse
from django.test import Client
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from .views import add_image

# Create your tests here.


class TestUrls(SimpleTestCase):
          
    def test_addimage_url(self):
        url = reverse('add-image', args=[1])
        self.assertEqual(resolve(url).func, add_image)