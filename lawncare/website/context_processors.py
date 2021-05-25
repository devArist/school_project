from . import models as website_models
from blog import models as blog_models
from service import models as service_models

def data(request):
    global_banner = website_models.GlobalBanner.objects.filter(status=True).first()
    information = website_models.Website.objects.filter(status=True).first()
    recent_blogs = blog_models.Blog.objects.filter(status=True).order_by('-date_add')[:3]
    services = service_models.Service.objects.filter(status=True)
    tips = service_models.Tips.objects.filter(status=True)
    testimonials = service_models.Testimonial.objects.filter(status=True)
    about = website_models.About.objects.filter(status=True).first()

    return locals()