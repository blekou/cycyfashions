from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Categorie(models.Model):
    nom = models.CharField(max_length=225, null=True)
    


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.nom


class Tag(models.Model):
    
    nom = models.CharField(max_length=225, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tag"

    def __str__(self):
        return self.nom


class Article(models.Model):
    
    image = models.ImageField(upload_to="image/slider", null=True)
    titre = models.CharField(max_length=225, null=True)
    description = models.TextField(null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="categories", null=True)
    tag = models.ManyToManyField(Tag, related_name="categories")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_article', null=True)
    nombre_de_vue = models.PositiveIntegerField(null=True)
  

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("single", kwargs={"pk": self.pk})


class Commentaire(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_commentaire', null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=225, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return self.user.username

