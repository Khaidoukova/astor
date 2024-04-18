import random
import string

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, UpdateView, TemplateView, DetailView

from main.models import User_request, Cars, Booking
from users.forms import UserRegisterForm, UserForm, UserLoginForm
from users.models import User


class UserLoginView(LoginView):
    model = User
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'


class ProfileView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetailView(DetailView):
    model = User
    context_object_name = 'object_user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        user_requests = User_request.objects.filter(owner=user)
        context['user_requests'] = user_requests

        cars = Cars.objects.filter(owner=user)
        context['cars'] = cars

        booking = Booking.objects.filter(owner=user)
        context['bookings'] = booking

        # Проверяем, является ли текущий пользователь владельцем страницы
        is_owner = self.request.user == user
        context['is_owner'] = is_owner

        return context
