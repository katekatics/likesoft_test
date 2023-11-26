from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    pub_year = models.IntegerField(verbose_name='Год публикации')
    isbn = models.CharField(max_length=13, verbose_name='ISBN')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["name"]

    def __str__(self):
        return self.name
