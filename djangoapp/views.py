from django.shortcuts import render
from djangoapp.models import Posts
# Create your views here.
def index(request):
    contents=Posts.objects.all
    
    posts={
        'posts':contents
    }
    return render(request, 'djangoapp/index.html',posts)

def detail(request,pk):
    content=Posts.objects.get(pk=pk)
    
    post={
        'post':content
    }
    return render(request,'djangoapp/detail.html',post)

def base(request):
    return render(request,"djangoapp/base.html")

def gallery(request):
    return render(request,"djangoapp/gallery.html")

def contact(request):
    return render(request,'djangoapp/contact.html')