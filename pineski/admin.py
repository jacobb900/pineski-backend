from django.contrib import admin
from .models import Pin, PinImage


class PinImageInline(admin.TabularInline):
    model = PinImage
    extra = 1


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'address', 'latitude', 'longitude', 'created_at']
    list_filter = ['category']
    search_fields = ['name', 'address']
    inlines = [PinImageInline]


@admin.register(PinImage)
class PinImageAdmin(admin.ModelAdmin):
    list_display = ['pin', 'image']