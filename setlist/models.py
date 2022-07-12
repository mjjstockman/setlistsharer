from django.db import models
from django.contrib.auth.models import User
from datetime import date
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, 'Waiting Confirmation'), (1, 'Published'))


class Venue(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False)
    # slug = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.title


class Release(models.Model):
    title = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song, related_name="releases")
    # slug = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.title


class Setlist(models.Model):
    gig = models.OneToOneField('home.Gig', related_name='setlist_gig',
                               on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    song = models.ManyToManyField(Song)
    status = models.IntegerField(choices=STATUS, default=0)
    agree = models.ManyToManyField(User, related_name='setlist_agree',
                                   blank=True)
    disagree = models.ManyToManyField(User, related_name='setlist_disagree',
                                      blank=True)

    class Meta:
        ordering = ['gig__date']

    # def __str__(self):
    #     return f"{self.gig.venue} on {self.gig.date}"

    # def __str__(self):
    #     return f"{self.song.title}"
