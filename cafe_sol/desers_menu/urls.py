from django.contrib import admin
from django.urls import path , include
from .views import menu , Deser
app_name = 'desers_menu'
urlpatterns = [
    path ('deser/' , menu , name = 'deser'),
    # path ('Deser/' , Deser),
    
]
