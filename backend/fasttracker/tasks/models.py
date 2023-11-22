from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(verbose_name='Категория задачи', max_length=200)
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title[:15]

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(verbose_name='Название задачи', max_length=254)
    description = models.TextField(verbose_name='Описание задачи')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор задачи', related_name='posts')
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', null=True, blank=True, related_name='posts')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.title[:15]} {self.author}'

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.author
