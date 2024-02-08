"""food_delivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Menu.views import * 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',homepage,name='home'),
    path('restaurant/<id>',Menu,name='home'),
    path('login/',login_page,name='login'),
    path('cart/',cart,name='cart'),
    path('card_btn/',card_btn,name='card_btn'),
    path('logout/',logout_page,name='logout'),
    path('register/',register,name='register'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
s=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(s)