from django.db import models

# Create your models here.
class CommonCommands(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		abstract = True
		
#tables
class User(CommonCommands):
	first_name = models.TextField()
	last_name = models.TextField()
	email = models.EmailField()
	shipping_address = models.TextField()
	
class Product(CommonCommands):
	price = models.FloatField()
	product_name = models.TextField()
	product_description = models.TextField()
	
class Cart(CommonCommands):
	cart_code = models.CharField(max_length = 30)
	total_price = models.FloatField()
	paid = models.BooleanField()
	Products = models.ManyToManyField('Product')
	
class Holidate(CommonCommands):
	Day = models.IntegerField()
	Month = models.IntegerField()
	Holiday = models.TextField()
	