from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import DraggableMPTTAdmin

from shops.models import Book, Category
from users.models import Address


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass


@admin.register(Address)
class AddressModelAdmin(ModelAdmin):
    pass