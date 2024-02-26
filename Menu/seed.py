from .models import *
from faker import Faker
import random, os
from django.conf import settings

fake = Faker()

def create_restaurants():
    names = ["Taj Mahal Indian Restaurant", "Spice Route", "Curry House", "Masala Kitchen", "Namaste India"]
    image_folder_path = os.path.join(settings.BASE_DIR, 'media/restaurant_images')
    image_files = os.listdir(image_folder_path)
    num_images = len(image_files)
    for i, name in enumerate(names):
        address = fake.address()
        description = fake.text(max_nb_chars=200)
        rating = round(random.uniform(3, 5), 1)
        image_file_name = image_files[i % num_images]  # Ensure cycling through available images
        image_path = f'restaurant_images/{image_file_name}'  # Relative path to the image
        restaurant = Restaurant.objects.create(
            name=name, 
            address=address, 
            description=description, 
            rating=rating, 
            image=image_path)
        restaurant.save()

def create_categories():
    Names=["Fish",'Rice','Chicken','Mutton','Veg','Paratha','Non-veg',]
    for category_name in Names:
        category = Category.objects.create(catagory=category_name)
        category.save()


def create_foods(num):
    if not Category.objects.exists():
        create_categories()  # Create 5 random categories if none exist

    if not Restaurant.objects.exists():
        create_restaurants()  # Create 3 random restaurants if none exist

    restaurants = Restaurant.objects.all()
    categories = Category.objects.all()
    for _ in range(num):
        restaurant = random.choice(restaurants)
        name = fake.name()
        category = random.choice(categories)
        cost = round(random.uniform(5, 50), 2)
        image = 'food_images/default.jpg'  # Default image path
        food = Food.objects.create(restaurant=restaurant, name=name, catagory=category, cost=cost, image=image)
        food.save()

def reset():
    Food.objects.all().delete()
    Category.objects.all().delete()
    Restaurant.objects.all().delete()
  
def create_all(food):
    create_restaurants()
    create_categories()
    create_foods(food)