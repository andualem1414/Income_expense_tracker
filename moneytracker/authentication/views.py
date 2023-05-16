from django.shortcuts import redirect, render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages, auth
from django.contrib.auth import authenticate



# Create your views here.

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email format not correct'}, status=400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry email exists, Try new one.'}, status=409)

        return JsonResponse({'email_valid':True})
    
    
class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry username exists, Try new one.'}, status=409)

        return JsonResponse({'username_valid':True})
    

class RegistrationView(View):

    def get(self, request):
        return render(request, "authentication/register.html")
    

    def post(self, request):
        # get user data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            "fieldValue":request.POST
        }
        # validate


        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, "Password too short, Must be 6 characters")
                    return render(request, "authentication/register.html", context)
                
                # create user account
                
                user = User.objects.create_user(username=username,email=email)
                user.set_password(password)
                user.save()
                
                messages.success(request, "Account successfully created")
                return redirect("login")


        
       
        return render(request, "authentication/register.html")
    

class LoginView(View):
    def get(self, request):
        return render(request, "authentication/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        if username and password:
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                auth.login(request, user)
                messages.success(request, "Wellcome Home my G")
                return redirect("expenses")
            
            messages.error(request, "Wrong credentials")
            return render(request, "authentication/login.html")
        
        messages.error(request, "Please fill all fields")
        return render(request, "authentication/login.html")
    
class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, "You have been logged out")
        return redirect("login")
