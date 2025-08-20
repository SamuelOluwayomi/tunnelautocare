from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('contact', views.contact_page, name="contact"),
    path('services/', views.services_page, name='services'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)