from django.urls import path

from . import views


urlpatterns = [
    path('', views.ClinicsView.as_view(), name='clinics'),
    path('detail/<slug:slug>/', views.ClinicDetailView.as_view(), name='clinic-detail'),
]