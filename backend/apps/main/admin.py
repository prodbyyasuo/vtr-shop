from django.contrib import admin
from django.utils.html import format_html
from .models import Brand, Category, Size, Product, ProductSize, ProductImage


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'logo_preview', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'logo_preview', 'banner_preview']

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'description', 'is_active')
        }),
        ('Изображения', {
            'fields': ('logo', 'logo_preview', 'banner', 'banner_preview')
        }),
        ('Системная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.logo.url
            )
        return "Нет изображения"

    logo_preview.short_description = 'Превью логотипа'

    def banner_preview(self, obj):
        if obj.banner:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 200px;" />',
                obj.banner.url
            )
        return "Нет изображения"

    banner_preview.short_description = 'Превью баннера'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1
    fields = ['size', 'stock']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'image_preview', 'is_main', 'order']
    readonly_fields = ['image_preview']
    ordering = ['order']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.image.url
            )
        return "Нет изображения"

    image_preview.short_description = 'Превью'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'article', 'brand', 'category',
        'price', 'sex', 'main_image_preview', 'created_at'
    ]
    list_filter = ['brand', 'category', 'sex', 'created_at']
    search_fields = ['name', 'article', 'description']
    readonly_fields = ['created_at', 'updated_at', 'main_image_preview']
    inlines = [ProductImageInline, ProductSizeInline]

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'article', 'brand', 'category', 'price')
        }),
        ('Характеристики', {
            'fields': ('material', 'product_print', 'clothing_cut', 'sex', 'sending')
        }),
        ('Описание', {
            'fields': ('description',)
        }),
        ('Системная информация', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def main_image_preview(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        if not main_image:
            main_image = obj.images.first()

        if main_image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                main_image.image.url
            )
        return "Нет изображения"

    main_image_preview.short_description = 'Главное фото'


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'stock']
    list_filter = ['size', 'product__brand', 'product__category']
    search_fields = ['product__name', 'size__name']
    list_editable = ['stock']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_preview', 'is_main', 'order', 'created_at']
    list_filter = ['is_main', 'created_at']
    search_fields = ['product__name']
    list_editable = ['is_main', 'order']
    readonly_fields = ['image_preview', 'created_at']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px;" />',
                obj.image.url
            )
        return "Нет изображения"

    image_preview.short_description = 'Превью изображения'
