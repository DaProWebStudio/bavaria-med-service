from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.services.translit import translit_slug


def upload_to_recaptcha(instance, filename):
    list_file = filename.split('.')
    return f'recaptcha/{translit_slug(list_file[0])}.{list_file[-1]}/'


class Statement(models.Model):
    full_name = models.CharField(_('Ваше имя'), max_length=50)
    email = models.EmailField(_('Ваша электронная почта'))
    phone = models.CharField(_('Контактный телефон'), max_length=80)
    region = models.CharField(_('Страна и город'), max_length=50)
    message = models.TextField(_('Ваше сообщение'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.full_name)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Заявка на лечение')
        verbose_name_plural = _('Заявки на лечение')


class Recaptcha(models.Model):
    image = models.ImageField(_('Изображение в Формате JPG 50X340'), upload_to=upload_to_recaptcha)
    answer = models.IntegerField(_('Ответ'))

    def __str__(self):
        return f"Ответ - {str(self.answer)}"
    
    class Meta:
        verbose_name = 'reCaptcha'
        verbose_name_plural = 'reCaptcha'