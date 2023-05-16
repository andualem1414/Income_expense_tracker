from typing import Any
from django.shortcuts import render, redirect
import os 
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages
from django.views import View
# Create your views here.

class UserPereferencesView(View):    

    def get(self, request):
        exists = UserPreferences.objects.filter(user=request.user).exists()

        currency_data = []

        file_path = os.path.join(settings.BASE_DIR, "currencies.json")
        if exists:
            default = UserPreferences.objects.get(user=request.user).currency
        else:
            default = "Choose..."


        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

            for k, v in data.items():
                currency_data.append({'name': k, 'value': v})
        # import pdb
        # pdb.set_trace()

        return render(request, "preferences/index.html", {'currencies':currency_data, 'user_preferences': default})

    def post(self, request):
        exists = UserPreferences.objects.filter(user=request.user).exists()
        user_preferences = None

        if exists:
            user_preferences = UserPreferences.objects.get(user=request.user)

        currency = request.POST['currency']

        if exists:
            user_preferences.currency = currency
            user_preferences.save()
        else:
            UserPreferences.objects.create(user= request.user, currency=currency)

        messages.success(request, "Changes Saved")
        return redirect("preferences")



