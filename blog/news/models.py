from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class News(models.Model):
    user = models.ForeignKey(User, verbose_name='Автор',
                             on_delete=models.CASCADE,)
    title = models.CharField(max_length=150, verbose_name='Заголовок',
                             db_index=True)
    text = models.TextField(max_length=None, verbose_name='Текст статті',
                            blank=True)
    image = models.ImageField(upload_to='img', blank=True, null=True,
                              verbose_name='Картинка')
    created = models.DateTimeField(verbose_name='Дата створення',
                                   auto_now_add=True)
    description = models.CharField(verbose_name='Опис', max_length=150,
                                   blank=True)
    keywords = models.CharField(verbose_name='Ключові слова', max_length=350,
                                blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')
    category = models.ForeignKey("Category", on_delete=models.SET_NULL,
                                 verbose_name='Категорія',
                                 blank=True, null=True, related_name="category")

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
        ordering = ['-created']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тегі'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags_detail', kwargs={'pk': self.pk})


class Comments(models.Model):
    user = models.ForeignKey(User, verbose_name='Коментатор',
                             on_delete=models.CASCADE)
    new = models.ForeignKey(News, verbose_name='Новина',
                            on_delete=models.CASCADE)
    text = models.TextField(max_length=None, verbose_name='Коментар',
                            blank=True)
    created = models.DateTimeField(verbose_name='Дата створення',
                                   auto_now_add=True)
    moderation = models.BooleanField(default=False,
                                     verbose_name='Можливість редагувати')

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['-created']

    def __str__(self):
        return '{}'.format(self.user)
