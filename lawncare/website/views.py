from django.shortcuts import render
from . import models
from service import models as service_models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.validators import validate_email
import re

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

@csrf_exempt
def form_process(request):
    success = False
    messages = ""
    if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            if name == '' or email == '' or subject == '' or message == '':
                message = 'Veuillez remplir les champs vides'
            elif name.isspace() or not re.fullmatch("[A-Za-zäöëüï'éè ]+", name):
                message = 'Veuillez saisir un nom valide'
            elif not re.fullmatch('(\w\.?)+@(\w\.?)+\.[a-z]{2,3}', email):
                message = 'Veuillez saisir un email valide'
            else:
                contact = models.Contact(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message,
                    )
                contact.save()
                messages = 'Votre message a bien été envoyé.'
                success = True


    
    datas = {
        'success': success,
        'message': messages
    }

    return JsonResponse(datas, safe=False)