from django.shortcuts import render
from django.views.generic import View, TemplateView

from clinic.models import Clinic
from core.models import Doctor

from .mixins import ViewMixin
from . import pages_info as info


class IndexView(ViewMixin):
    title = info.index_title
    description = info.index_description
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clinics"] = Clinic.objects.all()[:6]
        context["doctors"] = Doctor.objects.all()
        return context
    
    
class FAQView(ViewMixin):
    title = info.faq_title
    description = info.faq_description
    template_name = 'FAQ.html'


class ContactView(ViewMixin):
    title = info.contact_title
    description = info.contact_description
    template_name = 'contact.html'