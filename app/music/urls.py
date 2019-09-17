from django.urls import include, path

from music import views


app_name = 'music'

song_patterns = ([
    path('create/', views.SongCreateView.as_view(), name='create'),
    path('<int:pk>/', views.SongDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.SongUpdateView.as_view(), name='update'),
    path('', views.SongListView.as_view(), name='list'),
], 'songs')

album_patterns = ([
    path('create/', views.AlbumCreateView.as_view(), name='create'),
    path('<int:pk>/', views.AlbumDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.AlbumUpdateView.as_view(), name='update'),
    path('', views.AlbumListView.as_view(), name='list'),
], 'albums')

artist_patterns = ([
    path('create/', views.ArtistCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ArtistDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ArtistUpdateView.as_view(), name='update'),
    path('', views.ArtistListView.as_view(), name='list'),
], 'songs')

urlpatterns = [
    path('songs/', include(song_patterns, namespace='songs')),
    path('albums/', include(album_patterns, namespace='albums')),
    path('artists/', include(artist_patterns, namespace='artists'))
]
