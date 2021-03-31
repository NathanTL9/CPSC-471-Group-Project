from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clubs/', views.club, name='clubs'),
    path('events/', views.events, name='events'),
    path('announcements/', views.announcements, name='announcements'),
    path('profile/', views.profile, name='profile'),

]