from django.contrib import admin
from .models import Customer,Review
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','user_type']

    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
    
    def email(self,obj):
        return obj.user.email
    
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Review)