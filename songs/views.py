from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Song

songs_datas = Song.objects.all()

songs = {
    'songs': songs_datas
}

def index(request):
    return render(request, 'index.html', songs)

def song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)

    song_to_display = {
        'song': song
    }

    return render(request, 'song.html', song_to_display)