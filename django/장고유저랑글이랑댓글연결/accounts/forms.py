from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
                }
            )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'new-password',
                }
            )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'new-password',
                }
            )
    )
    email = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label = 'id',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
                }
            )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'new-password',
                }
            )
    )
    class Meta:
        model = get_user_model()
        fields = '__all__'
