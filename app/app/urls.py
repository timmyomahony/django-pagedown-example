from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls', namespace='music')),
    path('', TemplateView.as_view(template_name="index.html"), name='index')
]
