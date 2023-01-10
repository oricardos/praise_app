from django.contrib import admin
from .models import Song

class ListSongs(admin.ModelAdmin):
    # mostra nome da música e assunto
    list_display = ('song_name', 'matters')
    # adiciona um campo de busca e precisa da vírgula
    search_fields = ('song_name',)
    # adiciona um filtro por assunto e precisa da vírgula
    list_filter = ('matters',)
    # adiciona paginação, 10 por página
    list_per_page = 10
    # list_display_links = ('song_name') transforma uma informação em um link

admin.site.register(Song, ListSongs) # sempre passar a classe aqui pra pegar filtro, busca e paginação...