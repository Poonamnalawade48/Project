from inventory.models import *
from rest_framework import viewsets,permissions
from inventory.serializers import *

#Product viewset
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=ProductSerializer

    #ProductDetails Viewset
class ProductDetailsViewSet(viewsets.ModelViewSet):
    queryset=ProductDetails.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=ProductDetailsSerializer

       #Customer Viewset
class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=CustomerSerializer

#Order viewset
class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=OrderSerializer

#Sales viewset
class SalesViewSet(viewsets.ModelViewSet):
    queryset=Sales.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=SalesSerializer

#Payment viewset
class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=PaymentSerializer