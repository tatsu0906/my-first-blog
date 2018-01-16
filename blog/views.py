from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'blog/post_list.html', {})

def render_index(request):
    return render(request, 'blog/index.html', {})

def render_7(request):
    return render(request, 'blog/7.html', {})

def render_matrix(request):
    return render(request, 'blog/matrix.html', {})

def render_title(request):
    return render(request, 'blog/title.html', {})

def render_24(request):
    return render(request, 'blog/24.html', {})

def render_17(request):
    return render(request, 'blog/17.html', {})    

def render_coreterm(request):
    return render(request, 'blog/coreterm.html', {})    

def render_suppleterm(request):
    return render(request, 'blog/suppleterm.html', {})    

def render_board(request):
    return render(request, 'blog/board.html', {})    





#########################################################################
"""
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
"""