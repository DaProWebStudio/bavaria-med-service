from django.shortcuts import render
from django.views.generic import View, TemplateView

from core.mixins import ViewMixin


class ServiceView(ViewMixin):
    title = ''
    description = ''
    template_name = 'service.html'
    
    
class DiagnosticsView(ViewMixin):
    title = ''
    description = ''
    template_name = 'diagnostics.html'
    
    
class SupportView(ViewMixin):
    title = ''
    description = ''
    template_name = 'support.html'