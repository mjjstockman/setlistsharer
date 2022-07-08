from django.test import TestCase
from datetime import datetime
from django.test import Client
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from home.models import Gig
from .views import add, edit, detail, delete, agree, disagree
from .models import Venue, Song, Release, Setlist



class TestViews(TestCase):

    def test_setlist_detail(self):

        venue=Venue.objects.create(
            name='A Venue',
            city='A City',
        )

        song=Song.objects.create(
            title='A Title',
        )
       
        release=Release.objects.create(
            title='An Album',
        )

        setlist=Setlist.objects.create(
            status=0,
        )

        gig=Gig.objects.create(
            date=datetime.now()
        )

        
        user=User.objects.create(
            username='user',
            password='dphgfsS34',
            email='c@c.com',
        )

        # song.save()
        # gig.save()
        # venue.save()
        # release.save()
        # setlist.save()
        # user.save()

        release.songs.add(song)
        setlist.gig.add(gig)
      
      


    #   class TestUrls(TestCase):   

    # def test_add(self):
    #     url = reverse('add_setlist', args=[1])
    #     self.assertEqual(resolve(url).func, add)
        
    # def test_edit(self):
    #     url = reverse('edit_setlist', args=[1])
    #     self.assertEqual(resolve(url).func, edit)
  
    # def test_detail(self):
    #     url = reverse('delete_setlist', args=[1])
    #     self.assertEqual(resolve(url).func, delete)

    # def test_agree(self):
    #     url = reverse('agree', args=[1])
    #     self.assertEqual(resolve(url).func, agree)

    # def test_disagree(self):
    #     url = reverse('disagree', args=[1])
    #     self.assertEqual(resolve(url).func, disagree)