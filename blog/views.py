from django.shortcuts import render

posts = [
    {
        'author': 'PooyaS',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted':'Augost 28, 2018'

    },
        {
        'author': 'John D',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted':'Augost 29, 2018'
    }
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')