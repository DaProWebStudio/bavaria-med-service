from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

from core.services.translit import translit_slug


def upload_to_img(instance, filename):
    list_file = filename.split('.')
    return f'services/{translit_slug(instance.title)}.{list_file[-1]}'


class Service(models.Model):
    title = models.CharField(_('Название'), max_length=255)
    slug = models.SlugField(null=True, blank=True)
    descriptions = RichTextUploadingField(_('Описание'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = translit_slug(self.title)
        super(Service, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

        
class ClinicService(models.Model):
    clinic = models.ForeignKey('core.Clinic', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{str(self.service)} - {str(self.clinic)}"
    
    class Meta:
        verbose_name = _('Специализированная клиника')
        verbose_name_plural = _('Специализированные клиники')


class ServiceCarousel(models.Model):
    title = models.CharField(_('Название'), max_length=255)
    descriptions = models.TextField(_('Описание'))
    url = models.CharField('Ссылка на сервис', max_length=255, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)    
    
    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.title = self.service.title
        self.url = self.service.slug
        super(ServiceCarousel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Карусель')
        verbose_name_plural = _('Карусели')