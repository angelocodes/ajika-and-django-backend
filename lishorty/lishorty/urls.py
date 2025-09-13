from django.urls import path, include
from .views import index, root_link, add_link

urlpatterns = [
    path('', index, name='home'),
    path('create/', add_link, name='create-link'),
    path('<str:link_slug>/', root_link, name='root-link'),
    
]