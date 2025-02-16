from django.urls import path , include
from .views import Menu

app_name = 'menu'
urlpatterns = [
    path ('cafe/' , Menu.as_view(), name='cafe'),
]
