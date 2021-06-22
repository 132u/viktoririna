from django.db import models


# Create your models here.
class Order(models.Model):
    customer = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    comment = models.CharField(max_length=255)
    driver_name = models.CharField(max_length=255)

    def __str__(self):
        return f'Водитель {self.driver_name} ездил {self.date}, заработал {self.price}, заказчик = {self.customer}'
