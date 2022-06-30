from django.db import models
from cloudinary.models import CloudinaryField
from home.models import Gig

# Create your models here.
STATUS = ((0, 'No Image'), (1, 'Image Waiting Confirmation'), (2, 'Published Image'))


class Image(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)


    # def __str__(self):
    #     return f"{self.venue} in {self.venue.city} on {self.date}"