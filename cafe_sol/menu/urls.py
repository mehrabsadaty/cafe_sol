from django.urls import path
from .views import CoffeesView, DessertsView, HomeView

app_name = 'menu'
urlpatterns = [
    path ('' , HomeView.as_view(), name='home'),
    path ('cafe/' , CoffeesView.as_view(), name='cafe'),
    path ('dessert/' , DessertsView.as_view(), name='dessert'),
]
