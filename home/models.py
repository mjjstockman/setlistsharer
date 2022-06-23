from django.db import models
from datetime import date

# Create your models here.
# STATUS = ((0, 'Waiting Confirmation'), (1, 'Published'))

class Gig(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True,
                            null=True)
    venue = models.ForeignKey('setlist.Venue', on_delete=models.CASCADE,
                              null=True)
    # featured_image = CloudinaryField('image', null=True, blank=True)
    # featured_image_status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.venue} in {self.venue.city} on {self.date}"