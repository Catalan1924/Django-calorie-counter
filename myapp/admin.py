from django.contrib import admin
from .models import FoodItem

admin.site.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', 'calories', 'date')
    search_fields = ('name',)
    list_filter = ('date',)
    ordering = ('-date', '-id')
