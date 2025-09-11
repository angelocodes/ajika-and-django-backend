from django.shortcuts import render, get_object_or_404
from .models import JobPosting

# Create your views here.

def index(request):
    active_postings = JobPosting.objects.all()
    context = {
        'job_postings': active_postings
    }
    return render(request, 'job_board/index.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
   # try:
   #     job = JobPosting.objects.get_o(id=job_id)
    context = {
            'job': job
        }
    return render(request, 'job_board/job_detail.html', context)
   # except JobPosting.DoesNotExist:
   #     return HttpResponse("Job not found", status=404)