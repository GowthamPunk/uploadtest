from django.urls import path
from . import views

urlpatterns = [
    path('',views.newsapp,name='newsapp')
]