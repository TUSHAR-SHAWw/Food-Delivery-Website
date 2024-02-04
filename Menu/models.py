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

class Orders(models.Model):
    food=models.ForeignKey(Food,related_name='food_name',on_delete=models.CASCADE)
    costomer=models.ForeignKey(User,related_name='costomer_name',on_delete=models.CASCADE)
    location=models.CharField(max_length=250,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.costomer)
    
class Cart(models.Model):
    food=models.ForeignKey(Food,related_name='cart_food',on_delete=models.CASCADE)
    costomer=models.ForeignKey(User,related_name='cart_costomer',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.food)