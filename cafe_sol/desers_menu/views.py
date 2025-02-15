from django.shortcuts import render
from .models import Deser

# Create your views here.
def menu (request):
    all_desers = Deser.objects.all()
    
    for deser in all_desers :
        deser.fee =  str(deser.fee) + ',000'  
        
    return render (request , 'deser_menu.html' , {'deser': all_desers})
# def Deser (request):
#     all_desers = Deser.objects.all()
    
#     for deser in all_desers :
#         deser.fee =  str(deser.fee) + ',000'  
        
#     return render (request , 'deser_menu.html' , {'deser': all_desers})