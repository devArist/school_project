from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('form-process', views.form_process, name='form-process')
]
