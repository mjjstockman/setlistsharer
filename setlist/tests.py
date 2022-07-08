from django.test import TestCase
from datetime import datetime
from django.test import Client
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from .views import add, edit, detail, delete, agree, disagree
from .models import Venue, Song, Release


class TestUrls(TestCase):   

    def test_add(self):
        url = reverse('add_setlist', args=[1])
        self.assertEqual(resolve(url).func, add)
        
    def test_edit(self):
        url = reverse('edit_setlist', args=[1])
        self.assertEqual(resolve(url).func, edit)
  
    def test_detail(self):
        url = reverse('delete_setlist', args=[1])
        self.assertEqual(resolve(url).func, delete)

    def test_agree(self):
        url = reverse('agree', args=[1])
        self.assertEqual(resolve(url).func, agree)

    def test_disagree(self):
        url = reverse('disagree', args=[1])
        self.assertEqual(resolve(url).func, disagree)


class TestViews(TestCase):

    def test_setlist_detail(self):

        Venue.objects.create(
            name = 'A Venue',
            city = 'A City',
        )

        song1 = Song.objects.create(
            title = 'A Title',
        )
       
        Release.objects.create(
            title = 'An Album',
            songs = song1
        )
