from inventory.models import *
from rest_framework import viewsets,permissions,generics
from inventory.serializers import *
from django.core.paginator import Paginator

#insert products
class ProductInsertion(viewsets.ModelViewSet):
    product=Product(Brand="Acer",Description="Good Brand")
    product.save()
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

#insert productDetails
class ProductDetailsInsertion(viewsets.ModelViewSet):
    product=Product(Brand="Acer",Description="Good Brand")
    product.save()
    #status= foo_select = forms.ModelMultipleChoiceField("Available")
    productdetails=ProductDetails(product=product,ModelNo="Acer101",Price=30000,Stock=30,Description="model no is Acser101")
    productdetails.save()
    queryset=ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer

