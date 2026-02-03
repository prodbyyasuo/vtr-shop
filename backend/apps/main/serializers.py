from rest_framework import serializers
from .models import Category, Product, Brand, ProductImage, ProductSize, Size, Favorite


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products_count', 'created_at']

    def get_products_count(self, obj):
        return obj.products.count()


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']


class ProductSizeSerializer(serializers.ModelSerializer):
    size = SizeSerializer(read_only=True)

    class Meta:
        model = ProductSize
        fields = ['id', 'size', 'stock']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_main', 'order', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'article', 'description', 'price', 'category', 'category_name',
            'brand', 'brand_name', 'main_image',
            'created_at', 'updated_at'
        ]

    def get_main_image(self, obj):
        main_img = obj.images.filter(is_main=True).first()
        if main_img:
            return ProductImageSerializer(main_img).data
        return None


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo', 'banner', 'description', 'is_active', 'created_at']


class BrandDetailSerializer(BrandSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta(BrandSerializer.Meta):
        fields = BrandSerializer.Meta.fields + ['products']


class ProductDetailSerializer(ProductSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    sizes = ProductSizeSerializer(source='product_sizes', many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'article', 'material', 'product_print', 'clothing_cut',
            'sex', 'sending', 'description', 'price', 'brand', 'category',
            'created_at', 'updated_at'
        ]


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True
    )

    class Meta:
        model = Favorite
        fields = ['id', 'product', 'product_id', 'created_at']
        read_only_fields = ('id', 'created_at')


