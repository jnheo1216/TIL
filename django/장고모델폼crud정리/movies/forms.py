from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'제목을 쓰세요',
            }
        )
    )
    overview = forms.CharField(
        label = '줄거리',
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder':'줄거리를 쓰세요',
            }
        )
    )
    poster_path = forms.CharField(
        label = 'URL',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'URL 쓰세요',
            }
        )
    )
    class Meta:
        model = Movie
        fields = '__all__'