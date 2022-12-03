from django.shortcuts import render,redirect
from django.views.decorators.http import (require_http_methods, require_POST, require_safe)
from .forms import MovieForm

# Create your views here.
from .models import Movie

# 전체 조회
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

# methods 제한.
# 게시글 생성, 생성페이지로 이동
@require_http_methods(['GET', 'POST'])
def create(request):
    # 게시글 생성
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            # return render(request, 'movies/detail.html', context)
            return redirect('movies:detail', movie.pk)
    # 게시글 생성페이지로 이동
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

# 게시글 상세페이지로 이동
def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

@require_http_methods(['GET', 'POST'])
# 게시글 수정, 수정페이지로 이동
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    # 게시글 수정
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    # 게시글 수정페이지로 이동
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)

# 게시글 삭제
def delete(request, pk):
    movies = Movie.objects.get(pk=pk)
    movies.delete()

    return redirect('movies:index')