from django.contrib import admin
from django.urls import path, include
from home.views import weather  # Import your app's view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', weather, name='weather'),  # Add your app's URL pattern
    # Add a URL pattern for the root URL
    path('', weather, name='root'),  # Replace `weather` with the appropriate view function
]
