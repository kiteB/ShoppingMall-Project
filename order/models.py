from django.db import models


class Order(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)