from django.shortcuts import redirect, render
from django.http import HttpResponse
from blog.models import BlogPost 

# Create your views here.


def home(request):
    return render(request,"home.html")

def post_page(request,post_id):
    print(post_id)
    post=BlogPost.objects.get(pk=post_id)
    return render(request,"post.html",{"selected_post":post})

def all_posts(request):
    all_posts=BlogPost.objects.all()
    return render(request,"allposts.html",{"posts":all_posts})

def create_post(request):
    if request.method=="POST":
        title=request.POST["title"]
        content=request.POST["content"]
        new_post=BlogPost.objects.create(title=title, content=content)
        return redirect("/allposts/")
    return render(request,"create_post.html")

def delete_post(request,post_id):
    post=BlogPost.objects.get(pk=post_id)
    post.delete()
    return redirect("/allposts/")

def edit_post(request,post_id):
    post=BlogPost.objects.get(pk=post_id)
    if request.method=="POST":
        title=request.POST["title"]
        content=request.POST["content"]
        post.title=title
        post.content=content
        post.save()
        return redirect(f"/post/{post.id}/")


    return render(request,"edit_post.html",{"post":post})
















