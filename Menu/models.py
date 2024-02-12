from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name=models.CharField( max_length=50)
    address=models.CharField(max_length=150)
    description=models.CharField(max_length=200,null=True,blank=True)
    rating=models.FloatField()
    image=models.ImageField(upload_to='restaurant_images')
    def __str__(self):
        return self.name

class Food(models.Model):
    restaurant=models.ForeignKey(Restaurant,related_name='restaurant_name',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50)
    cost=models.FloatField()
    image=models.ImageField(upload_to='food_images')
    def __str__(self):
        return self.name

class OrderInfo(models.Model):
    costomer=models.ForeignKey(User,related_name='order_costomer_name',on_delete=models.CASCADE)
    Name=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=250,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)


class Orders(models.Model):
    orderinfo=models.ForeignKey(OrderInfo,related_name='orderinfo',on_delete=models.CASCADE)
    food=models.ForeignKey(Food,related_name='food_name',on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    total=models.FloatField(default=0)
    def __str__(self):
        return str(self.food)
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Food, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)