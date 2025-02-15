from django.db import models

# Create your models here.
class Deser (models.Model):
    deser_name = models.CharField(max_length=50)
    deser_description = models.TextField(default='', null=True , blank=True)
    fee = models.BigIntegerField(default=0)
