from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key =True)
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category

FileSystemStorage(location='/media/images')
class Product(models.Model):

    prd_id = models.AutoField
    prd_name = models.CharField(max_length=30)
    dics = models.CharField(max_length=500, default="")

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    img = models.ImageField(upload_to='shop/image',default = "")
    price= models.IntegerField(default=0)


    def __str__(self):
        return self.prd_name




class Cart(models.Model):
    id = models.AutoField(primary_key = True)
    prod_id = models.ForeignKey(Product, default='1', on_delete=models.SET_DEFAULT)

