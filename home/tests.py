from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Gig
# Create your tests here.


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        testgig = Gig.objects.create()

        
    def testhome(self):
        response = self.client.get(reverse('index'))
        print(response.content)
        print(response.headers)
        print(response.reason_phrase)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'base.html')

if __name__ == '__main__':
    unittest.main()