from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('about.html', views.about, name='about'),
    path('login.html', views.login, name='login'),
    path('signup.html', views.signup, name='signup'),
    path('add_member.html', views.add_member, name='add_member'),
    path('add_task.html', views.add_task, name='add_task'),
    path('all_task.html', views.all_task, name='all_task'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('all_member.html', views.all_member, name='all_member'),
    path('delete_task/<item_id>', views.delete_task, name='delete_task'),
    path('delete_membere/<item_id>', views.delete_member, name='delete_member'),

    ]
