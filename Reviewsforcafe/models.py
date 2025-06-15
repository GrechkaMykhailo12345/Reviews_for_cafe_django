from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок відгуку")
    content = models.TextField(verbose_name="Текст відгуку")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"

    def __str__(self):
        return self.title