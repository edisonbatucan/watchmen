from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreateForm, CustomUserUpdateForm
from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreateForm
#     form = CustomUserUpdateForm
#     model = CustomUser
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password', 're_password', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)


# Register your models here.
admin.site.register(CustomUser)