from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('singup', views.singup, name="singup"),
    path('sistema/', views.sistema, name="sistema"),
]
