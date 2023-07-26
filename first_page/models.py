from django.db import models
# Create your models here.


class Firm(models.Model):
    firm_name = models.CharField(max_length=40, verbose_name="Название фирмы")
    firm_adress = models.CharField(max_length=255, verbose_name="Адрес фирмы")
    firm_email = models.CharField(max_length=100, verbose_name="e-mail")
    firm_tel = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return str(self.firm_name)

    class Meta:
        verbose_name_plural = "Фирмы"
        verbose_name = "Фирма"
