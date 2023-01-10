from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('song/<int:song_id>/', views.song, name="song"),
    path('voice/<int:song_id>/', views.voice, name="voice"),
    path('instrumental/<int:song_id>/', views.instrumental, name="instrumental"),
]