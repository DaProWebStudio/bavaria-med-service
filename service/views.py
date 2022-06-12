from django.views.generic import ListView, TemplateView

from .models import ClinicService, Service
from core.mixins import ViewMixin
from service import pages_info as info


class ServiceView(ListView):
    model = Service
    context_object_name = 'services'
    extra_context = {
            "title": info.service_title, 
            "description": info.service_description
        }
    template_name = 'services/service.html'
    
    
class ServiceDetailView(TemplateView):
    template_name = 'services/service_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = Service.objects.get(slug=kwargs.get('slug'))
        context["clinics"] = ClinicService.objects.filter(service__slug=kwargs.get('slug')).select_related('clinic').values('clinic__title', 'clinic__slug')
        context["title"] = context["service"].title
        context["description"] = info.service_description
        return context


class DiagnosticsView(ViewMixin):
    title = info.diagnostics_title
    description = info.diagnostics_description
    template_name = 'diagnostics.html'
    
    
class SupportView(ViewMixin):
    title = info.support_title
    description = info.support_description
    template_name = 'support.html'