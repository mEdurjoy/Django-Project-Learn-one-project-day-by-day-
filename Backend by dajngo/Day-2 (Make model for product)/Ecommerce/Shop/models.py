from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATAGORY_CHOICES = (
    ('S', 'Saree'),
    ('L', 'Lahenga'),
    ('BK', 'Borka'),
    ('GP', 'Gents Pant'),
    ('BF', 'Baby Fashion'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATAGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)