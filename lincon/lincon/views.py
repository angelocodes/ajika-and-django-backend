from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView


from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):

    model = Link
    #template called model_link.html, so we create -> link_list.html
    context_object_name = 'object_list' #default is object_list
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')  # <-- use get() instead of []
        if slug:
            self.profile = get_object_or_404(Profile, slug=slug)
        else:
            # default to first profile in DB (or whatever logic you want)
            self.profile = Profile.objects.first()
        return self.profile.links.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile #add profile to context so that we can access it in template  
        return context


class LinkCreateView(CreateView):
    #auto creates a template model_form.html -> link_form.html
    model = Link
    fields = ['text', 'url']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            context['profile'] = get_object_or_404(Profile, slug=slug)
        return context

    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        profile = get_object_or_404(Profile, slug=slug)
        form.instance.profile = profile
        return super().form_valid(form)

    def get_success_url(self):
        # Use the link's profile slug
        return reverse_lazy('link-list', kwargs={'slug': self.object.profile.slug})

class LinkUpdateView(UpdateView):
    model = Link
    fields = ['text', 'url']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object.profile
        return context

    def get_success_url(self):
        return reverse_lazy('link-list', kwargs={'slug': self.object.profile.slug})

class LinkDeleteView(DeleteView):
    model = Link
    #expects a template called model_confirm_delete.html -> link_confirm_delete.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object.profile
        return context

    def get_success_url(self):
        return reverse_lazy('link-list', kwargs={'slug': self.object.profile.slug})

    #or we can use success_url = reverse_lazy('link-list') if we dont want to redirect to specific profile

def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links': links,
    }
    return render(request, 'lincon/profile.html', context)
