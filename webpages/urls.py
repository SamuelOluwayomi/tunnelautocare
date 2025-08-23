from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from webpages.views import google_verify

urlpatterns = [
    path('', views.home, name="home"),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact_view, name="contact"),
    path('services/', views.services_page, name='services'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('googlee434423ea7ef14a0.html', google_verify),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)