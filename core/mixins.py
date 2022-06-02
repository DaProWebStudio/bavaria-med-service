from django.shortcuts import render
from django.views.generic import View, TemplateView


class ViewMixin(View):
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {'title': self.title, 'description': self.description})