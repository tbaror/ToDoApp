from django.shortcuts import render
from .models import List

# Create your views here.

def home(request):
    all_item = List.objects.all
    return render(request ,'home.html', {'all_item':all_item})


def about(request):
    return render(request ,'about.html', {})    
