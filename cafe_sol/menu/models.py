from django.db import models


class Cafe(models.Model):
    name = models.CharField(max_length=50)
    describtion = models.TextField(null=True , blank=True)
    price = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Deser(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True , blank=True)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
