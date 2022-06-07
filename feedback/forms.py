from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

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

