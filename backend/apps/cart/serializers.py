from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    product_info = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = [
            'id', 'product', 'product_size', 'quantity',
            'total_price', 'added_at', 'product_info'
        ]

    def get_product_info(self, obj):
        return {
            'name': obj.product.name,
            'price': obj.product.price,
            'image': obj.product.image.url if obj.product.image else None
        }


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    total_items = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart
        fields = [
            'id', 'user', 'items', 'subtotal',
            'total_items', 'created_at', 'updated_at'
        ]


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_size_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1, default=1)

    def validate_product_id(self, value):
        """Проверка существования товара"""
        try:
            from main.models import Product
            product = Product.objects.get(id=value)
            if not product.is_active:
                raise serializers.ValidationError("Product is not active")
            return value
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found")


class UpdateCartItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)