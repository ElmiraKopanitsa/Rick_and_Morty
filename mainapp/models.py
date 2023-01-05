from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name='Локация')
    world = models.CharField(max_length=255, verbose_name='Измерение')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='location/', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Character(models.Model):
    GENDER = (
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('unknow', 'неизвестно')
    )

    ALIVE = (
        ('alive', 'Живой'),
        ('death', 'Мертвый'),
        ('unknow', 'неизвестно')
    )
    name = models.CharField(max_length=255, verbose_name='Персонаж')
    birth_location = models.ForeignKey(Location, related_name="birth_location", on_delete=models.SET_NULL, null=True, verbose_name='Место рождения')
    location = models.ForeignKey(Location, related_name="location", on_delete=models.SET_NULL, null=True, verbose_name='Место нахождения')
    description = models.TextField(verbose_name='Характеристика')
    image = models.ImageField(upload_to='characters/', verbose_name='Изображение')
    gender = models.CharField(max_length=50, choices=GENDER, verbose_name='Гендер')
    race = models.CharField(max_length=100, verbose_name='Раса')
    alive = models.CharField(max_length=50, choices=ALIVE, verbose_name='Статус жизни')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Epizod(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    number = models.PositiveIntegerField(verbose_name='Номер серии')
    number_season = models.PositiveIntegerField(verbose_name='Номер сезона')
    image = models.ImageField(upload_to='epizod/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    premiere = models.DateField(verbose_name='Дата')
    characters = models.ManyToManyField(Character, related_name='herois',  verbose_name='Персонажи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Эпизод'
        verbose_name_plural = 'Эпизоды'
