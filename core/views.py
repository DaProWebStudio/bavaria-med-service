from django.shortcuts import render
from django.views.generic import View, TemplateView

from .mixins import ViewMixin


class IndexView(ViewMixin):
    title = ''
    description = ''
    template_name = 'index.html'
    
    
class GreetingView(ViewMixin):
    title = ''
    description = ''
    template_name = 'greeting.html'
    
    
class FAQView(ViewMixin):
    title = 'Лечение за рубежом в вопросах и ответах'
    description = 'Уникальная подборка вопросов и ответов о лечении в Германии, германских клиниках и медицинском туризме за рубежом.'
    template_name = 'FAQ.html'


class ContactView(ViewMixin):
    title = 'Контактная информация'
    description = '«Bavaria Med Service» — диагностика, лечение и реабилитация в лучших клиниках Германии, медицинский туризм за рубежом.'
    template_name = 'contact.html'