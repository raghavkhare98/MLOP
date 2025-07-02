from django.db import models

# Create your models here.
class Product(models.Model):

    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_mfg_date = models.DateTimeField()
    product_expiry_date = models.DateTimeField()
    product_price = models.FloatField(default=0.0)
    product_vendor = models.CharField(max_length=100)

class Customer(models.Model):

    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)

class Order(models.Model):

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_time = models.DateTimeField()