from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from .models import Trip, Note

# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip/index.html'

def trip_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        'trips': trips
    }
    return render(request, 'trip/trip_list.html', context)

class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ['city', 'country', 'start_date', 'end_date']
    template_name = 'trip/trip_form.html'
    success_url = reverse_lazy('trip-list')

    def form_valid(self, form):
        # Assign the logged-in user as the owner of the trip
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class TripUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Trip
    fields = ['city', 'country', 'start_date', 'end_date']
    template_name = 'trip/trip_form.html'
    success_url = reverse_lazy('trip-list')

    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)

    def test_func(self):
        trip = self.get_object()
        return trip.owner == self.request.user
    


class TripDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Trip

    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)

    def test_func(self):
        trip = self.get_object()
        return trip.owner == self.request.user

    # data stored on Trip - also have the notes data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()  # Access related notes using the related_name
        context['notes'] = notes
        return context

class NoteCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Note
    fields = ['name', 'description', 'type', 'img', 'rating']
    template_name = "trip/note_form.html"

    def test_func(self):
        trip_id = self.kwargs['pk']
        trip = get_object_or_404(Trip, id=trip_id)
        return trip.owner == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip_id = self.kwargs['pk']
        trip = get_object_or_404(Trip, id=trip_id, owner=self.request.user)
        context['trip'] = trip
        return context

    def form_valid(self, form):
        trip_id = self.kwargs['pk']  # Get the trip ID from the URL
        trip = get_object_or_404(Trip, id=trip_id, owner=self.request.user)
        form.instance.trip = trip  # Associate the note with the trip
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('trip-detail', kwargs={'pk': self.object.trip.id})
    
class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['name', 'description', 'type', 'img', 'rating']
    template_name = "trip/note_form.html"

    def get_queryset(self):
        return Note.objects.filter(trip__owner=self.request.user)

    def test_func(self):
        note = self.get_object()
        return note.trip.owner == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trip'] = self.object.trip
        return context

    def get_success_url(self):
        return reverse_lazy('trip-detail', kwargs={'pk': self.object.trip.id})
    
class TripDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Trip
    template_name = 'trip/trip_confirm_delete.html'
    success_url = reverse_lazy('trip-list')

    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)

    def test_func(self):
        trip = self.get_object()
        return trip.owner == self.request.user

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'trip/note_confirm_delete.html'

    def get_queryset(self):
        return Note.objects.filter(trip__owner=self.request.user)

    def test_func(self):
        note = self.get_object()
        return note.trip.owner == self.request.user

    def get_success_url(self):
        return reverse_lazy('trip-detail', kwargs={'pk': self.object.trip.id})
