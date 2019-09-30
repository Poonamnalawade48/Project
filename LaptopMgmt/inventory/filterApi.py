from inventory.models import *
from rest_framework import viewsets,permissions,generics
from inventory.serializers import *

#filter laptops depending upon brand
class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    queryset=queryset.filter(Brand="Hp")

#filter laptops whose price less than 30000
class PriceLessProduct(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    queryset=queryset.filter(Price__lte=30000)

#filter laptops whose status is Available
class StatusAvailableProduct(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    queryset=queryset.filter(Status="Available")

#delete record
class DeleteProduct(viewsets.ModelViewSet):
    queryset=ProductDetails.objects.filter(product_id=25)
    serializer_class=ProductDetailsSerializer
    queryset.delete()

#update record
class UpdateRecord(viewsets.ModelViewSet):
    queryset=ProductDetails.objects.filter(Status="Available")
    queryset.update(Status="Sold")
    queryset=ProductDetails.objects.filter(Status="Sold")
    serializer_class=ProductDetailsSerializer
