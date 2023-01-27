from django.shortcuts import render, get_object_or_404, redirect
from .models import Song
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

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

# PESQUISA
def search(request):
    songs_datas_list = Song.objects.order_by('-song_name').filter(is_posted=True)

    if 'search' in request.GET:
        search_name = request.GET['search']
        if search:
            songs_datas_list = songs_datas_list.filter(song_name__icontains=search_name)

    data = {
        'songs': songs_datas_list
    }

    return render(request, 'search.html', data)