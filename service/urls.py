from django.urls import path

from . import views


urlpatterns = [
    path('', views.ServiceView.as_view(), name='service'),
    path('diagnostics/', views.DiagnosticsView.as_view(), name='diagnostics'),
]