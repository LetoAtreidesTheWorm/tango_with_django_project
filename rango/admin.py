from django.contrib import admin
from rango.models import Category, Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'views', 'likes')

admin.site.register(Category, CategoryAdmin)

class Admin_Page(admin.ModelAdmin):
    list_display = ( 'title', 'category', 'url', 'views')

admin.site.register(Page, Admin_Page)

admin.site.register(UserProfile)
# Register your models here.
