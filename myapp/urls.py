
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('add/',views.form_create,name='form_create'),
    path('<int:pk>/',views.form,name='form'),
    path('ajax/load_course',views.load_course,name='ajax_load_course'),
    path('confirm/',views.confirm,name='confirm'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home')
]
