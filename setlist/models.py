from django.db import models
from django.contrib.auth.models import User
from datetime import date
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, 'No Setlist'), (1, 'Waiting Confirmation'), (2, 'Published'))

class Venue(models.Model):
    """A class to represent a venue.

    Attributes
    name (char): name of venue
    city (char): the city the venue is in

    Returns:
        string: the name of the venue
    """
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Song(models.Model):
    """A class to represent a song.

    Attributes
    title (char): the name of the song

    Returns:
        string: the name of the song
    """
    title = models.CharField(max_length=200, unique=True, null=False)


    def __str__(self):
        return self.title


class Release(models.Model):
    """A class to represent a release.

    Attributes
    title (char): name of the release
    songs (m2m with Song model): a Song object

    Returns:
        string: the name of the release
    """
    title = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song, related_name="releases")


    def __str__(self):
        return self.title


class Setlist(models.Model):
    """A class to represent a setlist.

    Attributes
    gig (121 with Gig model): a Gig object
    author (FK in User model): a User object
    songs (m2m with Song model): a Song object
    status (integer): 0 = No Setlist, 1 = Setlist Waiting Confirmation,
        2 = Published Setlist
    agree (m2m with User model): User object
    disagree (m2m with User model): User object
    Returns:
        string: the <venue name> on <gig date>
    """
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

    def __str__(self):
        return f"{self.gig.venue} on {self.gig.date}"
