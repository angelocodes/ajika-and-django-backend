from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Link
from .forms import LinkForm

# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        'links': links
    }
    return render(request, 'lishorty/index.html', context)

def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.increment_clicks()
    return redirect(link.url)

def add_link(request):
    if request.method == 'POST':
        #form has data
        form = LinkForm(request.POST)
        if form.is_valid():
            #save the form data and return user to home page
            form.save()
            return redirect(reverse('home'))


            #process the data
            #print(form.cleaned_data)
            #name = form.cleaned_data['name']
            #url = form.cleaned_data['url']
            #slug = form.cleaned_data['slug']
            #link = Link(name=name, url=url, slug=slug)
            #link.save()
            #return redirect('home')
    else:
        #empty form
        form = LinkForm()

    context = {
        'form': form
    }
    return render(request, 'lishorty/create.html', context)