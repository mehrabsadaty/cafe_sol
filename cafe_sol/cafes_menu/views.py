from django.shortcuts import render
from .models import Cafe
from django.db import models

class Menu(models.Model):
    def get(request):
        coffees = Cafe.objects.all()
        
        for cafe in coffees :
            cafe.fee =  str(cafe.fee) + ',000'  
        return render (request , 'cafes_menu/cafe_menu.html' , {'cafe' : coffees})
