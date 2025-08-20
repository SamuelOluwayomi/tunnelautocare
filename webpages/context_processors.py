from .models import Service

def services_dropdown(request):
    services = Service.objects.all().order_by('title')[:6]
    return {'services_nav': services}