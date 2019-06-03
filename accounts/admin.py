from django.contrib import admin
from .models import Customer, Profile

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'status']
    list_editable = ['status']

    class Meta:
        model = Customer

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Profile)