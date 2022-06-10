from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill 

from core.services.translit import translit_slug


def upload_to_img(instance, filename):
    list_file = filename.split('.')
    return f'clinics/{translit_slug(instance.title)}.{list_file[-1]}'


class Clinic(models.Model):
    title = models.CharField(_('Название'), max_length=255)
    slug = models.SlugField(null=True, blank=True)
    descriptions = RichTextUploadingField(_('Описание'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = translit_slug(self.title)
        super(Clinic, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Клиника')
        verbose_name_plural = _('Клиники')