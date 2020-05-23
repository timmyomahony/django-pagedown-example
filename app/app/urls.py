from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('pagedown.urls')),
    path('admin/', admin.site.urls),
    path('music/', include('music.urls', namespace='music')),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
