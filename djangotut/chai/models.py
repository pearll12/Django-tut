from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KI', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/') 
    date_added = models.DateField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default =10)

    def __str__(self): #dunder string function
        return self.name #reason? check 9.3 readme