from django.views.generic import ListView, TemplateView

from .models import Clinic
from clinic import pages_info as info


class ClinicsView(ListView):
    model = Clinic
    context_object_name = 'clinics'
    extra_context = {
        "title": info.clinic_title, 
        "description": info.clinic_description
        }
    template_name = 'clinics.html'
    
    
class ClinicDetailView(TemplateView):
    template_name = 'clinic_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clinic"] = Clinic.objects.get(slug=kwargs.get('slug'))
        context["title"] = context["clinic"].title
        context["description"] = info.clinic_description
        return context
    