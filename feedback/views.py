from random import randint

from django.views.generic import FormView

from .models import Recaptcha
from .forms import CreateStatementForm
from . import pages_info as info

    
class ContactView(FormView):
    form_class = CreateStatementForm
    template_name = 'contact.html'
    success_url = '/thanks/'

    @staticmethod
    def get_recaptcha(**kwargs):
        count = Recaptcha.objects.all().count()
        return Recaptcha.objects.all()[randint(0, int(count) - 1)]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = info.contact_title
        context["description"] = info.contact_description
        context["recaptcha"] = self.get_recaptcha()
        context["errors"] = False if not kwargs.get('errors') else True
        return context

    def form_valid(self, form):
        data = self.request.POST.get
        if int(data('answer_user')) == int(data('answer_recaptcha')):
            form.save()
            return super().form_valid(form)
        return self.render_to_response(self.get_context_data(errors=True))
