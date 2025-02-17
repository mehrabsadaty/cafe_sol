from django.shortcuts import render
from .models import Cafe, Deser
from django.views import View



class HomeView(View):
    def get(request):
        return render(request, 'menu/first_menu.html')


class CoffeesView(View):
    def get(request):
        coffees = Cafe.objects.all()
        
        for cafe in coffees :
            cafe.fee =  str(cafe.fee) + ',000'  
        return render (request , 'menu/cafe_menu.html' , {'cafe' : coffees})
    
class DessertsView(View):
    def get(request):
        all_desers = Deser.objects.all()
    
        for deser in all_desers :
            deser.fee =  str(deser.fee) + ',000'  
            
        return render (request , 'menu/deser_menu.html' , {'deser': all_desers})
