from django.db import models

# Create your models here.
class Product(models.Model):
    Brand=models.CharField(max_length=30)
    Description=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.Brand

class ProductDetails(models.Model):
    Statusis=(
            ('Available','Ready to sale'),
            ('Sold','Not available'),
            ('Restock','coming in stock')
        )
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    ModelNo=models.CharField(max_length=30,blank=False)
    Price=models.FloatField()
    Stock=models.IntegerField()
    Status=models.CharField(max_length=40,choices=Statusis,default="Available")
    Description=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.ModelNo

class Customer(models.Model):
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    MobileNo=models.IntegerField()
    EmailId=models.EmailField(max_length=100, unique=False)

    def __str__(self):
        return self.Name

class Order(models.Model):
    proddetails=models.ForeignKey('ProductDetails',on_delete=models.CASCADE)
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    UnitPrice=models.FloatField()
    TotalAmount=models.FloatField()
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Date

class Sales(models.Model):
    order=models.ForeignKey('Order',on_delete=models.CASCADE)
    InvoiceNo=models.IntegerField()
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.InvoiceNo

class Payment(models.Model):
    Typeis=(
            ('ByCash','Pay through cash'),
            ('ByCard','Pay through card'),
            ('Online mode','Pay Online')
        )
    sales=models.ForeignKey('Sales',on_delete=models.CASCADE)
    PaymentType=models.CharField(max_length=70,choices=Typeis,default="ByCash")
    