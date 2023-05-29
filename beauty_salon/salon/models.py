from django.db import models


class Clients(models.Model):
    td_id = models.PositiveIntegerField(
        verbose_name='telegram ID клиента',
    )
    name = models.TextField(
        verbose_name='Имя пользователя',
    )
    client_phone_number = models.TextField(
        verbose_name='Номер телефона клиента',
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Salon(models.Model):
    name = models.TextField(
        verbose_name='Название салона',
    )
    adress = models.TextField(
        verbose_name='Адрес салона',
    )
    salon_phone_number = models.TextField(
        verbose_name='Номер телефона салона',
    )
    master = models.TextField(
        verbose_name='Имя мастера',
    )
    service = models.TextField(
        verbose_name='Наименование услуги',
    )
    price = models.IntegerField(
        verbose_name='Цена услуги',
    )
    visit_time = models.TextField(
        verbose_name='Время визита',
    )

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Master(models.Model):
    name = models.TextField(
        verbose_name='Имя мастера',
    )
    working_hours = models.TextField(
        verbose_name='Расписание мастера',
    )

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
