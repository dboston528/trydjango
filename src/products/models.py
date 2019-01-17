from django.db import models

# Create your models here.
class Product(models.Model):
    title          = models.CharField(max_length=120) #Max of 120 characters required
    description    = models.TextField(blank=True, null=True)
    price          = models.DecimalField(decimal_places=2, max_digits=10000, default=00.00)
    summary        = models.TextField()