from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        mail = request.POST['email']
        password = request.POST['passwrd']
        con_password = request.POST['con_passwrd']
        if password == con_password:
            if User.objects.filter(username = mail).exists():
                return HttpResponse("User already exists")
            else:
                user = User.objects.create_user(username = mail, first_name = f_name,last_name = l_name, email = mail ,password = password)
                user.save()
                return redirect("credentials:login")
        else:
            return HttpResponse("Password is incorrect...")
    return render(request, "register.html")
def login(request):
    if request.method == "POST":
        u_name = request.POST['email']
        pwd = request.POST['passwd']
        user = auth.authenticate(username = u_name,password = pwd )
        if user  is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return HttpResponse("Invalid Response(check password or username)")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("credentials:login")