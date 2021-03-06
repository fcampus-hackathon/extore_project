from django.contrib import admin
from .models import Category, Board


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)

class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'created', 'updated', ]
    ordering = ['-created']

admin.site.register(Board, BoardAdmin)
