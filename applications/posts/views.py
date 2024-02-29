from django.shortcuts import render

def posts(request):
    return render(request, 'views/posts.html')
