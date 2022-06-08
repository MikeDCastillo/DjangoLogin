from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#  Function based view
def taskList(request): 
    return HttpResponse('To Do list')
