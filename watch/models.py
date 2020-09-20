from django.db import models

# Create your models here.
# class Brand(models.Model):
#     name = models.CharField(max_length=50)
#     img = models.ImageField()

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = "Brand"

class Watch(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    have_stock = models.BooleanField(default=True)
    description = models.CharField(max_length=1000)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Watch"
