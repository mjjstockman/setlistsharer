from django.contrib import admin
from .models import Venue, Song, Release, Gig, Setlist

admin.site.register(Venue)
admin.site.register(Song)
admin.site.register(Release)
admin.site.register(Gig)
admin.site.register(Setlist)
