from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
           messages.info(request, "Incorrect Username")
           return redirect("/login/")
        user= authenticate(request, username=username,password=password)
        if user is None:
            print(f"Login failed for username: {username} with password: {password} ,{user}")
            messages.info(request, "Incorrect Password")
            return redirect("/login/")
        else:
            login(request,user)
            context={"user":user}
            return redirect("/",context)
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect("/login")

def register(request):
    if request.method=='POST':

        name= request.POST.get("username")
        email = request.POST.get("email")
        username= request.POST.get("email")
        password = request.POST.get("password")
        user= User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "This email is already registered.")
            return redirect("/register/")
        new_user=User.objects.create_user(
            username=username,
            first_name=name,
            email=email,
            password=password
        )
        messages.success(request, "You're registered.")
    return render(request,'register.html')


@login_required(login_url="/login/")
def Menu(request,id):
    foods=Food.objects.filter(restaurant__id=id)
    restaurant=Restaurant.objects.filter(id=id)
    restaurant=restaurant[0]
    foods={'foods':foods,'restaurant':restaurant}
    return render(request,'menu.html',foods,)


def homepage(request):
    restaurants=Restaurant.objects.all()
    restaurants={'restaurants':restaurants}
    return render(request,'index.html',restaurants)

def cart(request,id):
    item=Cart.objects.filter(costomer__id=id)
    item={'item':item}
    return render(request,'cart.html',item)

@login_required(login_url="/login/")
def order_page(request):
    return render(request,'order.html')