from django.db import models
from .shortcuts import product_image_upload_path


class Product(models.Model):
    CATEGORY = (
        ('SPC', 'SPC'),
        ('WPC', 'WPC'),
        ('Rockwood Board', 'Rockwood Board'),
        ('Toilet Partition', 'Toilet Partition'),
    )

    name = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to=product_image_upload_path)
    description = models.TextField(max_length=200)
    price = models.FloatField(default='00.00')
    category = models.CharField(max_length=200, choices=CATEGORY, default=CATEGORY[0])

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.id} - {self.name} - {self.price}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=55)
    address = models.TextField()
    total_price = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.name} - {self.email} - {self.total_price}"
