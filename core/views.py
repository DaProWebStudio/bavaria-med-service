from django.shortcuts import render
from django.views.generic import View, TemplateView

from .mixins import ViewMixin
from . import pages_info as info

class IndexView(ViewMixin):
    title = info.index_title
    description = info.index_description
    template_name = 'index.html'
    
    
class GreetingView(ViewMixin):
    title = info.greeting_title
    description = info.greeting_description
    template_name = 'greeting.html'
    
    
class FAQView(ViewMixin):
    title = info.faq_title
    description = info.faq_description
    template_name = 'FAQ.html'


class ContactView(ViewMixin):
    title = info.contact_title
    description = info.contact_description
    template_name = 'contact.html'