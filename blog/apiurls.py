from django.urls import path
from . import views

from .apiviews import *
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()

router.register('categorie', CategorieViewset)
router.register('article', ArticleViewset)
router.register('Tag', TagViewset)
router.register('Commentaire', CommentaireViewset)


urlpatterns = [
       
]

urlpatterns+= router.urls