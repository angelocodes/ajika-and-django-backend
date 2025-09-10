from django.urls import path

from .views import index

urlpatterns = [
    # Define your app-specific URL patterns here
    path('', index)
]
