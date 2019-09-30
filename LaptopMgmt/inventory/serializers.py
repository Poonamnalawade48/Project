from rest_framework import serializers
from inventory.models import *

#Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

#Productdetails serializer
class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDetails
        fields='__all__'

#Customer serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

#Order serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

#Sales serializer
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields='__all__'

#Payment serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'