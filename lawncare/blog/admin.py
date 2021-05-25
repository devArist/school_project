from django.contrib import admin
from django.utils.html import format_html
from . import models

#Register your models here.
@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'display_image', 
        'title', 
        'description', 
        'author', 
        'date_add', 
        'date_update'
        ]
    list_display_links = ['title', 'title', 'description']
    list_filter = ['author', 'date_add', 'date_update']
    filter_horizontal = ['tags']

    def display_image(self, obj):
        return format_html(f'<img src={obj.image.url} width=50px height=50px>')
    
    display_image.short_description = 'image'



@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'description', 'blog']

    def display_image(self, obj):
        return format_html(f'<img src={obj.image.url} width=80px height=80px>')
    
    display_image.short_description = 'image'


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'name', 'description']

    def display_image(self, obj):
        return format_html(f'<img src={obj.image.url} width=80px height=80px>')
    
    display_image.short_description = 'image'


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject','website']