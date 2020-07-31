from django.urls import path, include
from . import views

from .apiviews import *
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()

router.register('categorie', CategorieViewset)
router.register('article', ArticleViewset)
router.register('Tag', TagViewset)
router.register('Commentaire', CommentaireViewset)

app_name = 'blog'

urlpatterns = [
    path('fashion/', views.fashion, name='fashion'),
    path('single/<int:pk>', views.single, name='single'),
    path('monapi/', views.monapi, name='monapi'),
    path('api/', include('blog.apiurls')),
   
]
