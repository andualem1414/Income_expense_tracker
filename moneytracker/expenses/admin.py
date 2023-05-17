from django.contrib import admin
from .models import Expense, Catagory

# Register your models here.


admin.site.register(Expense)
admin.site.register(Catagory)