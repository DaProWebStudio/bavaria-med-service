import json
from django.views.generic import ListView, TemplateView, View
from django.http.response import JsonResponse

from .models import ClinicService, Service, ServiceLetter
from service import pages_info as info

from core.mixins import ViewMixin
from core.services.translit import translit_slug

class ServiceView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'services/service.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        context["letters"] = ServiceLetter.objects.all().values('letter', 'pk')
        context["title"] = info.service_title
        context["description"] = info.service_description
        return context
    
    
class ServiceDetailView(TemplateView):
    template_name = 'services/service_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = Service.objects.get(slug=kwargs.get('slug'))
        context["clinics"] = ClinicService.objects.filter(service__slug=kwargs.get('slug')).select_related('clinic').values('clinic__title', 'clinic__slug')
        context["title"] = context["service"].title
        context["description"] = info.service_description
        return context


class ServiceLetterJsonResponse(View):
    
    def get(self, *args, **kwargs):
        letter = ServiceLetter.objects.prefetch_related('services').get(pk=kwargs.get('pk'))
        data = {
            'services': list(letter.services.all().values("title", 'slug'))
            }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': True}) 


class DiagnosticsView(ViewMixin):
    title = info.diagnostics_title
    description = info.diagnostics_description
    template_name = 'diagnostics.html'
    
    
class SupportView(ViewMixin):
    title = info.support_title
    description = info.support_description
    template_name = 'support.html'