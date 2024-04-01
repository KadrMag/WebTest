from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from time import timezone
from .models import Post, Category, PostPhoto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count / 2 + count % 2
    return {'cats1': all[:half], 'cats2': all[half:]}


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # newPost = Post.objects.get(pk=1)
    context = {"posts": posts}  # , 'newPost': newPost
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def post(request, title=None):
    post = get_object_or_404(Post, title=title)
    imgs = PostPhoto.objects.filter(post=post)
    context = {"post": post, "imgs": imgs}
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


def about(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/about.html', context)


def contact(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/contact.html', context)


def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    context = {"post": post}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def search(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/search.html', context)


def create(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/create.html', context)
