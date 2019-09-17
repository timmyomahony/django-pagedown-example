from django.contrib import admin
from django.db import models

from music.models import Artist, Song, Album
from music.forms import AdminAlbumForm, AdminSongForm

from pagedown.widgets import AdminPagedownWidget


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class SongInline(admin.StackedInline):
    model = Song
    form = AdminSongForm
    extra = 0


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    form = AdminSongForm


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    form = AdminAlbumForm
    inlines = (SongInline,)
