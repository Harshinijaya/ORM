from django.db import models
from django.contrib import admin
class car(models.Model):
    car_name=models.CharField(max_length=20)
    car_color=models.CharField(max_length=5)
    car_model=models.CharField(max_length=10)
    car_no=models.Integer()
    car_quality=models.CharField(max_length=30)
class carAdmin(admin.ModelAdmin):
    list_display=["car_name","car_color","car_model","car_no","car_quality"]    


