from django.shortcuts import render, get_object_or_404
from .models import Service

# Create your views here.
def home(request):
    return render(request, "webpages/home.html", {})

def services(request):
    return render(request,"webpages/services.html", {})

# def service_detail(request, slug):
#     services = {
#         'engine-repair': {
#             'title': 'Engine Repair',
#             'description': 'We diagnose and repair all kinds of engine issues using modern diagnostic tools and years of expertise.',
#             'image': 'webpages/images/image1.jpg'
#         },
#         'oil-change': {
#             'title': 'Oil Change',
#             'description': 'Protect your engine with our quality oil change service. We use premium lubricants to keep your vehicle running smoothly.',
#             'image': 'webpages/images/image4.jpg'
#         },
#         'brake-service': {
#             'title': 'Brake Service',
#             'description': 'We inspect, replace, and maintain brake pads, discs, and fluids for safe driving.',
#             'image': 'webpages/images/image3.jpg'
#         },
#         'wheel-alignment': {
#             'title': 'Wheel Alignment',
#             'description': 'Proper wheel alignment helps your tires last longer and improves fuel efficiency. We’ve got the tools to do it right.',
#             'image': 'webpages/images/image5.jpg'
#         },
#         'battery-replacement': {
#             'title': 'Battery Replacement',
#             'description': 'Dead battery? We provide fast and reliable battery replacement services with testing.',
#             'image': 'webpages/images/image6.jpg'
#         },
#         'ac-repair': {
#             'title': 'Car AC Repair',
#             'description': 'Stay cool. We diagnose and fix air conditioning issues to keep your ride comfortable.',
#             'image': 'webpages/images/slide2.jpg'
#         },
#     }

#     service = services.get(slug)
#     if not service:
#         return render(request, '404.html')

#     return render(request, 'webpages/service_detail.html', {'service': service})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'webpages/service_detail.html', {'service': service})

def contact_page(request):
    service_query = request.GET.get('service', '')
    return render(request, 'webpages/contact.html', {'pre_filled_service': service_query})

def services_page(request):
    services = Service.objects.all()
    return render(request, 'webpages/services.html', {'services': services})