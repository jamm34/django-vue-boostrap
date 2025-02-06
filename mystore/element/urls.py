from django.urls import path
from . import views

app_name='element'

urlpatterns = [
    path('/add', views.add, name='add'),
    path('/add2', views.add2, name='add2'),
    path('/', views.index, name='index'),
     
]