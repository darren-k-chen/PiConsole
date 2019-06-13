from django.shortcuts import render, redirect
from django.http import HttpResponse

"""
 * |==================================================|
 * |======This code created by K.J. Chen(陳冠儒)======|
 * |=Copyright © 2019 K.J. Chen | All Rights Reserved=|
 * |==================================================|
"""

def index(request):
    return redirect(car_console)

def car_console(request):
    return render(request, 'console.html')

def car_console_css(request):
    return render(request, 'css/core.css')
