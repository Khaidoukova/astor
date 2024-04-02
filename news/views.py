from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

import news
from news.models import News
from pytils.translit import slugify
from telegram import Bot
from users.models import User


class NewsCreateView(CreateView):
    """Контроллер создания новости"""
    model = News
    fields = ('title', 'body', 'preview', )
    success_url = reverse_lazy('news:list')

    def form_valid(self, form):
        """ Добавляем слаг для формирования удобной ссылки на новость"""
        if form.is_valid():
            self.object = form.save()
            self.object.slug = slugify(self.object.title) # создание уникального slug идентификатора новости
            self.object.save()

            # Отправка сообщения в телеграм
            bot = Bot(token=settings.TOKEN)
            users = User.objects.filter(receive_notifications_email=True)

            for user in users:
                if user.get_updates:
                    send_mail(
                        subject=f"ДЦ Астор: {self.object.title}",
                        message = f"{self.object.body}",
                        from_email = settings.EMAIL_HOST_USER,
                        recipient_list = [user.email]
                    )


        return super().form_valid(form)


class NewsListView(ListView):
    """Контроллер просмотра списка новостей"""
    model = News


class NewsUpdateView(UpdateView):
    """Контроллер изменения отдельной новости"""
    model = News
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('news:list')

    def form_valid(self, form):
        """ Корректируем слаг для формирования удобной ссылки на новость"""
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.slug = slugify(self.object.title)  # Автоматическое обновление slug
            self.object.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('news:view', kwargs={'slug': self.object.slug})


class NewsDetailView(DetailView):
    """Контроллер просмотра отдельной новости"""
    model = News


class NewsDeleteView(DeleteView):
    """Контроллер удаления отдельной новости"""
    model = News
    success_url = reverse_lazy('news:list')


