from django.urls import path

from core import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]