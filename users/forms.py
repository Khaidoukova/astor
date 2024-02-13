from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.crypto import get_random_string
from main.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "name", "office_number", "company", "phone", "password1", "password2"]

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
