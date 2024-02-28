from django.contrib import admin
from .models import Product, Lesson, Group, Access


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'start_date', 'cost')
    search_fields = ('name', 'creator__username')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'video_url')
    search_fields = ('title', 'product__name')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'min_users', 'max_users')
    search_fields = ('name', 'product__name')
    filter_horizontal = ('users',)


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user__username', 'product__name')
