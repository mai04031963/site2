from django.db import models

# Create your models here.


class Demands(models.Model):
    demand_date = models.DateTimeField(auto_now_add=True, name="demand_date", verbose_name="Дата заявки")
    demand_client = models.CharField(blank=True, max_length=50, name="demand_client", verbose_name="Клиент")
    demand_address = models.CharField(blank=True, max_length=80, name="demand_address", verbose_name="Адрес")
    demand_type = models.CharField(blank=True, max_length=25, name="demand_type", verbose_name="Вид заявки")
    demand_tech = models.CharField(blank=True, max_length=30, name="demand_tech", verbose_name="Аппарат")
    demand_serial = models.CharField(blank=True, max_length=25, name="demand_serial", verbose_name="Серийный номер")
    demand_description = models.CharField(blank=True, max_length=255, name="demand_description", verbose_name="Описание неисправности")
    demand_telephone = models.CharField(blank=True, max_length=12, name="demand_telephone", verbose_name="Телефон")
    demand_fio = models.CharField(blank=True, max_length=50, name="demand_fio", verbose_name="Имя")
    demand_email = models.CharField(blank=True, max_length=50, name="demand_email", verbose_name="e-mail")
    demand_in_base = models.BooleanField(auto_created=True, default=False, name="demand_in_base", verbose_name="Занесено в базу данных")

    def __str__(self):
        return str(self.demand_date)

    class Meta:
        verbose_name_plural = "Заявки"
        verbose_name = "Заявка"
        ordering = ['-demand_date']