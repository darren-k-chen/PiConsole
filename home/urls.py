from django.urls import path
from . import views
from home.car_control import run

car_run = run.CarRun()

car_run.motor_init()

urlpatterns = [
    path('', views.index, name = 'index'),
    path('car_run/', views.car_console, name = "car_control_panel"),
    path('car_run/css_core/', views.car_console_css, name = "car_control_panel_css"),
    path('car_run/advance/', car_run.advance, name = 'go_advance'),
    path('car_run/back/', car_run.back, name = 'go_back'),
    path('car_run/left/', car_run.left, name = 'turn_left'),
    path('car_run/right/', car_run.right, name = 'turn_right'),
    path('car_run/situ_left/', car_run.situ_left, name = 'turn_left_in_situ'),
    path('car_run/situ_right/', car_run.situ_right, name = 'turn_right_in_situ'),
    path('car_run/stop_run/', car_run.stop_run, name = 'make_car_to_stop'),
    path('car_run/end_control/', car_run.all_stop, name = 'end_control'),
]

try:
    pass
except:
    car_run.stop()
