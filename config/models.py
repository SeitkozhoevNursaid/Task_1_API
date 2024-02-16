from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название продукта')
    description = models.TextField(verbose_name = 'Описание')
    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Название товара')
    price = models.IntegerField(verbose_name = 'Цена')
    description = models.TextField(verbose_name = 'Описание')
    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
        
    