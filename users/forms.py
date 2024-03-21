from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
from main.forms import StyleFormMixin
from users.models import User


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "name", "office_number", "company", "phone",
                  "get_updates", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        return user


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "name", "office_number", "company", "phone"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    """Форма для контроля авторизации пользователей с подтвержденным почтовым адресом"""

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)  # аутентификация пользователя по email

            if user and not user.is_active:
                raise ValidationError('Вам нужно подтвердить свой почтовый адрес, прежде чем войти.')

        return super().clean()
