from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.check_status, name='status'),
    path('hello/', views.say_hello, name='hello'),
]