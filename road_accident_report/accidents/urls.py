# accidents/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accident_list, name='acci_list'),
    path('create/', views.accident_create, name='accident_create'),
    path('update/<int:id>/', views.accident_update, name='accident_update'),
    path('delete/<int:id>/', views.accident_delete, name='accident_delete'),
]
