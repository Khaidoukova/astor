from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from users.models import User


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='название категории')
    description = models.TextField(verbose_name='описание')
    logo = models.ImageField(upload_to='logos/',
                             verbose_name='логотип', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Office(models.Model):
    office_id = models.CharField(max_length=100, verbose_name='помещение', unique=True)
    floor = models.IntegerField(verbose_name='этаж')
    sq_m = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='площадь')
    image1 = models.ImageField(upload_to='offices/', verbose_name='фото', null=True, blank=True)
    image2 = models.ImageField(upload_to='offices/',
                               verbose_name='фото', null=True, blank=True)
    image3 = models.ImageField(upload_to='offices/',
                               verbose_name='фото', null=True, blank=True)
    description = models.TextField(verbose_name='описание',
                                   null=True, blank=True)
    price = models.IntegerField(verbose_name='цена',
                                null=True, blank=True)

    def __str__(self):
        return f'{self.office_id}'

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'
        ordering = ('office_id',)


class User_request(models.Model):
    URGENT = 'срочно'
    NOT_URGENT = 'в текущем режиме'
    URGENCY = (
        (URGENT, 'срочно'),
        (NOT_URGENT, 'в текущем режиме')
    )

    DONE = 'выполнено'
    IN_PROGRESS = 'в работе'
    CLOSED = 'завершено'
    STATUS = ((DONE, 'выполнено'), (IN_PROGRESS, 'в работе'), (CLOSED, 'завершено'))

    date = models.DateTimeField(default=timezone.now, verbose_name='дата и время заявки')
    office_id = models.CharField(max_length=100, verbose_name='помещение')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='отправитель')
    description = models.TextField(verbose_name='описание')
    urgency = models.CharField(max_length=20, choices=URGENCY,
                               default=NOT_URGENT, verbose_name='срочность')
    status = models.CharField(max_length=20, choices=STATUS,
                              default=IN_PROGRESS, verbose_name='статус')
    comments = models.TextField(verbose_name='комментарий', blank=True, null=True)
    feedback = models.TextField(verbose_name='комментарий отправителя заявки', blank=True, null=True)
    date_completed = models.DateTimeField(verbose_name='дата и время выполнения заявки', blank=True, null=True)


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-date',)

    def __str__(self):
        return f'{self.description}'


class Booking(models.Model):
    TIMESLOT_LIST = (
        (0, 'первая половина дня'),
        (1, 'вторая половина дня'),
        (2, 'весь день'),

    )

    APPROVED = 'Согласовано'
    IN_PROGRESS = 'Отправлено на согласование'
    STATUS = ((APPROVED, 'Согласовано'), (IN_PROGRESS, 'Отправлено на согласование'))


    date = models.DateField(default=timezone.now, verbose_name='дата')

    duration = models.IntegerField(choices=TIMESLOT_LIST,
                                   verbose_name='длительность')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name='арендатор',
                              null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS,
                              default=IN_PROGRESS, verbose_name='статус')

    def __str__(self):
        return (f' Бронь переговорки:{self.date}, '
                f'от арендатора {self.owner}')


    class Meta:
        verbose_name = 'Бронь переговорки'
        verbose_name_plural = 'Брони переговорки'


class Cars(models.Model):
    ONE_TIME = 'разовый'
    WEEK = 'на неделю'
    TWO_WEEKS = 'две недели'
    MONTH = 'на месяц'
    PERMANENT = 'на постоянной основе'
    PERIOD = ((ONE_TIME, 'разовый'),
              (WEEK, 'на неделю'),
              (TWO_WEEKS, 'две недели'),
              (MONTH, 'на месяц'),
              (PERMANENT, 'на постоянной основе'))

    APPROVED = 'Согласовано'
    IN_PROGRESS = 'Отправлено на согласование'
    STATUS = ((APPROVED, 'Согласовано'), (IN_PROGRESS, 'Отправлено на согласование'))

    car_id = models.CharField(max_length=100, verbose_name='номер авто', unique=True)
    model = models.CharField(max_length=100, verbose_name='модель')
    period = models.CharField(max_length=20, choices=PERIOD,
                              default=PERMANENT, verbose_name='период выдачи разрешения на доступ')
    status = models.CharField(max_length=100, choices=STATUS,
                              default=IN_PROGRESS, verbose_name='статус')
    price = models.IntegerField(verbose_name='цена',
                                null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              verbose_name='арендатор',
                              null=True, blank=True)

    def __str__(self):
        return f'{self.car_id}, {self.owner}'

    class Meta:
        verbose_name = 'Допуск авто'
        verbose_name_plural = 'Допуски авто'

