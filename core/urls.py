from django.urls import path

from core import views

articles = 'articles'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('clinics/', views.ClinicsView.as_view(), name='clinics'),
    path('clinics/<slug:slug>/', views.ClinicDetailView.as_view(), name='clinic-detail'),
    
    path('faq/', views.FAQView.as_view(), name='faq'),
    
    path(f'{articles}/', views.ArticlesView.as_view(), name='articles'),
    path(f'{articles}/treatment/', views.TreatmentArticlesView.as_view(), name='treatment'),
    path(f'{articles}/motivation/', views.MotivationArticlesView.as_view(), name='motivation'),
    path(f'{articles}/clinic/', views.ClinicArticlesView.as_view(), name='clinic_articles'),
    path(f'{articles}/general/', views.GeneralArticlesView.as_view(), name='general'),
]