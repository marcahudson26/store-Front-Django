from django.db import models



class Order (models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"
    
    PAYMENT_STATUS_CHOICES =[
        (PAYMENT_STATUS_COMPLETE , "complete"),
        (PAYMENT_STATUS_FAILED , "failed"),
        (PAYMENT_STATUS_PENDING,"pending")
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices= PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)


class Product(models.Model):
    

    
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update= models.DateField(auto_now=True)
    



class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "g"
    
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "bronze"),
        (MEMBERSHIP_SILVER,"silver"),
        (MEMBERSHIP_GOLD, "gold"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)
    
    
    