from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.check_status, name='status'),
    path('hello/<str:name>/', views.say_hello, name='hello'),
    path('bye/<str:name>/', views.say_bye, name='bye'),
]