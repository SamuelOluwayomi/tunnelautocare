from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from django.contrib import messages
from .forms import ContactForm
from django.http import FileResponse
import os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, "webpages/home.html", {})

def services(request):
    return render(request,"webpages/services.html", {})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'webpages/service_detail.html', {'service': service})

def services_page(request):
    services = Service.objects.all()
    return render(request, 'webpages/services.html', {'services': services})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been received.')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error. Please check your input.')
    else:
        form = ContactForm()

    return render(request, 'webpages/contact.html', {'form': form})

def google_verify(request):
    path = os.path.join(settings.BASE_DIR, 'webpages', 'static', 'googlee434423ea7ef14a0.html')
    return FileResponse(open(path, 'rb'))