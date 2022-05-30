from django.shortcuts import render
from django.views.generic import View, TemplateView

from core.mixins import InfoMixin


class ServiceView(TemplateView, InfoMixin):
    template_name = 'service.html'
    
    
class DiagnosticsView(TemplateView, InfoMixin):
    template_name = 'diagnostics.html'