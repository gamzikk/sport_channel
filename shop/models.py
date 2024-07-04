from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Модель товаров в магазине.
class Product(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images_products/', verbose_name='Изображение товара')
	name = models.CharField(max_length=30, verbose_name='Название товара')
	text = models.TextField('Описание')
	price = models.IntegerField(verbose_name='Цена товара')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата объявления')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'