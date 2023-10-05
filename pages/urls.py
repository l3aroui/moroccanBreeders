from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('register',views.user_register,name='register'),
    path('login', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('breeders_dashboard/',views.breeders_dashboard,name='breeders_dashboard'),
    path('profile',views.user_profile,name='profile')
    ]
