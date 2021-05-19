from django.db import models

# Create your models here.
class Service(models.Model):
    image = models.FileField(upload_to='img', blank=True, null=True)
    icon = models.CharField(verbose_name='icône', max_length=50, null=True, blank=True)
    title = models.CharField(verbose_name='titre', max_length=200)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'service'

    def __str__(self):
        return self.title


class Tips(models.Model):
    CHOICES = (
        ('Fall', 'Fall'),
        ('Winter', 'Winter'),
        ('Summer', 'Summer'),
        ('Spring', 'Spring'),
    )
    image = models.FileField(upload_to='img', blank=True, null=True)
    season = models.CharField(
        verbose_name='saison', 
        max_length=200, 
        choices=CHOICES
        )
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Conseil d'entretien saisonnier"
        verbose_name_plural = "Conseil d'entretiens saisonnier"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.FileField(upload_to='img', blank=True, null=True)
    name = models.CharField(verbose_name='nom', max_length=200)
    job = models.CharField(verbose_name='job', max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'témoignage'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.FileField(upload_to='img', blank=True, null=True)
    title = models.CharField(verbose_name='titre', max_length=200)
    subtitle = models.CharField(verbose_name='sous-titre', max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'gallerie'

    def __str__(self):
        return self.name