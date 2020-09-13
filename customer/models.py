# from django.db import models
# from django.contrib.auth.models import User
# from watch.models import Watch

# # Create your models here.
# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# class Review(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
#     content = models.CharField(max_length=200)
#     star = models.IntegerField()

