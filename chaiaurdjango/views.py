from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   return render(request, 'index.html', {'name': 'Chai'})

def about(request):
   return render(request, 'about.html', {'name': 'about'})

def contact(request):
    return render(request, 'contact.html', {'name': 'contact'})