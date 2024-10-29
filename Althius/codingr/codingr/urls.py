# codingr/urls.py (or the main urls.py file for your Django project)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('usersystem.urls')),  # Replace 'your_app_name' with the actual name of your app
]
