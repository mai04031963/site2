from django.db import models
from datetime import date
# Create your models here


class News(models.Model):
    news_date = models.DateField(auto_now_add=True)
    news_text = models.TextField(blank=True)