from django.urls import path
from home.views import weather

urlpatterns = [
    path('weather/', weather, name='weather'),
    # Add other URL patterns as needed
]
