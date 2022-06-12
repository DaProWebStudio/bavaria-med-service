from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Clinic, Doctor

from .mixins import ViewMixin
from . import pages_info as info


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = info.index_title
        context['description'] = info.index_description
        context["doctors"] = Doctor.objects.all()
        return context
    

class ClinicsView(ListView):
    model = Clinic
    context_object_name = 'clinics'
    extra_context = {
        "title": info.clinic_title, 
        "description": info.clinic_description
        }
    template_name = 'clinics/clinics.html'
    
    
class ClinicDetailView(TemplateView):
    template_name = 'clinics/clinic_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clinic"] = Clinic.objects.get(slug=kwargs.get('slug'))
        context["title"] = context["clinic"].title
        context["description"] = info.clinic_description
        return context


class FAQView(ViewMixin):
    title = info.faq_title
    description = info.faq_description
    template_name = 'FAQ.html'


class ContactView(ViewMixin):
    title = info.contact_title
    description = info.contact_description
    template_name = 'contact.html'
    

class ArticlesView(ViewMixin):
    title = info.articles_title
    description = info.articles_description
    template_name = 'articles/index.html'


class TreatmentArticlesView(ViewMixin):
    title = info.treatment_title
    description = info.articles_description
    template_name = 'articles/treatment.html'
    
    
class MotivationArticlesView(ViewMixin):
    title = info.motivation_title
    description = info.articles_description
    template_name = 'articles/motivation.html'
    
    
class ClinicArticlesView(ViewMixin):
    title = info.clinic_ar_title
    description = info.articles_description
    template_name = 'articles/clinic.html'
    

class GeneralArticlesView(ViewMixin):
    title = info.general_title
    description = info.articles_description
    template_name = 'articles/general.html'
    
    
def custom_page_not_found_view(request, exception=None):
    return render(request, "errors/404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})


def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})


def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})