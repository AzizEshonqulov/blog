from multiprocessing import context
from django.shortcuts import redirect, render
from pers_blog.forms import PostCreateForm, CommentCreateForm
from pers_blog.models import Category, Post
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home_page(request):
    data = Post.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context=context)



def post(request):
    data = Post.objects.all()
    categorys = Category.objects.all()
    context = {'data': data, 'category':categorys}
    return render(request, 'blog.html', context=context)



def post_detail(request, pk):
    data = Post.objects.get(id=pk)
    categorys = Category.objects.all()
    comment = data.comments.all()
    comment_count = comment.count()
    context = {'post': data, 'comment': comment, 'comment_count': comment_count, 'category':categorys}
    return render(request, 'single-blog.html', context)



def category(request, pk):
    category = Post.objects.filter(category__id=pk)
    context = {'category':category}
    return render(request, 'category.html', context)
    



def post_new(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Muvaffaqiyatli qo'shildi")
            return redirect('post_detail', post.id)
        else:
            messages.warning(request, form.errors)
            print(form.errors)
    form = PostCreateForm()
    context = {'form': form}
    print(request.POST)
    return render(request, 'post_new.html', context)


def comment_new(request):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('post_detail', comment.post.id)
        else:
            print(form.errors)
    form = CommentCreateForm()
    context = {'form': form}
    print(request.POST)
    return render(request, 'single-blog.html', context)

    

def post_update(request, pk):
    post = Post.objects.get(id=pk)
    form = PostCreateForm(instance=post)
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Muvaffaqiyatli o'zgartirildi!")
            return redirect('post_detail', post.id)
        else:
            messages.warning(request, form.errors)
            print(form.errors)
    context = {'form': form}
    return render(request, 'post_new.html', context)



def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    messages.error(request, 'Maqola o\'chirildi')
    return redirect('home')


def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registratsiyadan o\'tdingiz')
            return redirect(home_page)
        else:
            messages.error(request, form.errors)
            print(form.errors)
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'register.html', context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username</div>')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Username or password if incorrect')
            return redirect('login')
    return render(request, 'login.html')        


def logoutPage(request):
    logout(request)
    return redirect('login')