from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def PostList(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        user = request.user
        post_title =  request.POST.get('title')
        post_content =  request.POST.get('content')
        slug = post_title.replace(" ", "-")

        post = Post(title=post_title, slug=slug, author=user, content=post_content, status=1)
        post.save()
        return render(request, 'hub.html', {'saved':1, 'posts':posts})
    else:
        return render(request, 'hub.html', {'posts':posts})

def PostDetail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        content = form.cleaned_data.get("content")
        post_parent = post
        author = request.user
        comment = Comment(post=post_parent, content=content, author=author)
        comment.save()
        return render(request, 'post_detail.html', {'post':post, 'comments':comments, 'form':form})

    else:
        return render(request, 'post_detail.html', {'post':post, 'comments':comments, 'form':form})