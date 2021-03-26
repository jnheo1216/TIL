from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews':reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviews = form.save(commit=False)
            reviews.user_id = request.user
            reviews.save()
            return redirect('community:index')
    else:
        form = ReviewForm()

    context = {
        'form':form,
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm()
    context = {
        'comment_form': comment_form,
        'review': review,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def comments_create(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review_id = review
            comment.user_id = request.user
            comment.save()
            return redirect('community:detail', review_pk)

        context = {
            'comment_form': comment_form,
            'review': review,
        }
        return render(request, 'community/detail.html', context)

    return redirect('accounts:login')