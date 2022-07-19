from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, 'No Image'), (1, 'Waiting Confirmation'), (2, 'Published'))


class Gig(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True,
                            null=True)
    venue = models.ForeignKey('setlist.Venue', on_delete=models.CASCADE,
                              null=True)
    image = CloudinaryField('image', null=True, blank=True)
    image_status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.venue} in {self.venue.city} on {self.date}"
