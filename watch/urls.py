from django.urls import path
from .views import WatchDashboardView, WatchRegisterView

urlpatterns = [
    path('', WatchDashboardView.as_view(), name="watch_index"),
    path('register', WatchRegisterView.as_view(), name="watch_reg"),
]