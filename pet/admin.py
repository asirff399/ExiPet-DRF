from django.contrib import admin
from .models import Pet,PetType,Adoption
# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','gender','price']

class AdoptionAdmin(admin.ModelAdmin):
    list_display = ['customer','pet__name','adopted_on','pet_price','balance_after_adoption']

class PetTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Pet,PetAdmin)
admin.site.register(PetType,PetTypeAdmin)
admin.site.register(Adoption,AdoptionAdmin) 