from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Count

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
    if request.method=='POST':
        print('hi')
    foods=Food.objects.filter(restaurant__id=id)
    restaurant=Restaurant.objects.filter(id=id)
    restaurant=restaurant[0]
    cart_items = {}
    user=request.user
    if user.is_authenticated:
        cart = user.cart
        cart_items_query = CartItem.objects.filter(cart=cart)
        for item in cart_items_query:
            cart_items[item.food_id] = item.quantity 

    foods={'foods':foods,'restaurant':restaurant,'cart_items':cart_items}
    return render(request,'menu.html',foods,)


def homepage(request):
    restaurants=Restaurant.objects.all()
    restaurants={'restaurants':restaurants}
    return render(request,'index.html',restaurants)

def cart(request):
    user = request.user
    try:
        cart_items = CartItem.objects.filter(cart__user=user)
    except Cart.DoesNotExist:
        # Create a new Cart object for the user and save it
        new_cart = Cart.objects.create(user=request.user)
        new_cart.save()
        cart_items = CartItem.objects.filter(cart__user=user)
    return render(request, 'cart.html', {'item': cart_items})

def card_btn(request):
    # Your function logic here
    # For example, you can print a message
    print("Button clicked!")
    return JsonResponse({'status': 'success'})

@login_required(login_url="/login/")
def order_page(request):
    return render(request,'order.html')