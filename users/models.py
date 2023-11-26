from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    reg_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
