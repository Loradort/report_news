from django.contrib import admin
from .models import Category, Classes

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)


@admin.register(Classes)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'class_name', 'class_credit', 'class_year', 'semester', 'class_category')