from django.shortcuts import render

posts = [
    {
        'author': 'Sebastian',
        'title': 'My first post',
        'content': 'This is my first post',
        'date_posted': 'July 7 2020'
    },
    {
        'author': 'Andrei',
        'title': 'My first post',
        'content': 'This is my first post',
        'date_posted': 'July 10 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
