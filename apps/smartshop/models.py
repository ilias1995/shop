from django.db import models

class NameProduct(models.Model):
	name = models.CharField(max_length=200)

class Product(models.Model):
	nameproduct = models.ForeignKey(NameProduct)
	name_pro = models.CharField(max_length=200)
	price = models.IntegerField()
	photos = models.ImageField(upload_to='images')
	about = models.TextField()



