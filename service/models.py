from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill 

from core.services.translit import translit_slug


def upload_to_news_img(instance, filename):
    list_file = filename.split('.')
    return f'News/{instance.news.slug[0:35]}/{translit_slug(list_file[0])}.{list_file[-1]}/'


class Service(models.Model):
    title = models.CharField(_('Название'), max_length=255)
    slug = models.SlugField(null=True, blank=True)
    descriptions = models.RichTextField(_('Описание'))
    image = ProcessedImageField(verbose_name=_('Фото'), upload_to=upload_to_main_img, format='webp',
                                processors=[ResizeToFill(756, 425)], options={'quality': 90})
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = translit_slug(self.name)
        super(News, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')