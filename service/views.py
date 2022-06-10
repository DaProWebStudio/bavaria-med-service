from django.views.generic import View, TemplateView

from core.mixins import ViewMixin
from service import pages_info as info


class ServiceView(ViewMixin):
    title = info.service_title
    description = info.service_description
    template_name = 'service.html'
    
    
class DiagnosticsView(ViewMixin):
    title = info.diagnostics_title
    description = info.diagnostics_description
    template_name = 'diagnostics.html'
    
    
class SupportView(ViewMixin):
    title = info.support_title
    description = info.support_description
    template_name = 'support.html'