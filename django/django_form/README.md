# 장고의 form


## 정의
```python
# 앱이름/forms.py
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
# # 실제 모델과 관련없는 것도 작성이 가능
#     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect)
## 얘는 우리가 작성한 모델과 연관이 없을 수 있음!!

#################################################

## 얘는 모델과 연관 있음
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title', 'content')

```

## 사용

### views.py
```python
def create(request):
    if request.method == 'POST':  # create
        form = ArticleForm(request.POST)
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
```

### templates
```html
{% extends 'base.html' %}

{% block content %}
    <h2>New article</h2>

    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button>제출</button>
    </form>
    
{% endblock  %}
```


## create, update 개선
```python
def update(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # modelform클래스로 인스턴스 생성
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        # 위의 article을 인스턴스로 form에 넣음
        form = ArticleForm(instance=article)  # create와의 차이점
    # create도 이런 식으로 안정적으로 개선할 수 있음!!!
    # 탬플릿을 밑에서 랜더
    # 유효성 검사를 통과하지 못한 경우도 포함
    context = {
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```