from django.contrib import admin
from . import models
from django.utils.html import format_html
#Register your models here.
@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'description']

    # def display_image(self, obj):
    #     return mark_safe(f'<img src={obj.image.url} width=80px height=80px>')
    
    # display_image.short_description = 'image'


@admin.register(models.Tips)
class TipsAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'season',]

    def display_image(self, obj):
        return format_html('<img src={} style="width:100px height:80px">'.format(obj.image.url))
    
    display_image.short_description = 'image'


# @admin.register(models.Testimonial)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ['display_image', 'name', 'job']

#     def display_image(self, obj):
#         return format_html('<img src={} width=100px height=80px>'.format(obj.image.url))
    
    
    display_image.short_description = 'image'


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'subtitle']

    def display_image(self, obj):
        return format_html('<img src={} width=100px height=80px>'.format(obj.image.url))
    
    display_image.short_description = 'image'