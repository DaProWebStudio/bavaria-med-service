from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include

from core.sitemaps import sitemaps, robots_txt
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('service/', include('service.urls')),
    path('contacts/', include('feedback.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt/", robots_txt),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    
handler404 = 'core.view.custom_page_not_found_view'
handler500 = 'core.view.custom_error_view'
handler403 = 'core.view.custom_permission_denied_view'
handler400 = 'core.view.custom_bad_request_view'