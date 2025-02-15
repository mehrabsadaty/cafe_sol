from django.urls import path
from .views import menu_options

urlpatterns = [
    path('' , menu_options)
]
