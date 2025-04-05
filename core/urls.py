from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define the view function directly in urls.py
def index_view(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('', index_view),  # Use a different name to avoid conflicts
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
]