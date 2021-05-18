from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/index.html')

def service(request):
    return render(request, 'service/services.html')

def about(request):
    return render(request, 'website/about.html')

def gallery(request):
    return render(request, 'service/gallery.html')

def contact(request):
    return render(request, 'website/contact.html')