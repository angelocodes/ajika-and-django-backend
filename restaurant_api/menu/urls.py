from django.urls import path
from .views import item_list, item_list_serialized, item_detail, menu_ui

urlpatterns = [
    path('', item_list, name='item_list'),
    path('serialized/', item_list_serialized, name='item_list_serialized'),
    path('detail/<int:pk>/', item_detail, name='item_detail'),
    path('ui/', menu_ui, name='menu_ui'),
]
