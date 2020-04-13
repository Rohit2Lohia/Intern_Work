import requests
from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from .models import Article
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.forms import ModelForm
from django.urls import reverse

requests.packages.urllib3.disable_warnings()


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    # query= request.GET.get("q")
    # if query:
    #     articles = articles.filter(title__icontains=query)
    return render(request, 'articles/articles_list.html', {'articles': articles})

def article_search(request):
    articles = Article.objects.all().order_by('date')
    query= request.GET.get("q")
    if query:
        articles = articles.filter(title__icontains=query)
    return render(request, 'articles/articles_list.html', {'articles': articles})

def article_list_ascend(request):
    articles = Article.objects.all().order_by('title')
    return render(request, 'articles/articles_list.html', {'articles': articles})

def article_list_user(request, user):
    art = Article.objects.all().order_by('author')
    articles=[]
    for x in art:
        # print(x.author," ",request.user)
        if( x.author == request.user ):
            # print("In if")
            articles.append(x)
    # print(articles)
    return render(request, 'articles/articles_list.html', {'articles': articles})

def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})

@login_required(login_url="/accounts/login/")
def article_edit(request, slug):
    if request.user.is_superuser:
        # movie = get_object_or_404(Article, pk=pk)
        movie = Article.objects.get(slug=slug)
    else:
        # movie = get_list_or_404( Article, pk=pk, user=request.user)
        movie = Article.objects.get(slug=slug)
    form = forms.CreateArticle(request.POST or None, instance=movie )
    if form.is_valid():
        instance=form.save(commit=False)
        instance.author=request.user
        instance.save()
        return redirect('articles:list')
    movie.delete()
    return render(request, 'articles/article_create.html', {'form':form})

@login_required(login_url="/accounts/login/")
def article_delete(request, slug):
    del_movie = Article.objects.get(slug=slug)
    del_movie.delete()

    return HttpResponseRedirect(reverse('articles:list'))
