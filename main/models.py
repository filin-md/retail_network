from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release = models.DateField(verbose_name='Дата выхода продукта на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title} - {self.model}'


class NetworkUnit(models.Model):
    TYPES = [
        ('factory', 'Завод'),
        ('retail', 'Розничная сеть'),
        ('businessman', 'ИП'),
    ]

    title = models.CharField(max_length=150, verbose_name='Название')
    type = models.CharField(max_length=30, choices=TYPES, verbose_name='Тип ')
    products = models.ManyToManyField(Product, blank=True, null=True, verbose_name='Продукты')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    level = models.IntegerField(default=None, blank=True, null=True, editable=False, verbose_name='Уровень в иерархии')


    class Meta:
        verbose_name = 'Объект сети'
        verbose_name_plural = 'Объекты сети'

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if self.type == 'factory':
            self.level = 0
            self.supplier = None
        elif self.supplier.type == 'factory':
            self.level = 1
        elif self.supplier and self.supplier.type == 'retail' or self.supplier and self.supplier.type == 'businessman':
            self.level = 2
        else:
            self.level = None

        super().save(*args, **kwargs)

class Contact(models.Model):
    email = models.EmailField(verbose_name='e-mail')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house = models.PositiveSmallIntegerField(verbose_name='Номер дома')
    unit = models.OneToOneField(NetworkUnit, on_delete=models.CASCADE, verbose_name='Контакт')


    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
