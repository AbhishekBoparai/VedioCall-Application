from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('videocall/',views.videocall, name='videocall'),
    path('logout/',views.logout_view, name='logout'),
    path('join/',views.join_room, name='join'),
    path('',views.index,name='index'),
   

]