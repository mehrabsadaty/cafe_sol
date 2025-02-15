from django.urls import path , include
from .views import menu

app_name = 'cafes_menu'
urlpatterns = [
    path ('cafe/' , menu, name='cafe')
]
