from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

from cloudinary.forms import cl_init_js_callbacks

def index(request):
    # photos = Photo.objects.all()
    # ctx = {'photos':photos}
    # return render(request, '/', ctx)
    #if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #if the form is valid
        if form.is_valid():
            #Yes, Save
            form.save()
            #Redirect to Home
            return HttpResponseRedirect('/')

            #No, Show Error
        else:
            return HttpResponseRedirect(form.error.as_json())



    #Get all posts limit = 20
    posts = Post.objects.all()[:20]

    #Show
    return render(request, 'posts.html',
                  {'posts': posts})

def delete(request, post_id):
    #Find post
    post = Post.objects.get(id= post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        form = PostForm(instance=post)

    else:
        form = PostForm(instance=post, data=request.POST, files=request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('/', post_id=post.id)


    context = {'post': post, 'index': index, 'form': form}
    return render(request, 'edit.html', context)


def likebtn(request,post_id):
    like = Post.objects.get(id= post_id)
    like.likes += 1
    # for i in range (10):
    #     if i%2 == 1:
    #         like.likes += 1
    #     else:
    #         like.likes -= 1
    like.save()
    return HttpResponseRedirect('/')


