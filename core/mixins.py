from django.views.generic import View, TemplateView


class InfoMixin:
    
    @staticmethod
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["phone"] = '996707366749'
        return context