from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone


# Модель новостей.
class Articles(models.Model):
    image = models.ImageField(upload_to='images_news/')
    title = models.CharField(max_length=200)
    full_text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


# Модель комментариев.
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья')
    comment_text = models.TextField('Текст комментария')
    comment_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'














# class Comment(models.Model):
#     new = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Новость')
#     author = models.CharField('Автор', max_length=30)
#     content = models.TextField('Содержание')
#     created_at = models.DateTimeField('Опубликован', auto_now_add=True, db_index=True)

#     class Meta:
#         verbose_name = 'Комментарий'
#         verbose_name_plural = 'Комментарии'
#         ordering = ['created_at']

