from django.contrib import admin
from .models import Album, Song
# Register your models here.

admin.site.register(Album) #rejestrujemy w panelu admin
admin.site.register(Song)