from django.contrib import admin
from .models import Category, Size, Product , \
    ProductImage , ProductSize
    
    
class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1
class ProductSizeInLine(admin.TabularInline):
    model = ProductSize
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'category' , 'color' , 'price']#По каким параметрам можно искать
    
    list_filter = ['category' , 'color']#по каким можно фильтровать 
    
    search_fields = ['name' , 'color' , 'descriprtion']#поиск по полям
    
    prepopulated_fields = {'slug': ('name',) }#Вводим name - заполняется slug
    
    inlines = [ProductImageInLine, ProductSizeInLine]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'slug']
    prepopulated_fields = {'slug': ('name', )}
    
    
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Category , CategoryAdmin)
admin.site.register(Size , SizeAdmin)
admin.site.register(Product , ProductAdmin)
    
    
    
    