from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요',
            }
        )
    )
    movie_title = forms.CharField(
        label='영화 제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '영화의 제목을 입력하세요',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력하세요',
            }
        )
    )
    rank = forms.IntegerField(
        label='당신의 점수',
    )
    class Meta:
        model = Review
        fields = ('title', 'movie_title', 'content', 'rank')
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)