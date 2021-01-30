from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Job


class JobList(ListView):
    model = Job
    template_name = 'careers.html'
    context_object_name = 'jobs'

