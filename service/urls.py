from django.urls import path

from . import views


urlpatterns = [
    path('', views.ServiceView.as_view(), name='service'),
    path('detail/<slug:slug>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('diagnostics/', views.DiagnosticsView.as_view(), name='diagnostics'),
    path('support/', views.SupportView.as_view(), name='support'),
]