from django.shortcuts import render, redirect
from .models import Movie

# Read
def index(request):
    movies = Movie.objects.all()  # 모든 영화 정보 내놔
    context = {
        'movies': movies,
    }
    
    return render(request, 'movies/index.html', context)


# Create
def new(request):
    return render(request, 'movies/new.html')


def create(request):
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')  # 받아온 정보들로

    movie = Movie(title=title, overview=overview, poster_path=poster_path)  # 새로운 Movie생성
    movie.save()

    return redirect('movies:index')


# Read
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)  # 해당 pk의 글만 불러옴
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


## 여기까지
# Update
def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)  # 해당 글을 불러와서 

    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')

    movie.title = title
    movie.overview = overview
    movie.poster_path = poster_path  # 새 정보로 업데이트
    movie.save()

    return redirect('movies:detail', movie.pk)


# Delete
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)  # 해당 pk의 글을 

    if request.method == 'POST': # 포스트방식 입력이라면 삭제
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', pk)