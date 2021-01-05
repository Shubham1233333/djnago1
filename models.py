from django.db import models

# Create your models here.
class Brand(models.Model):
    name=models.CharField(max_length=20,null=True ,blank=True)
    def __str__(self):
        return self.name
    
class catogery(models.Model):
    name=models.CharField(max_length=20,null=True ,blank=True)
    def __str__(self):
        return self.name
      


class product(models.Model):
    name=models.CharField(max_length=20 ,null=True ,blank=True)
    price=models.FloatField(max_length=10)
    pic=models.ImageField(upload_to='products',null=True,blank=True)
    list_price=models.FloatField(max_length=10)
    quantity=models.FloatField(max_length=10)
    catogery=models.ForeignKey(catogery,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    description=models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
    @staticmethod
    def get_all__product():
        return product.objects.all()    
    @staticmethod
    def get_all__product_by_id(catogery_id):
        if catogery_id:

              resp=product.objects.filter(catogery_id=catogery_id)
              return resp
        else:
            return product.get_all__product()
    @staticmethod
    def get_product_by_id(kyes):
       

              resp=product.objects.filter(id__in=kyes) 
              return resp       
                  


