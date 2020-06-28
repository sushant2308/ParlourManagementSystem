from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('adminlogin/', views.adminl, name='adminlogin'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('profile/', views.profile, name='profile'),
    path('addser/', views.addser, name='addser'),
    path('appointment/', views.appointment, name='appointment'),
    path('viewappo/', views.viewappo, name='viewappo'),
    path('accept/<int:pk>', views.Accept, name='Accept'),
    path('decline/<int:pk>', views.Decline, name='Decline'),
    
]