from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return redirect(car_control_panel)

def car_console(request, file_type = 'html'):
    if file_type == 'html':
        return render(request, 'templates/console.html')
    else:
        return render(request, 'templates/css/core.css')
