from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

posts = [
    {
        'author':'Matthew Franson',
        'title': 'Blog Post 1',
        'content': 'First post about Smudge',
        'date_posted':'October 16, 2018'
    },
    {
        'author':'Smudge Franson',
        'title': 'Blog Post 2',
        'content': 'Smudge discusses her sleep schedule',
        'date_posted':'October 17, 2018'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)  # render takes the first request object as its first argument the second argument is the template name we want to render.

class PostListView(ListView):
    model = Post 


def about(request):
     return render(request, 'blog/about.html', {'title':'About'})
