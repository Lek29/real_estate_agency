from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField(
        'Наличие балкона',
        null=True,
        blank=True,
        db_index=True)

    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField(
        'Новостройка',
        null=True,
        blank=True,
        default=None,
    )

    likes = models.ManyToManyField(
        User,
        related_name='liked_flats',
        verbose_name='Кто лайкнул',
        blank=True,
    )

    owners = models.ManyToManyField(
        'Owner',
        related_name='properties',
        verbose_name='Собственники',
        blank=True,
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}.)'

    class Meta():
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Кто жаловался:',
        related_name='reports',
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name='Квартира, на которую пожаловались',
        related_name='issues',
    )
    text = models.TextField(
        verbose_name='Текст жалобы'
    )

    def __str__(self):
        return f'Жалоба от {self.user} на квартиру {self.flat}'

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200, db_index=True)
    phonenumbers = models.CharField('Номер владельца', max_length=20)
    pure_phone = models.CharField(
                            'Нормализованный номер владельца',
                            max_length=20,
                            blank=True,
                            null=True,
                            db_index=True,
    )
    flat = models.ManyToManyField(
        Flat,
        related_name='flat_owners',
        verbose_name='Квартиры в собственности'
    )

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
