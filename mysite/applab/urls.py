from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hello/', views.hello),
    path('nice/', views.nice),
]