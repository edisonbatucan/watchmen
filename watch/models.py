# from django.db import models

# # Create your models here.
# class Brand(models.Model):
#     name = models.CharField(max_length=50)

# class Watch(models.Model):
#     name = models.CharField(max_length=100)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     have_stock = models.BooleanField(default=True)
#     description = models.CharField(max_length=1000)
