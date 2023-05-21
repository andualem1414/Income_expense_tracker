import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from expenses.models import Expense

from .models import Source, Income
from userpreferences.models import UserPreferences
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

@login_required(login_url="/authentication/login")

def index(request):
    incomes = Income.objects.filter(owner= request.user)
    currency = UserPreferences.objects.get(user=request.user).currency
    paginator = Paginator(incomes, 4)

    page_number= request.GET.get('page')
    
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        "income" :incomes,
        "page_obj": page_obj,
        "currency": currency,
    }

    return render(request, "income/index.html", context)


def search_income(request):
    if request.method == "POST":
        search_string = json.loads(request.body).get("searchText", "") 


        incomes = Income.objects.filter(
            amount__istartswith=search_string, owner=request.user) | Income.objects.filter(
            date__istartswith=search_string, owner=request.user) | Income.objects.filter(
            description__icontains=search_string, owner=request.user) | Income.objects.filter(
            source__istartswith=search_string, owner=request.user)
            
        data = incomes.values()
        
        return JsonResponse(list(data), safe=False)
    
    
def add_income(request):
    sources = Source.objects.all()
    context = {
            "sources":sources,
            "values": request.POST
        }
    if request.method == "GET":
        return render(request, 'income/add_income.html' ,context) 

    if request.method == "POST":
        amount = request.POST["amount"]
        description = request.POST["description"]
        source = request.POST["source"]
        date = request.POST["income_date"]
        
        if not amount:
            messages.error(request, "Amount is required")
            return render(request, 'income/add_income.html' , context) 
        if not description:
            messages.error(request, "description")
            return render(request, 'income/add_income.html' , context) 

        Income.objects.create(owner= request.user, amount=amount, description=description, source=source, date=date)
        messages.success(request, "Income saved successfully")


        return redirect('income')


def edit_income(request, id):
    income = Income.objects.get(pk =id)
    sources = Source.objects.all()

    context = {
            "values": income,
            "sources": sources
        }

    if request.method == "GET":
        return render(request, "income/edit_income.html", context)
    
    else:
        amount = request.POST["amount"]
        description = request.POST["description"]
        source = request.POST["source"]
        date = request.POST["income_date"]
        
        if not amount:
            messages.error(request, "Amount is required")
            return render(request, 'income/edit_income.html' , context) 
        if not description:
            messages.error(request, "description")
            return render(request, 'income/edit_income.html' , context) 

        income.amount = amount
        income.date = date
        income.source = source
        income.description = description

        income.save()

        messages.success(request, "income Updated successfully")

        return render(request, "income/edit_income.html", context)


def delete_income(request, id):
    income = Income.objects.get(pk=id)
    income.delete()

    messages.success(request, "Income deleted successfully")

    return redirect("income")