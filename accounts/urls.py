from django.urls import path
from . import views


#This handle all Account related url

urlpatterns = [
    path('signupaccount/',views.signupaccount, name='signupaccount'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
]