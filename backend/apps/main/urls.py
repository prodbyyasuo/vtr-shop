from django.urls import path
from . import views

urlpatterns = [
    # Brands
    path('brands/', views.BrandListView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', views.BrandDetailView.as_view(), name='brand-detail'),

    # Products
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    # Favorites
    path('favorites/', views.FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/<int:pk>/', views.FavoriteDetailView.as_view(), name='favorite-delete'),
    path('favorites/toggle/<int:product_id>/', views.toggle_favorite, name='toggle-favorite'),
    path('favorites/check/<int:product_id>/', views.is_favorite, name='is-favorite'),
]