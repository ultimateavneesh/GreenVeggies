from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendor_firstname = models.CharField(max_length=20, default="")
    vendor_lastname = models.CharField(max_length=20, default="")
    vendor_username = models.CharField(max_length=20, default="")
    vendor_contact = models.CharField(max_length=20, default="")
    vendor_email = models.CharField(max_length=50, default="")
    vendor_address = models.CharField(max_length=100, default="")
    vendor_city = models.CharField(max_length=20, default="")
    vendor_state = models.CharField(max_length=20, default="")
    vendor_zip = models.CharField(max_length=10, default="")

    # Product Prices
    apple = models.CharField(max_length=20)
    banana = models.CharField(max_length=20)
    broccoli = models.CharField(max_length=20)
    cabbage = models.CharField(max_length=20)
    capsicum = models.CharField(max_length=20)
    carrot = models.CharField(max_length=20)
    cauliflower = models.CharField(max_length=20)
    chilly = models.CharField(max_length=20)
    coriander = models.CharField(max_length=20)
    cucumber = models.CharField(max_length=20)
    garlic = models.CharField(max_length=20)
    ginger = models.CharField(max_length=20)
    grapes = models.CharField(max_length=20)
    guava = models.CharField(max_length=20)
    jackfruit = models.CharField(max_length=20)
    lemon = models.CharField(max_length=20)
    lychee = models.CharField(max_length=20)
    mango = models.CharField(max_length=20)
    mushroom = models.CharField(max_length=20)
    onion = models.CharField(max_length=20)
    orange = models.CharField(max_length=20)
    papaya = models.CharField(max_length=20)
    pear = models.CharField(max_length=20)
    pea = models.CharField(max_length=20)
    pineapple = models.CharField(max_length=20)
    pomegranate = models.CharField(max_length=20)
    potato = models.CharField(max_length=20)
    pumpkin = models.CharField(max_length=20)
    scallion = models.CharField(max_length=20)
    spinach = models.CharField(max_length=20)
    tomato = models.CharField(max_length=20)
    turnip = models.CharField(max_length=20)
    watermelon = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.vendor_firstname

class Customer(models.Model):
    customer_firstname = models.CharField(max_length=20, default="")
    customer_lastname = models.CharField(max_length=20, default="")
    customer_username = models.CharField(max_length=20, default="")
    customer_contact = models.CharField(max_length=20, default="")
    customer_email = models.CharField(max_length=50, default="")
    customer_address = models.CharField(max_length=100, default="")
    customer_city = models.CharField(max_length=20, default="")
    customer_state = models.CharField(max_length=20, default="")
    customer_zip = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.customer_firstname
