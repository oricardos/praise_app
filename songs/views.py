from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Song

def index(request):
    songs_datas = Song.objects.order_by('-song_name').filter(is_posted=True)

    songs = {
        'songs': songs_datas
    }
    return render(request, 'index.html', songs)

# MÚSICAS
def song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)

    song_to_display = {
        'song': song
    }

    return render(request, 'song.html', song_to_display)

# VOZES
def voice(request, song_id):
    song = get_object_or_404(Song, pk=song_id)

    song_to_display = {
        'song': song
    }

    return render(request, 'voice.html', song_to_display)

# INSTRUMENTAL
def instrumental(request, song_id):
    song = get_object_or_404(Song, pk=song_id)

    song_to_display = {
        'song': song
    }

    return render(request, 'instrumental.html', song_to_display)