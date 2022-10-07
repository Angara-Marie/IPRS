from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','middle_name', 'last_name', 'age')
    search_fields = ('first_name', 'middle_name','last_name')
admin.site.register(Customer, CustomerAdmin) 
