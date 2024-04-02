from django.db import models
from django.utils import timezone

from django.conf import settings
from pytils.translit import slugify


class Announcement(models.Model):
    """Модель объявлений, подаваемых арендаторами"""
    title = models.CharField(max_length=200, verbose_name='Заголовок объявления (будет видим на главной странице)')
    body = models.TextField(verbose_name='Текст объявления', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    image = models.ImageField(upload_to='announcements', verbose_name='Изображение', null=True, blank=True)
    stop_date = models.DateField(verbose_name='Дата окончания показа объявления',
                                 default=timezone.now() + timezone.timedelta(days=30))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              verbose_name='арендатор',
                              null=True, blank=True)
    slug = models.CharField(max_length=100, verbose_name='slug', null=True, blank=True)




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
