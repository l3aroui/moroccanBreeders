from django.contrib import admin
from .models import Breeders,Profile,Delivery,Breeder_payment
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms

class BreedersAdmin(admin.ModelAdmin):
    # form = BreedersAdminForm
    list_display=['user','milk_quantity','balance']
    readonly_fields = ( 'milk_quantity', 'balance')
    actions = ['pay_breeders']

    def pay_breeders(self, request, queryset):
        for breeders in queryset:
            if breeders.milk_quantity > 0:
                milk_quantity = breeders.milk_quantity
                balance = breeders.balance
                breeders.make_payment(milk_quantity, balance)
        
        self.message_user(request, "Breeders have been successfully paid.")

    pay_breeders.short_description = "Pay the breeders"
# Register the Breeders model with the custom admin
admin.site.register(Breeders, BreedersAdmin)





class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_time'].widget.attrs['readonly'] = True

class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryForm
    list_display = ['breeders', 'date_time', 'milk_quantity', 'liter_price']

    def save_model(self, request, obj, form, change):
        breeders = obj.breeders
        breeders.add_milk_quantity(obj.milk_quantity)
        breeders.update_balance(obj.milk_quantity, obj.liter_price)
        breeders.save()
        obj.save()

    def get_readonly_fields(self, request, obj=None):
        if obj:  # For existing objects, make all fields read-only
            return self.fields
        return []  # For new objects, no fields will be read-only
    
admin.site.register(Delivery, DeliveryAdmin)

# Autres importations et définitions d'admin si elles existent

# Définition des classes d'administration
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email', 'get_phone_number', 'last_name', 'is_staff')

    def get_phone_number(self, obj):
        return obj.profile.phone_number if hasattr(obj, 'profile') else None

    #get_phone_number.short_description = 'Phone Number'

# Enregistrement des classes d'administration
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class BreederPaymentsAdmin(admin.ModelAdmin):
    list_display = ['breeders', 'milk_quantity', 'balance', 'date_time']
    readonly_fields = ['breeders', 'milk_quantity', 'balance', 'date_time']
    search_fields = ['breeders__user__username']
    list_filter = ['date_time']
    def has_add_permission(self, request):
        return False

admin.site.register(Breeder_payment, BreederPaymentsAdmin)