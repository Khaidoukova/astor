from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from pytils.translit import slugify

from announcements.forms import AnnouncementForm
from announcements.models import Announcement


class AnnouncementsCreateView(CreateView):
    """Контроллер создания объявления"""
    model = Announcement
    form_class = AnnouncementForm

    def form_valid(self, form):
        """ Добавляем слаг для формирования удобной ссылки на объявление"""
        if form.is_valid():
            self.object = form.save()
            self.object.slug = slugify(self.object.title) # создание уникального slug идентификатора новости
            self.object.owner = self.request.user
            self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('announcements:view', kwargs={'slug': self.object.slug})


class AnnouncementsListView(ListView):
    """Контроллер просмотра списка новостей"""
    model = Announcement
    ordering = ['-created_at']


class AnnouncementsUpdateView(UpdateView):
    """Контроллер изменения отдельной новости"""
    model = Announcement
    fields = ('title', 'body', 'image', 'is_active', 'stop_date')
    success_url = reverse_lazy('announcements:view')

    def form_valid(self, form):
        """ Корректируем слаг для формирования удобной ссылки на новость"""
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.slug = slugify(self.object.title)  # Автоматическое обновление slug
            self.object.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('news:view', kwargs={'slug': self.object.slug})


class AnnouncementsDetailView(DetailView):
    """Контроллер просмотра отдельной новости"""
    model = Announcement


class AnnouncementsDeleteView(DeleteView):
    """Контроллер удаления отдельной новости"""
    model = Announcement
    success_url = reverse_lazy('main:index')



