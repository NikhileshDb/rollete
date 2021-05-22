from django.urls import path
from .views import *


urlpatterns = [
    path('', add_numbers, name='add_number'),
    path('save_number', save_number, name='save_number'),
    path('del_number', del_number, name='del_number'),
    path('rol/', rol, name='rol'),
    path('register/', register, name='register'),
]