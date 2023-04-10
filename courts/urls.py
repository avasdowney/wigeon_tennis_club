from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='index'),
    #Court 1
    path('reservationform/1/1', views.c1t1, name='form'),
    path('reservationform/1/2', views.c1t2, name='form'),
    path('reservationform/1/3', views.c1t3, name='form'),
    path('reservationform/1/4', views.c1t4, name='form'),
    path('reservationform/1/5', views.c1t5, name='form'),
    path('reservationform/1/6', views.c1t6, name='form'),
    #Court 2
    path('reservationform/2/1', views.c2t1, name='form'),
    path('reservationform/2/2', views.c2t2, name='form'),
    path('reservationform/2/3', views.c2t3, name='form'),
    path('reservationform/2/4', views.c2t4, name='form'),
    path('reservationform/2/5', views.c2t5, name='form'),
    path('reservationform/2/6', views.c2t6, name='form'),
    #Court 3
    path('reservationform/3/1', views.c3t1, name='form'),
    path('reservationform/3/2', views.c3t2, name='form'),
    path('reservationform/3/3', views.c3t3, name='form'),
    path('reservationform/3/4', views.c3t4, name='form'),
    path('reservationform/3/5', views.c3t5, name='form'),
    path('reservationform/3/6', views.c3t6, name='form'),
    #Court 4
    path('reservationform/4/1', views.c4t1, name='form'),
    path('reservationform/4/2', views.c4t2, name='form'),
    path('reservationform/4/3', views.c4t3, name='form'),
    path('reservationform/4/4', views.c4t4, name='form'),
    path('reservationform/4/5', views.c4t5, name='form'),
    path('reservationform/4/6', views.c4t6, name='form'),
    #Court 5
    path('reservationform/5/1', views.c5t1, name='form'),
    path('reservationform/5/2', views.c5t2, name='form'),
    path('reservationform/5/3', views.c5t3, name='form'),
    path('reservationform/5/4', views.c5t4, name='form'),
    path('reservationform/5/5', views.c5t5, name='form'),
    path('reservationform/5/6', views.c5t6, name='form'),
    #Court 6
    path('reservationform/6/1', views.c6t1, name='form'),
    path('reservationform/6/2', views.c6t2, name='form'),
    path('reservationform/6/3', views.c6t3, name='form'),
    path('reservationform/6/4', views.c6t4, name='form'),
    path('reservationform/6/5', views.c6t5, name='form'),
    path('reservationform/6/6', views.c6t6, name='form'),
    #Court 7
    path('reservationform/7/1', views.c7t1, name='form'),
    path('reservationform/7/2', views.c7t2, name='form'),
    path('reservationform/7/3', views.c7t3, name='form'),
    path('reservationform/7/4', views.c7t4, name='form'),
    path('reservationform/7/5', views.c7t5, name='form'),
    path('reservationform/7/6', views.c7t6, name='form'),
    #Court 8
    path('reservationform/8/1', views.c8t1, name='form'),
    path('reservationform/8/2', views.c8t2, name='form'),
    path('reservationform/8/3', views.c8t3, name='form'),
    path('reservationform/8/4', views.c8t4, name='form'),
    path('reservationform/8/5', views.c8t5, name='form'),
    path('reservationform/8/6', views.c8t6, name='form'),
    #Court 9
    path('reservationform/9/1', views.c9t1, name='form'),
    path('reservationform/9/2', views.c9t2, name='form'),
    path('reservationform/9/3', views.c9t3, name='form'),
    path('reservationform/9/4', views.c9t4, name='form'),
    path('reservationform/9/5', views.c9t5, name='form'),
    path('reservationform/9/6', views.c9t6, name='form'),
    #Court 10
    path('reservationform/10/1', views.c10t1, name='form'),
    path('reservationform/10/2', views.c10t2, name='form'),
    path('reservationform/10/3', views.c10t3, name='form'),
    path('reservationform/10/4', views.c10t4, name='form'),
    path('reservationform/10/5', views.c10t5, name='form'),
    path('reservationform/10/6', views.c10t6, name='form'),
    #Court 11
    path('reservationform/11/1', views.c11t1, name='form'),
    path('reservationform/11/2', views.c11t2, name='form'),
    path('reservationform/11/3', views.c11t3, name='form'),
    path('reservationform/11/4', views.c11t4, name='form'),
    path('reservationform/11/5', views.c11t5, name='form'),
    path('reservationform/11/6', views.c11t6, name='form'),
    #Court 12
    path('reservationform/12/1', views.c12t1, name='form'),
    path('reservationform/12/2', views.c12t2, name='form'),
    path('reservationform/12/3', views.c12t3, name='form'),
    path('reservationform/12/4', views.c12t4, name='form'),
    path('reservationform/12/5', views.c12t5, name='form'),
    path('reservationform/12/6', views.c12t6, name='form'),


]