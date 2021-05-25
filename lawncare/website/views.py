from django.shortcuts import render
from . import models
from service import models as service_models

# Create your views here.
def home(request):
    banner = models.Banner.objects.get(status=True)
    three_services = service_models.Service.objects.filter(status=True)[:3]
    return render(request, 'website/index.html', locals())

def service(request):
    return render(request, 'service/services.html')

def about(request):
    return render(request, 'website/about.html')

def gallery(request):
    galleries = service_models.Gallery.objects.filter(status=True)
    return render(request, 'service/gallery.html', locals())

def contact(request):
    return render(request, 'website/contact.html')