from django.db import models

# Create your models here.
class About(models.Model):
    image = models.FileField(upload_to='img', max_length=100)
    title = models.CharField(verbose_name='titre', max_length=200)
    subtitle = models.CharField(verbose_name='sous-titre', max_length=200)
    description = models.TextField()
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'a propos'
        verbose_name_plural = 'a propos'
    
    def __str__(self):
        return self.title


class Banner(models.Model):
    image = models.FileField(upload_to='img', max_length=100)
    title = models.CharField(verbose_name='titre', max_length=200)
    subtitle = models.CharField(verbose_name='sous-titre', max_length=200)
    description = models.TextField()
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Bannière'
        verbose_name_plural = 'Bannières'
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(verbose_name='nom', max_length=200)
    email = models.EmailField(verbose_name='email', max_length=200)
    subject = models.CharField(verbose_name='sujet', max_length=200)
    message = models.TextField()
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
    
    def __str__(self):
        return self.name


class  Newsletter(models.Model):
    email = models.EmailField(max_length=200)
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
    
    def __str__(self):
        return self.email


class SocialNetwork(models.Model):
    icon = models.CharField(max_length=200)
    link = models.URLField(verbose_name="url", max_length=200)
    name = models.CharField(verbose_name='nom', max_length=200)
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'réseau social'
        verbose_name_plural = 'réseaux sociaux'
    
    def __str__(self):
        return self.name


class Website(models.Model):
    address = models.CharField(max_length=200, verbose_name='adresse')
    phone = models.CharField(verbose_name='téléphone', max_length=200)
    email = models.EmailField(verbose_name='email', max_length=200)
    website = models.URLField(verbose_name='site web', null=True)
    copyrights = models.CharField(verbose_name='copyright', max_length=200)
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Information générale'
        verbose_name_plural = 'Informations générales'
    
    def __str__(self):
        return self.phone


class GlobalBanner(models.Model):
    image = models.FileField(
        verbose_name='bannière des autres pages du site', 
        upload_to='img'
        )
    date_add = models.DateTimeField(verbose_name="date d'ajout", auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Bannière générale'
        verbose_name_plural = 'Bannière générale'
    
    def __str__(self):
        return 'bannère des autres pages du site'