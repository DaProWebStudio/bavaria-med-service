from django.urls import reverse
from django.views.decorators.http import require_GET
from django.contrib.sitemaps import Sitemap  
from django.http import HttpResponse

from .models import Clinic, Doctor
from service.models import Service
from core import urls as core_urls
from service import urls as service_urls


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        core_urls_list = [url.name for url in core_urls.urlpatterns if url.name != 'clinic-detail']
        service_urls_list = [url.name for url in service_urls.urlpatterns if url.name != 'service-detail']
        return core_urls_list + service_urls_list

    def location(self, item):
        return reverse(item)
    

class ClinicSitemap(Sitemap):  
    changefreq = 'monthly'  
    priority = 0.9
  
    def items(self):  
        return Clinic.objects.all()  
      
    def lastmod(self, obj):  
        return obj.updated_at


class DoctorSitemap(Sitemap):  
    changefreq = 'monthly'  
    priority = 0.8
  
    def items(self):  
        return Doctor.objects.all()  
      
    def lastmod(self, obj):  
        return obj.updated_at


class ServiceSitemap(Sitemap):  
    changefreq = 'weekly'  
    priority = 1
  
    def items(self):  
        return Service.objects.all()  
      
    def lastmod(self, obj):  
        return obj.updated_at


sitemaps = {  
    'static': StaticViewSitemap,
    'clinic': ClinicSitemap,
    'doctor': DoctorSitemap,
    'service': ServiceSitemap,
}

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
        "Host: www.bavariamed.ru",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")