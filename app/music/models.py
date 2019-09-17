from django.db import models
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=128)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music:artists:detail', args=[str(self.id)])


class Album(models.Model):
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music:albums:detail', args=[str(self.id)])


class Song(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    lyrics = models.TextField(blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music:songs:detail', args=[str(self.id)])
