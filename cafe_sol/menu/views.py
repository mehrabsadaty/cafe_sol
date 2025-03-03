from django.shortcuts import render
from .models import Cafe, Deser
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'menu/first_menu.html')


class CoffeesView(View):
    def get(self, request):
        coffees = Cafe.objects.all()  
        
        for cafe in coffees :
            cafe.price = str(cafe.price) + ',000'
        return render(request, 'menu/cafe_menu.html' , {'cafe' : coffees})
    
class DessertsView(View):
    def get(self, request):
        all_desers = Deser.objects.all()
        
        for deser in all_desers :
            deser.price = str(deser.price) + ',000'
        return render (request , 'menu/deser_menu.html' , {'deser': all_desers})
