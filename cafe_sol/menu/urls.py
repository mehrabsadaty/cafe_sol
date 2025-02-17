from django.urls import path , include
from .views import CoffeesView, DessertsView

app_name = 'menu'
urlpatterns = [
    path ('' , DessertsView.as_view(), name='dessert'),
    path ('cafe/' , CoffeesView.as_view(), name='cafe'),
    path ('dessert/' , DessertsView.as_view(), name='dessert'),
]
