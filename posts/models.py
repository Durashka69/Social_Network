from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название поста')
    author = models.ForeignKey(
        User, verbose_name='Автор', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Содержание поста')
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='likes')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
