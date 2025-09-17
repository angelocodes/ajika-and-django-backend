from django.urls import path
from .views import HomeView, NoteCreateView, NoteDeleteView, NoteUpdateView, TripCreateView, TripDeleteView, TripDetailView, TripUpdateView, trip_list

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', trip_list, name='trip-list'),
    path('dashboard/trip/create', TripCreateView.as_view(), name='trip-create'),
    path('dashboard/trip/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    path('dashboard/trip/<int:pk>/note/create', NoteCreateView.as_view(), name='note-create'),
    path('dashboard/note/<int:pk>/edit', NoteUpdateView.as_view(), name='note-edit'),
    path('dashboard/trip/<int:pk>/edit', TripUpdateView.as_view(), name='trip-edit'), 
    path('dashboard/trip/<int:pk>/delete', TripDeleteView.as_view(), name='trip-delete'),
    path('dashboard/note/<int:pk>/delete', NoteDeleteView.as_view(), name='note-delete'),
]