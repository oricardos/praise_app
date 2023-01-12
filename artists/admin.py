from django.contrib import admin
from .models import Artist

class ListArtist(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Artist, ListArtist) # sempre passar a classe aqui pra pegar filtro, busca e paginação...
