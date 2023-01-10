from django.db import models
from datetime import datetime
from artists.models import Artist

class Song(models.Model):
    #geral
    is_posted = models.BooleanField(default=True)
    song_name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    matters = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    playback = models.CharField(max_length=200, blank=True)
    spotify = models.CharField(max_length=200)
    ytmusic = models.CharField(max_length=200)
    featured_image = models.CharField(default="", max_length=250, blank=True)
    note = models.TextField(blank=True) #observações

    #  VOZES
    lyric = models.TextField()
    voices = models.CharField(max_length=200, blank=True)
    extra_voice = models.CharField(max_length=200, blank=True)
    
    # INSTRUMENTOS
    tone = models.CharField(max_length=200)
    cipher = models.CharField(max_length=200)
    bpm = models.IntegerField()

    acoustic_guitar = models.CharField(max_length=200, blank=True)
    electric_guitar = models.CharField(max_length=200, blank=True)
    keyboard = models.CharField(max_length=200, blank=True)
    bass = models.CharField(max_length=200, blank=True)
    drums = models.CharField(max_length=200, blank=True)

    date_posted = models.DateTimeField(default=datetime.now, blank=True) #se por algum motivo não conseguir pegar a data, pode ficar vazio

    # mostra o nome da música no admin
    def __str__(self):
        return self.song_name
