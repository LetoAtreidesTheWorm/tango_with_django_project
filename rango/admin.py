from django.contrib import admin
from rango.models import Category, Page

class Admin_Page(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')

admin.site.register(Category, Admin_Page)

class Admin_Page(admin.ModelAdmin):
    list_display = ( 'title', 'category', 'url', 'views')

admin.site.register(Page, Admin_Page)
# Register your models here.
