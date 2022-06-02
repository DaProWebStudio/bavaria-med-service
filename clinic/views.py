from django.shortcuts import render
from django.views.generic import View, TemplateView

from core.mixins import ViewMixin


class ClinicView(ViewMixin):
    title = ''
    description = ''
    template_name = 'clinics.html'
