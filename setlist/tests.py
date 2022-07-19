from django.test import TestCase
from datetime import datetime
from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from home.models import Gig
from .views import add, edit, detail, delete, agree, disagree
from .models import Venue, Song, Release, Setlist


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

        venue1 = Venue.objects.create(
            name='A Venue',
            city='A City',
        )

        song1 = Song.objects.create(
            title='A Title',
        )
        
        release1 = Release.objects.create(
            title='An Album',
        )
        
        gig1=Gig.objects.create(
            date=datetime.now()
        )

        setlist1 = Setlist(status=0)
        setlist1.save()

        user1 = User.objects.create(
            username='user',
            password='dphgfsS34',
            email='c@c.com',
        )

        setlist1.gig = gig1

        setlist1.song.add(song1)