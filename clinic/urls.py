from django.urls import path

from . import views


urlpatterns = [
    path('', views.ClinicView.as_view(), name='clinics'),
]