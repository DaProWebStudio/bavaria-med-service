from django.views.generic import ListView, TemplateView

from .models import Clinic

from core.mixins import ViewMixin
from clinic import pages_info as info


class ClinicView(ListView):
    model = Clinic
    context_object_name = 'clinics'
    template_name = 'clinics.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = info.clinic_title
        context["description"] = info.clinic_description
        return context
    
