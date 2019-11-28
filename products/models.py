from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    ARTEFACTS = (
        
        ('HIS', 'Historical'),
        ('CUL', 'Cultural'),
        ('REL', 'Religious'),
        ('MED', 'Media'),
    )
    
    title = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to="images")
    details = models.CharField(max_length=255)
    history = models.TextField()
    quantity = models.IntegerField()
    artefact = models.CharField(max_length=3, choices=ARTEFACTS)
    posted_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return "(" + self.title + ", " + self.details + ", " + self.history + ", " + self.artefact + ")"