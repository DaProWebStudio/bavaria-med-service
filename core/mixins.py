from django.shortcuts import render
from django.views.generic import View, TemplateView


class ViewMixin(View):
    
    def get(self, *args, **kwargs):
        context = {
            'title': self.title, 
            'description': self.description
        }
        return render(self.request, self.template_name, context)