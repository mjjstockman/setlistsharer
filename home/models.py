from datetime import date
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, 'No Image'), (1, 'Image Waiting Confirmation'), (2, 'Published Image'))


class Gig(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True,
                            null=True)
    venue = models.ForeignKey('setlist.Venue', on_delete=models.CASCADE,
                              null=True)
    image = CloudinaryField('image', null=True, blank=True)
    image_status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.venue} in {self.venue.city} on {self.date}"