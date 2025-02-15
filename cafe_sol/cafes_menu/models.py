from django.db import models

# Create your models here.
class Cafe (models.Model):
    cafe_name = models.CharField(max_length=50)
    cafe_describtion = models.TextField(default='', null=True , blank=True)
    fee = models.BigIntegerField(default=0)