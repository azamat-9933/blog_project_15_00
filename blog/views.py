from django.shortcuts import render

# Create your views here.
from blog.models import *


def index_view(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    context = {
        "categories": categories,
        "posts": posts
    }

    return render(request, "index.html", context)


def about_us_view(request):
    return render(request, "about_us.html")

def our_team_view(request):
    return render(request, "our_team.html")

def contacts_view(request):
    return render(request, "contacts.html")

def services_view(request):
    return render(request, "services.html")


def category_view(request, slug):
    category = Category.objects.get(slug=slug)  # 1 объект по условию указанному
    posts = Post.objects.filter(category=category)  # все объекты по условию указанному
    categories = Category.objects.all()  # все категории которые есть

    context = {
        'category': category,
        'categories': categories,
        'posts': posts
    }

    return render(request, "category.html", context)


def search_view(request):
    word = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=word)
    categories = Category.objects.all()

    context = {
        'word': word,
        'posts': posts,
        'categories': categories
    }

    return render(request, "search.html", context)









