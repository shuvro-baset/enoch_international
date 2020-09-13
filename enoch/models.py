from django.db import models



class Product(models.Model):
    # CATEGORY = (
    # 	# 		('Indoor', 'Indoor'),
    # 	# 		('Out Door', 'Out Door'),
    # 	# 		)

    name = models.CharField(max_length=200, null=True)
    image = models.ImageField()
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True)
    # category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=55, null=True)
    address = models.CharField(max_length=155, null=True)
    total_price = models.CharField(max_length=50, null=True)
