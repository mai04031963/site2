from django.db import models
from datetime import date
from django.utils.timezone import now

# Create your models here.


class Comments(models.Model):
    comment_date = models.DateField(auto_now_add=True, verbose_name='Дата')
    comment_text = models.TextField(blank=True, verbose_name='Отзыв')
    comment_sign = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    comment_contact = models.CharField(max_length=100, blank=True, verbose_name='Контакт')
    answer_for_comment = models.TextField(blank=True, verbose_name='Ответ на отзыв')
    answer_sign = models.CharField(max_length=100, blank=True, verbose_name='Подпись к ответу')

    def __str__(self):
        return str(self.comment_date)

    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзыв"
        ordering = ['-comment_date']