from django.shortcuts import render

# Create your views here.
def menu_options (request):
    return render(request , 'first_menu.html')
