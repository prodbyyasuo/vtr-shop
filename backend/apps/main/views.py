from rest_framework import generics, filters, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Count, Avg
from .models import Category, Product, Brand, ProductSize, Favorite
from .serializers import (
    CategorySerializer, ProductSerializer,
    ProductDetailSerializer, ProductCreateUpdateSerializer,
    BrandSerializer, BrandDetailSerializer, FavoriteSerializer
)


class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return BrandSerializer
        return BrandDetailSerializer


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name', 'description', 'article']
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)

        # Фильтр по цене
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        # Фильтр по наличию (проверяем, есть ли товары с размерами в наличии)
        in_stock = self.request.query_params.get('in_stock')
        if in_stock and in_stock.lower() == 'true':
            # Получаем ID товаров, у которых есть размеры в наличии
            product_ids_with_stock = ProductSize.objects.filter(
                stock__gt=0
            ).values_list('product_id', flat=True).distinct()

            queryset = queryset.filter(id__in=product_ids_with_stock)

        # Сортировка
        sort_by = self.request.query_params.get('sort_by')

        if sort_by == 'popular':
            # Сортировка по популярности (в реальном проекте можно добавить поле popularity_score)
            # Пока сортируем по количеству связанных размеров как признак популярности
            queryset = queryset.annotate(
                size_count=Count('product_sizes')
            ).order_by('-size_count', '-created_at')
        elif sort_by == 'newest':
            # Сортировка по новизне (уже есть в ordering по умолчанию)
            queryset = queryset.order_by('-created_at')
        elif sort_by == 'sale':
            # Сортировка по акции (в реальном проекте можно добавить поле is_on_sale)
            # Пока просто сортируем по возрастанию цены (предполагаем, что "на распродаже" дешевле)
            queryset = queryset.order_by('price')
        elif sort_by == 'cheapest':
            queryset = queryset.order_by('price')
        elif sort_by == 'most_expensive':
            queryset = queryset.order_by('-price')
        else:
            # Если не указана сортировка, используем стандартную
            queryset = queryset.order_by('-created_at')

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateUpdateSerializer
        return ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProductCreateUpdateSerializer
        return ProductDetailSerializer


# Функции резервирования не нужны, так как у нас система размеров
# Вместо общего stock_quantity у нас ProductSize с отдельным количеством для каждого размера


class FavoriteListView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteDetailView(generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def toggle_favorite(request, product_id):
    """
    Добавить или удалить товар из избранного
    """
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        product=product
    )

    if created:
        message = 'Product added to favorites'
        status_code = status.HTTP_201_CREATED
    else:
        favorite.delete()
        message = 'Product removed from favorites'
        status_code = status.HTTP_204_NO_CONTENT

    return Response({'message': message}, status=status_code)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def is_favorite(request, product_id):
    """
    Проверить, находится ли товар в избранном у пользователя
    """
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    is_fav = Favorite.objects.filter(user=request.user, product=product).exists()
    return Response({'is_favorite': is_fav})
