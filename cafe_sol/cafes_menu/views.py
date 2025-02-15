from django.shortcuts import render
from .models import Cafe

# Create your views here.
def menu (request):
    all_cafe = Cafe.objects.all()
    
    for cafe in all_cafe :
        cafe.fee =  str(cafe.fee) + ',000'  
    return render (request , 'cafe_menu.html' , {'cafe' : all_cafe})
