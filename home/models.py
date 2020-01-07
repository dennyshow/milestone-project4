from django.db import models
from products.models import Product

# Create your models here.

class Page(models.Model):
    product_id = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return "product_id:" + str(self.product_id)