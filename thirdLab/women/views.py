from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [
    {'title': "About", 'url_name': 'about'},
    {'title': "Add article", 'url_name': 'add_page'},
    {'title': "Feedback", 'url_name': 'contact'},
    {'title': "Log In", 'url_name': 'login'}
]


def index(request):
    posts = Women.objects.all()

    send_parameters = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context=send_parameters)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Add article exception')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Add article'})


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Authorization")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found :(</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    send_parameters = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=send_parameters)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    send_parameters = {
        'posts': posts,
        'menu': menu,
        'title': 'Display by category',
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=send_parameters)
