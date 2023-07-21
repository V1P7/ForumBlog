from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Forum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Forum.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include('hitcount.urls', namespace = 'hitcount')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)