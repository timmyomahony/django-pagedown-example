from django import forms

from music.models import Artist, Album, Song

from pagedown.widgets import AdminPagedownWidget, PagedownWidget


# Admin forms

class AdminAlbumForm(forms.ModelForm):
    description = forms.CharField(
        widget=AdminPagedownWidget(),
        max_length=500)

    class Meta:
        model = Album
        fields = '__all__'


class AdminSongForm(forms.ModelForm):
    description = forms.CharField(
        widget=AdminPagedownWidget(),
        max_length=500)
    lyrics = forms.CharField(
        widget=AdminPagedownWidget(),
        max_length=500)

    class Meta:
        model = Song
        fields = '__all__'


# General forms


class ArtistForm(forms.ModelForm):
    about = forms.CharField(
        widget=PagedownWidget())

    class Meta:
        model = Artist
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    description = forms.CharField(
        widget=PagedownWidget())

    class Meta:
        model = Album
        fields = '__all__'


class SongForm(forms.ModelForm):
    description = forms.CharField(
        widget=PagedownWidget())
    lyrics = forms.CharField(
        widget=PagedownWidget())

    class Meta:
        model = Song
        fields = '__all__'
