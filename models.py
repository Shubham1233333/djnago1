from django.db import models

# Create your models here.
class order(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    address=models.TextField(max_length=30)
    product_name=models.CharField(max_length=20)
    price=models.IntegerField(max_length=20)
    quantity=models.IntegerField(default="1")
    def __str__(self):
        return self.name
    
