from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Page(models.Model):
    product_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return "user_id:" + str(self.user_id) + "product_id:" + str(self.product_id)