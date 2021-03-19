from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods


# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)  # 에러날땐 404페이지를 띄워라
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# new랑 create 합체
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':  # create
        form = ArticleForm(request.POST, request.FILES)  # media를 위해 내용 추가
        if form.is_valid:
            article = form.save()  # form.save()는 반환값이 있다.
            return redirect('articles:index')
        return redirect('articles:create')

    else:  # new
        form = ArticleForm()
        context = {
            'form': form,
        }

        return render(request, 'articles/new.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # modelform클래스로 인스턴스 생성
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        # 위의 article을 인스턴스로 form에 넣음
        form = ArticleForm(instance=article)  # create와의 차이점
    # create도 이런 식으로 안정적으로 개선할 수 있음!!!
    context = {
        'form': form,
    }
    return render(request, 'articles/edit.html', context)


def delete(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', pk)