from django import views
from django.urls import path

urlpatterns = [

    path('add',views.add,name='add'),
    ]