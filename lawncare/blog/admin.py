from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

# Register your models here.
@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'description', 'author']

    def display_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width=80px height=80px>')
    
    display_image.short_description = 'image'



@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'description', 'blog']
    filter_horizontal = ('tags',)

    def display_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width=80px height=80px>')
    
    display_image.short_description = 'image'


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'user', 'description']

    def display_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width=80px height=80px>')
    
    display_image.short_description = 'image'


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject','website']