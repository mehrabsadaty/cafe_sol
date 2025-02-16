from django.shortcuts import render
from .models import Cafe
from django.views import View

class Menu(View):
    def get(request):
        coffees = Cafe.objects.all()
        
        for cafe in coffees :
            cafe.fee =  str(cafe.fee) + ',000'  
        return render (request , 'menu/cafe_menu.html' , {'cafe' : coffees})
