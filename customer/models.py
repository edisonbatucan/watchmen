from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
# from watch.models import Watch
from .managers import CustomBaseManager

# Create your models here.
class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]

    username = None
    email = models.EmailField(unique = True)
    date_of_birth = models.DateField(blank = True, null = True)
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    address = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 15, null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    objects = CustomBaseManager()

    @property
    def name(self):
        return ''.join([self.last_name, ', ', self.first_name])

    @property
    def age(self):
        age = int((date.today() - self.date_of_birth).days / 365.2425)
        return age

    def __str__(self):
        return self.email

    class Meta:
        db_table = "User"

# class Review(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
#     content = models.CharField(max_length=200)
#     star = models.IntegerField()
