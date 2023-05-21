from django.contrib import admin
from .models import Expense, Catagory

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display=('amount','description','owner','catagory', 'date')
    search_field=('amount','description','owner','catagory')


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Catagory)



