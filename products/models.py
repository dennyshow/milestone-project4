from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Product(models.Model):
    ARTEFACTS = (
        
        ('HISTO', 'Historical'),
        ('CULTU', 'Cultural'),
        ('RELIG', 'Religious'),
        ('MEDIA', 'Media'),
    )
    
    title = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to="images")
    details = models.CharField(max_length=255)
    history = models.TextField()
    quantity = models.IntegerField()
    artefact = models.CharField(max_length=5, choices=ARTEFACTS)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    auction_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return "(" + self.title + ", " + self.details + ", " + self.history + ", " + self.artefact + ")"