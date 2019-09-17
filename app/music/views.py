from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from music.models import Artist, Album, Song
from music.forms import ArtistForm, AlbumForm, SongForm


# Artist


class ArtistDetailView(DetailView):
    model = Artist


class ArtistListView(ListView):
    model = Artist


class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm


class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = ArtistForm


# Album


class AlbumDetailView(DetailView):
    model = Album


class AlbumListView(ListView):
    model = Album


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm


class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm


# Song


class SongDetailView(DetailView):
    model = Song


class SongListView(ListView):
    model = Song


class SongCreateView(CreateView):
    model = Song
    form_class = SongForm


class SongUpdateView(UpdateView):
    model = Song
    form_class = SongForm
