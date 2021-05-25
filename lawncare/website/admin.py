from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'subtitle', 'description', 'status']
    list_filter = ['title', 'subtitle', 'description']
    list_display_links =  ['title', 'subtitle', 'description']

    def display_image(self, obj):
        return format_html(
            f'<img src={obj.image.url} width=100px height=80px>'
        )
    
    display_image.short_description = 'image'


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'subtitle', 'description', 'status']
    list_filter = ['title', 'subtitle', 'description']
    list_display_links =  ['display_image', 'title', 'subtitle', 'description']

    def display_image(self, obj):
        return format_html(
            f'<img src={obj.image.url} width=100px height=80px>'
        )
    
    display_image.short_description = 'image'

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'date_add']
    list_filter = ['email', 'date_add', 'name',]
    readonly_fields = ['name', 'email', 'subject', 'message', 'status']


@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email']
    readonly_fields = ['email', 'status']


@admin.register(models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['icon', 'link', 'name', 'status']


@admin.register(models.GlobalBanner)
class GlobalBannerAdmin(admin.ModelAdmin):
    list_display = ['display_image']

    def display_image(self, obj):
        return format_html(
            f'<img src={obj.image.url} width=100px height=80px>'
        )
    
    display_image.short_description = 'image'


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email', 'website', 'copyrights', 'status']
