from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView
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

class TripCreateView(CreateView):
    model = Trip
    fields = ['city', 'country', 'start_date', 'end_date']
    # looks for template named model_form.html -> trip_form.html
    success_url = reverse_lazy('trip-list')

    def form_valid(self, form):
        # Assign the logged-in user as the owner of the trip
        form.instance.owner = self.request.user
        return super().form_valid(form)
    


class TripDetailView(DetailView):
    model = Trip

    # data stored on Trip - also have the notes data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()  # Access related notes using the related_name
        context['notes'] = notes
        return context