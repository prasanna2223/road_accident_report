from django.urls import path
from .views import signup_view,user_login_view, admin_login_view, logout_view
from django.shortcuts import redirect
from . import views
urlpatterns = [
    path('login/', views.user_login_view, name='user_login'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('register/', views.signup_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

]
