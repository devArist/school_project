from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
    image = models.FileField( upload_to='img',)
    title = models.CharField(verbose_name='titre', max_length=200)
    description = models.TextField()
    author = models.ForeignKey(
        "Author", 
        verbose_name='auteur', 
        on_delete=models.CASCADE,
        related_name='author_blogs'
        )
    paragraph = models.TextField(verbose_name='paragraphe')
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Post(models.Model):
    image = models.FileField( upload_to='img',)
    title = models.CharField(verbose_name='titre', max_length=200)
    description = models.TextField()
    blog = models.ForeignKey(
        "Blog", 
        verbose_name="blog", 
        on_delete=models.CASCADE,
        related_name='blog_articles'
        )
    tags = models.ManyToManyField("Tag", verbose_name='tags')
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Tag(models.Model):
    name = models.CharField(verbose_name='nom', max_length=200)
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'tag'

    def __str__(self):
        return self.name



class Author(models.Model):
    image = models.FileField(upload_to=None, max_length=100)
    user = models.OneToOneField(
        get_user_model(), 
        verbose_name=("utilisateur"), 
        on_delete=models.CASCADE
        )
    description = models.TextField()
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'auteur'
    
    def __str__(self):
        return self.user.username


class Comment(models.Model):
    name = models.CharField(verbose_name='nom', max_length=200)
    email = models.EmailField(max_length=200)
    website = models.URLField(
        verbose_name='site web', 
        max_length=200, 
        blank=True, 
        null=True
        )
    subject = models.TextField(null=True)
    blog = models.ForeignKey(
        "Blog", 
        verbose_name='blog', 
        on_delete=models.CASCADE,
        related_name='blog_comments'
        )
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'commentaire'
    
    def __str__(self):
        return self.name