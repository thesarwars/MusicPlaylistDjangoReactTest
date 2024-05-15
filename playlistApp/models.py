from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    track_url = models.URLField()
    is_public = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title
    
class Playlist(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    tracks = models.ManyToManyField(Track, related_name="Music_Track")
    
    
    def __str__(self) -> str:
        return self.name