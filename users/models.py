from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        # Get instance of registered user
        user = User.objects.get(id=self.user_id)
        return "id=" + str(self.pk) + "username=" + user.username + "email=" + user.email
    