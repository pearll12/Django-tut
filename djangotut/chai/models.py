from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator,MinLengthValidator
from datetime import timedelta

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

# Relationships - One to Many
class chaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name="review")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #from django.core.validators import MinValueValidator, MaxValueValidator
    comment = models.TextField(max_length=200)
    date_added = models.DateTimeField(default = timezone.now)

    def __str__(self): #dunder string function
        return f'{self.user} review for {self.chai.name}'

# Many to Many
class Store(models.Model):
    name =  models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name
    
# One to One
def defaultuntil():
    return timezone.now() + timedelta(days=600)

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, related_name="certificate", on_delete=models.CASCADE)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(default=defaultuntil) 
    certificate_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])

    def __str__(self):
        return f'Certificate for {self.chai.name}'
