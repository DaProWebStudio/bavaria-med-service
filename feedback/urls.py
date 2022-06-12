from django.urls import path

from . import views


urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]