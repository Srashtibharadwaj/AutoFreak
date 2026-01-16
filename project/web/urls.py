from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('user_dashboard',views.user_dashboard,name='user_dashboard'),
    path('user_booking',views.user_booking,name='user_booking'),
    path('user_changepassword',views.user_changepassword,name='user_changepassword'),
    path('user_editprofile',views.user_editprofile,name='user_editprofile'),
    path('user_lasttrip',views.user_lasttrip,name='user_lasttrip'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('admin_addedoffers',views.admin_addedoffers,name='admin_addedoffers'),
    path('admin_car',views.admin_car,name='admin_car'),
    path('admin_employees',views.admin_employees,name='admin_employees'),
    path('admin_changepassword',views.admin_changepassword,name='admin_changepassword'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    
    
    
    
    
    

    
    
    
]
