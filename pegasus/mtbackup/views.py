from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. Du bist im mtbackup index.")

def get_backup(request):
    return HttpResponse("Das ist der get_backup view.")
