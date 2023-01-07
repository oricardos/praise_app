from django.shortcuts import render

songs_datas = {
    'song_name': '',
    'lyric': '',
    'tone': '',
    'cipher': '',
    'bpm': '',
    'video': '',
    'author': '',
    'spotify': '',
    'ytmusic': '',
    'deezer': '',
    'amazon': '',
    'matters': ''
    }

def index(request):
    return render(request, 'index.html', songs_datas)

def song(request):
    return render(request, 'song.html')