from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .models import Statement


class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = 'required'
            visible.field.widget.attrs['placeholder'] = visible.label
            

class CreateStatementForm(BaseForm):
    class Meta:
        model = Statement
        fields = ['full_name', 'email', 'phone', 'region', 'message']
        widgets = {'message': Textarea(attrs={"minlength": "20", "maxlength": "5000", "style": "height: 200px"})}

    def send_statement(self):
        full_name = self.cleaned_data["full_name"]
        title_send = f'На сайт поступило новая завка от {full_name}'
        title, from_email = settings.EMAIL_TITLE_FROM, settings.EMAIL_HOST_USER
        to_form_1, to_form_2 = 'Adi Kambarov <adikgk@mail.ru>', 'Adi Estebes uulu <adikgk232323@gmail.com>'
        headers = {'From': f'{title} <{from_email}>'}
        context = {
            'full_name': full_name, 
            'email': self.cleaned_data["email"], 
            'phone': self.cleaned_data["phone"], 
            'region': self.cleaned_data["region"], 
            'message': self.cleaned_data["message"]
        }
        html_content = render_to_string('email/send_statement.html', context)  
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(title_send, text_content, from_email, [to_form_1, to_form_2], headers=headers)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)