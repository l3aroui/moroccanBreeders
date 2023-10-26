from django.contrib import admin
from .models import Product
from .models import Category,Orders_Confirm

# Register your models here.




class Admin_product(admin.ModelAdmin):
    list_display =['name','price','category','date_time','active']
admin.site.register(Product,Admin_product)
admin.site.register(Category)



def livrer_commande(modeladmin, request, queryset):
    carts = set()
    
    for item in queryset:
        carts.add(item.cart)
        item.delete()
    
    for cart in carts:
        cart.itempanier_set.all().delete()
        cart.delete()


livrer_commande.short_description = "Livrer les itempaniers sélectionnés"


class OrdersConfirmAdmin(admin.ModelAdmin):
    list_display = ['cart']
    actions = [livrer_commande]
    readonly_fields = ['cart']
    def has_add_permission(self, request):
        return False
admin.site.register(Orders_Confirm,OrdersConfirmAdmin)

