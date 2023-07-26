from django.db import models
# Create your models here


class News(models.Model):
    news_date = models.DateField(auto_now_add=True, verbose_name="Дата")
    news_text = models.TextField(blank=True, verbose_name="Новость")

    def __str__(self):
        return str(self.news_text)

    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "Новость"
        ordering = ['-news_date']