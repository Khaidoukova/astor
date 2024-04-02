from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView, TemplateView)

from announcements.models import Announcement
from news.models import News
from .forms import CompanyForm, OfficeForm, User_requestForm, BookingForm, CarsForm
from .models import Company, Office, User_request, Booking, Cars


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        send_mail(
            name,
            message,
            phone_number,
            ['olga@noran.ru'],

        )
    context = {
        'title': 'Контакты',
    }

    return render(request, 'main/contacts.html', context)


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcements'] = Announcement.objects.all().order_by('-created_at')
        context['news'] = News.objects.all()

        return context


class CompanyListView(ListView):
    model = Company

    def get_queryset(self):
        companies = Company.objects.all()
        return companies


class CompanyDetailView(DetailView):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('main:index')


class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('main:index')

    def test_func(self):
        user = self.request.user

        if user.is_staff or user.is_superuser or user.is_manager:
            return True
        else:
            return False


class CompanyDeleteView(LoginRequiredMixin,
                        DeleteView):
    model = Company
    success_url = reverse_lazy('main:index')


class OfficeListView(ListView):
    model = Office


class OfficeDetailView(DetailView):
    model = Office


class OfficeCreateView(CreateView):
    model = Office
    form_class = OfficeForm
    success_url = reverse_lazy('main:index')


class OfficeUpdateView(LoginRequiredMixin,
                       UserPassesTestMixin,
                       UpdateView):
    model = Office
    form_class = OfficeForm
    success_url = reverse_lazy('main:index')

    def test_func(self):
        user = self.request.user

        if user.is_staff or user.is_superuser or user.is_manager:
            return True
        else:
            return False


class OfficeDeleteView(LoginRequiredMixin,
                       PermissionRequiredMixin,
                       DeleteView):
    model = Office
    success_url = reverse_lazy('main:index')


class User_requestListView(ListView):
    model = User_request
    template_name = 'main/user_request_list.html'
    context_object_name = 'user_requests'


class User_requestDetailView(DetailView):
    model = User_request


class User_requestCreateView(CreateView):
    model = User_request
    form_class = User_requestForm
    success_url = reverse_lazy('main:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'owner': self.request.user}
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super().form_valid(form)


class User_requestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User_request
    form_class = User_requestForm
    success_url = reverse_lazy('main:index')

    def test_func(self):
        user = self.request.user

        if user.is_staff or user.is_superuser or user.is_manager:
            return True
        else:
            return False

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class User_requestDeleteView(LoginRequiredMixin,
                             PermissionRequiredMixin,
                             DeleteView):
    model = User_request
    success_url = reverse_lazy('main:index')
    # permission_required = 'main.delete_testcategory'


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class CarsListView(ListView):
    model = Cars


class CarsDetailView(DetailView):
    model = Cars


class CarsCreateView(CreateView):
    model = Cars
    template_name = 'main/car_form.html'
    form_class = CarsForm
    success_url = reverse_lazy('main:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class CarsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cars
    form_class = CarsForm
    success_url = reverse_lazy('main:index')

    def test_func(self):
        user = self.request.user

        if user.is_staff or user.is_superuser or user.is_manager:
            return True
        else:
            return False


class CarsDeleteView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     DeleteView):
    model = Cars
    success_url = reverse_lazy('main:index')
    permission_required = 'main.delete_testcategory'
