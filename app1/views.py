from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def valentine_page(request):
    return render(request, 'valentine.html')

def march8_page(request):
    return render(request, 'march8.html')