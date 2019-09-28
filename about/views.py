from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from about.models import Job


def index(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs
    }
    return render(request, 'about/index.html', context)
