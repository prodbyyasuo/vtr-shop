from django.contrib import admin
from django.utils.html import format_html
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ['added_at', 'get_total_price']
    fields = ['product', 'product_size', 'quantity', 'get_total_price', 'added_at']

    def get_total_price(self, obj):
        if obj.id:
            return format_html(
                '<strong>${}</strong>',
                obj.total_price
            )
        return '-'

    get_total_price.short_description = 'Total Price'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_total_items', 'get_subtotal', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['created_at', 'updated_at', 'get_subtotal', 'get_total_items']
    inlines = [CartItemInline]

    fieldsets = (
        ('Cart Information', {
            'fields': ('user', 'get_total_items', 'get_subtotal')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_total_items(self, obj):
        return obj.total_items

    get_total_items.short_description = 'Total Items'

    def get_subtotal(self, obj):
        return format_html(
            '<strong>${}</strong>',
            obj.subtotal
        )

    get_subtotal.short_description = 'Subtotal'

    actions = ['clear_carts']

    def clear_carts(self, request, queryset):
        total_items = sum(cart.total_items for cart in queryset)
        for cart in queryset:
            cart.clear()
        self.message_user(
            request,
            f'Successfully cleared {queryset.count()} cart(s) with {total_items} items.'
        )

    clear_carts.short_description = 'Clear selected carts'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'product_size', 'quantity', 'get_total_price', 'added_at']
    list_filter = ['added_at', 'product']
    search_fields = ['cart__user__username', 'product__name']
    readonly_fields = ['added_at', 'get_total_price']

    fieldsets = (
        ('Item Information', {
            'fields': ('cart', 'product', 'product_size', 'quantity')
        }),
        ('Pricing', {
            'fields': ('get_total_price',)
        }),
        ('Timestamps', {
            'fields': ('added_at',),
            'classes': ('collapse',)
        }),
    )

    def get_total_price(self, obj):
        return format_html(
            '<strong>${}</strong>',
            obj.total_price
        )

    get_total_price.short_description = 'Total Price'