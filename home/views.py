from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return redirect(car_console)

def car_console(request):
    return render(request, 'console.html')

def car_console_css(request):
    return render(request, 'css/core.css')
