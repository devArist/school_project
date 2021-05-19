from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blogs'),
    path('detail', views.detail, name='detail'),
]