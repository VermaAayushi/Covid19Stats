from django.shortcuts import render
from django.http import HttpResponse
from .models import Resources

# Create your views here.

def home(request):
    resources = Resources.objects.all()
    return render(request,'stats/home.html',{'resources':resources})

def stats(request):
    return render(request, 'stats/stats.html')


def graphs(request):
    return render(request, 'stats/graphs.html')


def check(request):
    return render(request, 'stats/check.html')



