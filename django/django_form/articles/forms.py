from django import forms
from .models import Article


# html form tag 생성
# 유효성 검사

# class ArticleForm(forms.Form):
#     REGIONS = [
#         ('daejeon', '대전'),
#         ('seoul', '서울'),
#         ('busan', '부산'),
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect)
## 얘는 우리가 작성한 모델과 연관이 없을 수 있음!!

#################################################

## 얘는 모델과 연관 있음
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요',
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

    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title', 'content')

        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'form-control my-title',
        #         'placeholder': '제목을 입력하세요',
        #     }),
        #     'content': forms.Textarea(attrs={
        #         'class': 'form-control',
        #         'placeholder': '내용을 입력하세요',
        #     }),
        # }
    