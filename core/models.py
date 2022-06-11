from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill 

from core.services.translit import translit_slug


def upload_to_img_doctor(instance, filename):
    list_file = filename.split('.')
    return f'doctors/{translit_slug(instance.full_name)}.{list_file[-1]}'


class Clinic(models.Model):
    title = models.CharField(_('Название'), max_length=255)
    slug = models.SlugField(null=True, blank=True)
    descriptions = RichTextUploadingField(_('Описание'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('clinic-detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = translit_slug(self.title)
        super(Clinic, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Клиника')
        verbose_name_plural = _('Клиники')


class Doctor(models.Model):
    full_name = models.CharField(_('Ф.И.О'), max_length=50)
    slug = models.SlugField(null=True, blank=True)
    position = models.CharField(_('Должность'), max_length=155)
    description = RichTextUploadingField(_('Резюме'))
    image = ProcessedImageField(verbose_name=_('Фото'), upload_to=upload_to_img_doctor, format='webp',
                                processors=[ResizeToFill(300, 360)], options={'quality': 90})
    
    created_at = models.DateTimeField("Созданно", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.full_name)

    def save(self, *args, **kwargs):
        self.slug = translit_slug(self.full_name)
        super(Doctor, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Врач')
        verbose_name_plural = _('Врачи')