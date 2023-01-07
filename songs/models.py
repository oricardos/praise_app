from django.db import models
from datetime import datetime

class Song(models.Model):
    song_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    matters = models.CharField(max_length=200)
    lyric = models.TextField()
    tone = models.CharField(max_length=200)
    cipher = models.CharField(max_length=200)
    bpm = models.IntegerField()
    video = models.CharField(max_length=200)
    spotify = models.CharField(max_length=200)
    ytmusic = models.CharField(max_length=200)
    featured_image = models.CharField(default="", max_length=250)
    date_posted = models.DateTimeField(default=datetime.now, blank=True) #se por algum motivo não conseguir pegar a data, pode ficar vazio

    def __str__(self):
        return self.song_name
