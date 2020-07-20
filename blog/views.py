from django.shortcuts import render, redirect
from .models import Article
from .forms import CommentaireForm

# Create your views here.

def fashion(request):
    grid_box = Article.objects.all().order_by('-id')[:1]
    article_box = Article.objects.filter()[:7]
    posts = Article.objects.filter()[:1]
   
    datas = {
        'grid_box':grid_box,
        'article_box':article_box,
        'posts':posts,
    }
    return render(request, 'fashion-category.html', datas)



def single(request,pk):
    post = Article.objects.all().order_by('-id')[:1]


    if request.method =="POST":
        form = CommentaireForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()

            return redirect('single', pk = post.pk)

    else:
        form = CommentaireForm()



    datas = {
        'post':post,
        'form':form,
    }
    return render(request, 'single-post.html', datas)
    