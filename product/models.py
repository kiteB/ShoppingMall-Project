from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    explanation = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product/", blank=True, null=True)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
