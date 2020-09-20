from django.urls import path
from .views import CustomerDashboardView, CustomerRegisterView

urlpatterns = [
    path('', CustomerDashboardView.as_view(), name="customer_index"),
    path('register', CustomerRegisterView.as_view(), name="customer_reg"),
]