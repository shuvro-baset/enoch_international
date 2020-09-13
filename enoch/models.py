from django.db import models
from .shortcuts import product_image_upload_path


class Product(models.Model):
    # CATEGORY = (
    # 	# 		('Indoor', 'Indoor'),
    # 	# 		('Out Door', 'Out Door'),
    # 	# 		)

    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=product_image_upload_path)
    description = models.TextField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    # category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.id} - {self.name} - {self.price}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=55, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    total_price = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.name} - {self.email} - {self.total_price}"
