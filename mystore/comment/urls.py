from django.urls import path
from . import views

app_name='comment'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('list_comment/', views.list_comment, name='list_comment'),
    path('', views.index, name='index'),  
    path('update_comment/<int:pk>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:pk>', views.delete_comment, name='delete_comment'),   
]