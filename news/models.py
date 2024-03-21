from django.db import models

NULLABLE = {'blank': True, 'null': True}


class News(models.Model):
    """Модель новости"""
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='news_pics/', verbose_name='изображение', **NULLABLE)
    date = models.DateField(auto_now=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.title}, дата публикации {self.date}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
