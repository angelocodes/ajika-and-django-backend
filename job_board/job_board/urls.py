from django.urls import path

from .views import index, job_detail

urlpatterns = [
    # Define your app-specific URL patterns here
    path('', index, name='home'),
    path('job/<int:job_id>/', job_detail, name='job_detail'),
]
