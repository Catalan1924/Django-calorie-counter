from django.urls import path
from . import views
urlpatterns = [
path('',           views.dashboard, name='dashboard'),
path('add/',       views.add_food,  name='add_food'),
path('delete/int:pk/', views.delete_food, name='delete_food'),
path('reset/',     views.reset_day, name='reset_day'),
path('add/', views.add_food, name='add_food')
]