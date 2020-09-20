from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'address',
            'email',
        )

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'address',
            'email',
        )