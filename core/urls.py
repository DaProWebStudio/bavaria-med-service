from django.urls import path

from core import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('greeting/', views.GreetingView.as_view(), name='greeting'),
]