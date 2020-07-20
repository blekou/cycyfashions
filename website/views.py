from .models import Presentation,Slider
from blog.models import Article
from django.shortcuts  import render



# Create your views here.

def home(request):
    popular = Article.objects.order_by("nombre_de_vue")[:1]
    Trending = Article.objects.order_by("-id")[:2]
    Slider  = Article.objects.filter()[:1]
    Latest =  Article.objects.order_by("-id")[:4]
    grid_box =  Article.objects.filter()[:6]
    Reviews  =  Article.objects.filter()[:6]
    datas = {
        'popular':popular,
        'Trending':Trending,
        'Slider':Slider,
        'Latest':Latest,
        'grid_box':grid_box,
        'Reviews':Reviews,
    }
    return render(request, 'index.html', datas)

def contact(request):
    datas = {

    }
    return render(request, 'contact.html', datas)



