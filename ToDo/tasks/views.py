from django.shortcuts import render
from tasks.models import task, hashtag
from django.views import generic

class Task(generic.ListView):
    model = task
