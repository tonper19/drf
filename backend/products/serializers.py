from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    your_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'price', 'sale_price', 'your_discount']
        # read_only_fields = ['id', 'sale_price']

    def get_your_discount(self, obj):
        if not hasattr(obj, 'get_discount'):
            return None
        if not isinstance(obj, Product):
            return None
            
        return obj.get_discount()


  # def validate_price(self, value):
  #     if value < 0:
  #         raise serializers.ValidationError("Price cannot be negative.")
  #     return value
