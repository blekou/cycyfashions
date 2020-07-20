from django.db import models
from django.contrib.auth.models import User
import  datetime


# Create your models here.

class Categories(models.Model):
    nom = models.CharField(max_length=225, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nom


        
class Presentation(models.Model):
    image = models.ImageField(upload_to="image/slider")
    titre = models.CharField(max_length=225, null=True)
    description = models.TextField(null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Presentation"
        verbose_name_plural = "Presentation"

    def __str__(self):
        return self.titre


class Slider(models.Model):
    image = models.ImageField(upload_to="image/slider")
    titre = models.CharField(max_length=225, null=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="slider_user")
    nombre_commentaire = models.PositiveIntegerField(null=True)
    nombre_vue = models.PositiveIntegerField(null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='slider_categories', null=True)


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"

    def __str__(self):
        return self.titre



class SiteInfo(models.Model):

    image = models.ImageField(upload_to="image/slider")
    titre = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    map_url = models.TextField(null=True)
    icon = models.ImageField(upload_to = 'image/SiteInfo')
    logo = models.ImageField(upload_to='image/SiteInfo')
    description  = models.TextField()
    nom = models.CharField(max_length=225)
    email = models.EmailField(null=True)


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "site infos"
        verbose_name_plural = "site infos"

    def __str__(self):
        return self.titre


class Reseaux_sociaux(models.Model):
    
    Icone = [
        ('facebook', 'fa fa-facebok'),
        ('twitter', 'fa fa-twitter'),
        ('rss', 'fa fa-rss'),
        ('goole-plus', 'fa fa-goole-plus'),
        ('linkedin', 'fa fa-linkedin'),
        ('pinterest', 'fa fa-pinterest'),

    ]

    icone = models.CharField(choices = Icone, max_length = 225)
    nom = models.CharField(max_length=225)
    lien = models.URLField()

    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "reseaux sociaux"
        verbose_name_plural = "reseaux sociaux"

    def __str__(self):
        return self.nom

    
    
