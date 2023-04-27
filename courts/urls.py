from django.urls import path
from . import views

urlpatterns = [
    #dates
    path('', views.menu, name='date1'),
    path('2', views.menu2, name='date2'),
    path('3', views.menu3, name='date3'),
    path('4', views.menu4, name='date4'),
    path('5', views.menu5, name='date5'),
    path('6', views.menu6, name='date6'),
    path('7', views.menu7, name='date7'),
    
    path('tournament/', views.tournament, name='tournamnent'),

    #Day 1
    #Court 1
    path('reservationform/1/1/1', views.d1c1t1, name='form'),
    path('reservationform/1/1/2', views.d1c1t2, name='form'),
    path('reservationform/1/1/3', views.d1c1t3, name='form'),
    path('reservationform/1/1/4', views.d1c1t4, name='form'),
    path('reservationform/1/1/5', views.d1c1t5, name='form'),
    path('reservationform/1/1/6', views.d1c1t6, name='form'),
    #Court 2
    path('reservationform/1/2/1', views.d1c2t1, name='form'),
    path('reservationform/1/2/2', views.d1c2t2, name='form'),
    path('reservationform/1/2/3', views.d1c2t3, name='form'),
    path('reservationform/1/2/4', views.d1c2t4, name='form'),
    path('reservationform/1/2/5', views.d1c2t5, name='form'),
    path('reservationform/1/2/6', views.d1c2t6, name='form'),
    #Court 3
    path('reservationform/1/3/1', views.d1c3t1, name='form'),
    path('reservationform/1/3/2', views.d1c3t2, name='form'),
    path('reservationform/1/3/3', views.d1c3t3, name='form'),
    path('reservationform/1/3/4', views.d1c3t4, name='form'),
    path('reservationform/1/3/5', views.d1c3t5, name='form'),
    path('reservationform/1/3/6', views.d1c3t6, name='form'),
    #Court 4
    path('reservationform/1/4/1', views.d1c4t1, name='form'),
    path('reservationform/1/4/2', views.d1c4t2, name='form'),
    path('reservationform/1/4/3', views.d1c4t3, name='form'),
    path('reservationform/1/4/4', views.d1c4t4, name='form'),
    path('reservationform/1/4/5', views.d1c4t5, name='form'),
    path('reservationform/1/4/6', views.d1c4t6, name='form'),
    #Court 5
    path('reservationform/1/5/1', views.d1c5t1, name='form'),
    path('reservationform/1/5/2', views.d1c5t2, name='form'),
    path('reservationform/1/5/3', views.d1c5t3, name='form'),
    path('reservationform/1/5/4', views.d1c5t4, name='form'),
    path('reservationform/1/5/5', views.d1c5t5, name='form'),
    path('reservationform/1/5/6', views.d1c5t6, name='form'),
    #Court 6
    path('reservationform/1/6/1', views.d1c6t1, name='form'),
    path('reservationform/1/6/2', views.d1c6t2, name='form'),
    path('reservationform/1/6/3', views.d1c6t3, name='form'),
    path('reservationform/1/6/4', views.d1c6t4, name='form'),
    path('reservationform/1/6/5', views.d1c6t5, name='form'),
    path('reservationform/1/6/6', views.d1c6t6, name='form'),
    #Court 7
    path('reservationform/1/7/1', views.d1c7t1, name='form'),
    path('reservationform/1/7/2', views.d1c7t2, name='form'),
    path('reservationform/1/7/3', views.d1c7t3, name='form'),
    path('reservationform/1/7/4', views.d1c7t4, name='form'),
    path('reservationform/1/7/5', views.d1c7t5, name='form'),
    path('reservationform/1/7/6', views.d1c7t6, name='form'),
    #Court 8
    path('reservationform/1/8/1', views.d1c8t1, name='form'),
    path('reservationform/1/8/2', views.d1c8t2, name='form'),
    path('reservationform/1/8/3', views.d1c8t3, name='form'),
    path('reservationform/1/8/4', views.d1c8t4, name='form'),
    path('reservationform/1/8/5', views.d1c8t5, name='form'),
    path('reservationform/1/8/6', views.d1c8t6, name='form'),
    #Court 9
    path('reservationform/1/9/1', views.d1c9t1, name='form'),
    path('reservationform/1/9/2', views.d1c9t2, name='form'),
    path('reservationform/1/9/3', views.d1c9t3, name='form'),
    path('reservationform/1/9/4', views.d1c9t4, name='form'),
    path('reservationform/1/9/5', views.d1c9t5, name='form'),
    path('reservationform/1/9/6', views.d1c9t6, name='form'),
    #Court 10
    path('reservationform/1/10/1', views.d1c10t1, name='form'),
    path('reservationform/1/10/2', views.d1c10t2, name='form'),
    path('reservationform/1/10/3', views.d1c10t3, name='form'),
    path('reservationform/1/10/4', views.d1c10t4, name='form'),
    path('reservationform/1/10/5', views.d1c10t5, name='form'),
    path('reservationform/1/10/6', views.d1c10t6, name='form'),
    #Court 11
    path('reservationform/1/11/1', views.d1c11t1, name='form'),
    path('reservationform/1/11/2', views.d1c11t2, name='form'),
    path('reservationform/1/11/3', views.d1c11t3, name='form'),
    path('reservationform/1/11/4', views.d1c11t4, name='form'),
    path('reservationform/1/11/5', views.d1c11t5, name='form'),
    path('reservationform/1/11/6', views.d1c11t6, name='form'),
    #Court 12
    path('reservationform/1/12/1', views.d1c12t1, name='form'),
    path('reservationform/1/12/2', views.d1c12t2, name='form'),
    path('reservationform/1/12/3', views.d1c12t3, name='form'),
    path('reservationform/1/12/4', views.d1c12t4, name='form'),
    path('reservationform/1/12/5', views.d1c12t5, name='form'),
    path('reservationform/1/12/6', views.d1c12t6, name='form'),

    #Day 2
     #Court 1
    path('reservationform/2/1/1', views.d2c1t1, name='form'),
    path('reservationform/2/1/2', views.d2c1t2, name='form'),
    path('reservationform/2/1/3', views.d2c1t3, name='form'),
    path('reservationform/2/1/4', views.d2c1t4, name='form'),
    path('reservationform/2/1/5', views.d2c1t5, name='form'),
    path('reservationform/2/1/6', views.d2c1t6, name='form'),
    #Court 2
    path('reservationform/2/2/1', views.d2c2t1, name='form'),
    path('reservationform/2/2/2', views.d2c2t2, name='form'),
    path('reservationform/2/2/3', views.d2c2t3, name='form'),
    path('reservationform/2/2/4', views.d2c2t4, name='form'),
    path('reservationform/2/2/5', views.d2c2t5, name='form'),
    path('reservationform/2/2/6', views.d2c2t6, name='form'),
    #Court 3
    path('reservationform/2/3/1', views.d2c3t1, name='form'),
    path('reservationform/2/3/2', views.d2c3t2, name='form'),
    path('reservationform/2/3/3', views.d2c3t3, name='form'),
    path('reservationform/2/3/4', views.d2c3t4, name='form'),
    path('reservationform/2/3/5', views.d2c3t5, name='form'),
    path('reservationform/2/3/6', views.d2c3t6, name='form'),
    #Court 4
    path('reservationform/2/4/1', views.d2c4t1, name='form'),
    path('reservationform/2/4/2', views.d2c4t2, name='form'),
    path('reservationform/2/4/3', views.d2c4t3, name='form'),
    path('reservationform/2/4/4', views.d2c4t4, name='form'),
    path('reservationform/2/4/5', views.d2c4t5, name='form'),
    path('reservationform/2/4/6', views.d2c4t6, name='form'),
    #Court 5
    path('reservationform/2/5/1', views.d2c5t1, name='form'),
    path('reservationform/2/5/2', views.d2c5t2, name='form'),
    path('reservationform/2/5/3', views.d2c5t3, name='form'),
    path('reservationform/2/5/4', views.d2c5t4, name='form'),
    path('reservationform/2/5/5', views.d2c5t5, name='form'),
    path('reservationform/2/5/6', views.d2c5t6, name='form'),
    #Court 6
    path('reservationform/2/6/1', views.d2c6t1, name='form'),
    path('reservationform/2/6/2', views.d2c6t2, name='form'),
    path('reservationform/2/6/3', views.d2c6t3, name='form'),
    path('reservationform/2/6/4', views.d2c6t4, name='form'),
    path('reservationform/2/6/5', views.d2c6t5, name='form'),
    path('reservationform/2/6/6', views.d2c6t6, name='form'),
    #Court 7
    path('reservationform/2/7/1', views.d2c7t1, name='form'),
    path('reservationform/2/7/2', views.d2c7t2, name='form'),
    path('reservationform/2/7/3', views.d2c7t3, name='form'),
    path('reservationform/2/7/4', views.d2c7t4, name='form'),
    path('reservationform/2/7/5', views.d2c7t5, name='form'),
    path('reservationform/2/7/6', views.d2c7t6, name='form'),
    #Court 8
    path('reservationform/2/8/1', views.d2c8t1, name='form'),
    path('reservationform/2/8/2', views.d2c8t2, name='form'),
    path('reservationform/2/8/3', views.d2c8t3, name='form'),
    path('reservationform/2/8/4', views.d2c8t4, name='form'),
    path('reservationform/2/8/5', views.d2c8t5, name='form'),
    path('reservationform/2/8/6', views.d2c8t6, name='form'),
    #Court 9
    path('reservationform/2/9/1', views.d2c9t1, name='form'),
    path('reservationform/2/9/2', views.d2c9t2, name='form'),
    path('reservationform/2/9/3', views.d2c9t3, name='form'),
    path('reservationform/2/9/4', views.d2c9t4, name='form'),
    path('reservationform/2/9/5', views.d2c9t5, name='form'),
    path('reservationform/2/9/6', views.d2c9t6, name='form'),
    #Court 10
    path('reservationform/2/10/1', views.d2c10t1, name='form'),
    path('reservationform/2/10/2', views.d2c10t2, name='form'),
    path('reservationform/2/10/3', views.d2c10t3, name='form'),
    path('reservationform/2/10/4', views.d2c10t4, name='form'),
    path('reservationform/2/10/5', views.d2c10t5, name='form'),
    path('reservationform/2/10/6', views.d2c10t6, name='form'),
    #Court 11
    path('reservationform/2/11/1', views.d2c11t1, name='form'),
    path('reservationform/2/11/2', views.d2c11t2, name='form'),
    path('reservationform/2/11/3', views.d2c11t3, name='form'),
    path('reservationform/2/11/4', views.d2c11t4, name='form'),
    path('reservationform/2/11/5', views.d2c11t5, name='form'),
    path('reservationform/2/11/6', views.d2c11t6, name='form'),
    #Court 12
    path('reservationform/2/12/1', views.d2c12t1, name='form'),
    path('reservationform/2/12/2', views.d2c12t2, name='form'),
    path('reservationform/2/12/3', views.d2c12t3, name='form'),
    path('reservationform/2/12/4', views.d2c12t4, name='form'),
    path('reservationform/2/12/5', views.d2c12t5, name='form'),
    path('reservationform/2/12/6', views.d2c12t6, name='form'),

    #Day 3
     #Court 1
    path('reservationform/3/1/1', views.d3c1t1, name='form'),
    path('reservationform/3/1/2', views.d3c1t2, name='form'),
    path('reservationform/3/1/3', views.d3c1t3, name='form'),
    path('reservationform/3/1/4', views.d3c1t4, name='form'),
    path('reservationform/3/1/5', views.d3c1t5, name='form'),
    path('reservationform/3/1/6', views.d3c1t6, name='form'),
    #Court 2
    path('reservationform/3/2/1', views.d3c2t1, name='form'),
    path('reservationform/3/2/2', views.d3c2t2, name='form'),
    path('reservationform/3/2/3', views.d3c2t3, name='form'),
    path('reservationform/3/2/4', views.d3c2t4, name='form'),
    path('reservationform/3/2/5', views.d3c2t5, name='form'),
    path('reservationform/3/2/6', views.d3c2t6, name='form'),
    #Court 3
    path('reservationform/3/3/1', views.d3c3t1, name='form'),
    path('reservationform/3/3/2', views.d3c3t2, name='form'),
    path('reservationform/3/3/3', views.d3c3t3, name='form'),
    path('reservationform/3/3/4', views.d3c3t4, name='form'),
    path('reservationform/3/3/5', views.d3c3t5, name='form'),
    path('reservationform/3/3/6', views.d3c3t6, name='form'),
    #Court 4
    path('reservationform/3/4/1', views.d3c4t1, name='form'),
    path('reservationform/3/4/2', views.d3c4t2, name='form'),
    path('reservationform/3/4/3', views.d3c4t3, name='form'),
    path('reservationform/3/4/4', views.d3c4t4, name='form'),
    path('reservationform/3/4/5', views.d3c4t5, name='form'),
    path('reservationform/3/4/6', views.d3c4t6, name='form'),
    #Court 5
    path('reservationform/3/5/1', views.d3c5t1, name='form'),
    path('reservationform/3/5/2', views.d3c5t2, name='form'),
    path('reservationform/3/5/3', views.d3c5t3, name='form'),
    path('reservationform/3/5/4', views.d3c5t4, name='form'),
    path('reservationform/3/5/5', views.d3c5t5, name='form'),
    path('reservationform/3/5/6', views.d3c5t6, name='form'),
    #Court 6
    path('reservationform/3/6/1', views.d3c6t1, name='form'),
    path('reservationform/3/6/2', views.d3c6t2, name='form'),
    path('reservationform/3/6/3', views.d3c6t3, name='form'),
    path('reservationform/3/6/4', views.d3c6t4, name='form'),
    path('reservationform/3/6/5', views.d3c6t5, name='form'),
    path('reservationform/3/6/6', views.d3c6t6, name='form'),
    #Court 7
    path('reservationform/3/7/1', views.d3c7t1, name='form'),
    path('reservationform/3/7/2', views.d3c7t2, name='form'),
    path('reservationform/3/7/3', views.d3c7t3, name='form'),
    path('reservationform/3/7/4', views.d3c7t4, name='form'),
    path('reservationform/3/7/5', views.d3c7t5, name='form'),
    path('reservationform/3/7/6', views.d3c7t6, name='form'),
    #Court 8
    path('reservationform/3/8/1', views.d3c8t1, name='form'),
    path('reservationform/3/8/2', views.d3c8t2, name='form'),
    path('reservationform/3/8/3', views.d3c8t3, name='form'),
    path('reservationform/3/8/4', views.d3c8t4, name='form'),
    path('reservationform/3/8/5', views.d3c8t5, name='form'),
    path('reservationform/3/8/6', views.d3c8t6, name='form'),
    #Court 9
    path('reservationform/3/9/1', views.d3c9t1, name='form'),
    path('reservationform/3/9/2', views.d3c9t2, name='form'),
    path('reservationform/3/9/3', views.d3c9t3, name='form'),
    path('reservationform/3/9/4', views.d3c9t4, name='form'),
    path('reservationform/3/9/5', views.d3c9t5, name='form'),
    path('reservationform/3/9/6', views.d3c9t6, name='form'),
    #Court 10
    path('reservationform/3/10/1', views.d3c10t1, name='form'),
    path('reservationform/3/10/2', views.d3c10t2, name='form'),
    path('reservationform/3/10/3', views.d3c10t3, name='form'),
    path('reservationform/3/10/4', views.d3c10t4, name='form'),
    path('reservationform/3/10/5', views.d3c10t5, name='form'),
    path('reservationform/3/10/6', views.d3c10t6, name='form'),
    #Court 11
    path('reservationform/3/11/1', views.d3c11t1, name='form'),
    path('reservationform/3/11/2', views.d3c11t2, name='form'),
    path('reservationform/3/11/3', views.d3c11t3, name='form'),
    path('reservationform/3/11/4', views.d3c11t4, name='form'),
    path('reservationform/3/11/5', views.d3c11t5, name='form'),
    path('reservationform/3/11/6', views.d3c11t6, name='form'),
    #Court 12
    path('reservationform/3/12/1', views.d3c12t1, name='form'),
    path('reservationform/3/12/2', views.d3c12t2, name='form'),
    path('reservationform/3/12/3', views.d3c12t3, name='form'),
    path('reservationform/3/12/4', views.d3c12t4, name='form'),
    path('reservationform/3/12/5', views.d3c12t5, name='form'),
    path('reservationform/3/12/6', views.d3c12t6, name='form'),

    #Day4
     #Court 1
    path('reservationform/4/1/1', views.d4c1t1, name='form'),
    path('reservationform/4/1/2', views.d4c1t2, name='form'),
    path('reservationform/4/1/3', views.d4c1t3, name='form'),
    path('reservationform/4/1/4', views.d4c1t4, name='form'),
    path('reservationform/4/1/5', views.d4c1t5, name='form'),
    path('reservationform/4/1/6', views.d4c1t6, name='form'),
    #Court 2
    path('reservationform/4/2/1', views.d4c2t1, name='form'),
    path('reservationform/4/2/2', views.d4c2t2, name='form'),
    path('reservationform/4/2/3', views.d4c2t3, name='form'),
    path('reservationform/4/2/4', views.d4c2t4, name='form'),
    path('reservationform/4/2/5', views.d4c2t5, name='form'),
    path('reservationform/4/2/6', views.d4c2t6, name='form'),
    #Court 3
    path('reservationform/4/3/1', views.d4c3t1, name='form'),
    path('reservationform/4/3/2', views.d4c3t2, name='form'),
    path('reservationform/4/3/3', views.d4c3t3, name='form'),
    path('reservationform/4/3/4', views.d4c3t4, name='form'),
    path('reservationform/4/3/5', views.d4c3t5, name='form'),
    path('reservationform/4/3/6', views.d4c3t6, name='form'),
    #Court 4
    path('reservationform/4/4/1', views.d4c4t1, name='form'),
    path('reservationform/4/4/2', views.d4c4t2, name='form'),
    path('reservationform/4/4/3', views.d4c4t3, name='form'),
    path('reservationform/4/4/4', views.d4c4t4, name='form'),
    path('reservationform/4/4/5', views.d4c4t5, name='form'),
    path('reservationform/4/4/6', views.d4c4t6, name='form'),
    #Court 5
    path('reservationform/4/5/1', views.d4c5t1, name='form'),
    path('reservationform/4/5/2', views.d4c5t2, name='form'),
    path('reservationform/4/5/3', views.d4c5t3, name='form'),
    path('reservationform/4/5/4', views.d4c5t4, name='form'),
    path('reservationform/4/5/5', views.d4c5t5, name='form'),
    path('reservationform/4/5/6', views.d4c5t6, name='form'),
    #Court 6
    path('reservationform/4/6/1', views.d4c6t1, name='form'),
    path('reservationform/4/6/2', views.d4c6t2, name='form'),
    path('reservationform/4/6/3', views.d4c6t3, name='form'),
    path('reservationform/4/6/4', views.d4c6t4, name='form'),
    path('reservationform/4/6/5', views.d4c6t5, name='form'),
    path('reservationform/4/6/6', views.d4c6t6, name='form'),
    #Court 7
    path('reservationform/4/7/1', views.d4c7t1, name='form'),
    path('reservationform/4/7/2', views.d4c7t2, name='form'),
    path('reservationform/4/7/3', views.d4c7t3, name='form'),
    path('reservationform/4/7/4', views.d4c7t4, name='form'),
    path('reservationform/4/7/5', views.d4c7t5, name='form'),
    path('reservationform/4/7/6', views.d4c7t6, name='form'),
    #Court 8
    path('reservationform/4/8/1', views.d4c8t1, name='form'),
    path('reservationform/4/8/2', views.d4c8t2, name='form'),
    path('reservationform/4/8/3', views.d4c8t3, name='form'),
    path('reservationform/4/8/4', views.d4c8t4, name='form'),
    path('reservationform/4/8/5', views.d4c8t5, name='form'),
    path('reservationform/4/8/6', views.d4c8t6, name='form'),
    #Court 9
    path('reservationform/4/9/1', views.d4c9t1, name='form'),
    path('reservationform/4/9/2', views.d4c9t2, name='form'),
    path('reservationform/4/9/3', views.d4c9t3, name='form'),
    path('reservationform/4/9/4', views.d4c9t4, name='form'),
    path('reservationform/4/9/5', views.d4c9t5, name='form'),
    path('reservationform/4/9/6', views.d4c9t6, name='form'),
    #Court 10
    path('reservationform/4/10/1', views.d4c10t1, name='form'),
    path('reservationform/4/10/2', views.d4c10t2, name='form'),
    path('reservationform/4/10/3', views.d4c10t3, name='form'),
    path('reservationform/4/10/4', views.d4c10t4, name='form'),
    path('reservationform/4/10/5', views.d4c10t5, name='form'),
    path('reservationform/4/10/6', views.d4c10t6, name='form'),
    #Court 11
    path('reservationform/4/11/1', views.d4c11t1, name='form'),
    path('reservationform/4/11/2', views.d4c11t2, name='form'),
    path('reservationform/4/11/3', views.d4c11t3, name='form'),
    path('reservationform/4/11/4', views.d4c11t4, name='form'),
    path('reservationform/4/11/5', views.d4c11t5, name='form'),
    path('reservationform/4/11/6', views.d4c11t6, name='form'),
    #Court 12
    path('reservationform/4/12/1', views.d4c12t1, name='form'),
    path('reservationform/4/12/2', views.d4c12t2, name='form'),
    path('reservationform/4/12/3', views.d4c12t3, name='form'),
    path('reservationform/4/12/4', views.d4c12t4, name='form'),
    path('reservationform/4/12/5', views.d4c12t5, name='form'),
    path('reservationform/4/12/6', views.d4c12t6, name='form'),

    #Day 5
     #Court 1
    path('reservationform/5/1/1', views.d5c1t1, name='form'),
    path('reservationform/5/1/2', views.d5c1t2, name='form'),
    path('reservationform/5/1/3', views.d5c1t3, name='form'),
    path('reservationform/5/1/4', views.d5c1t4, name='form'),
    path('reservationform/5/1/5', views.d5c1t5, name='form'),
    path('reservationform/5/1/6', views.d5c1t6, name='form'),
    #Court 2
    path('reservationform/5/2/1', views.d5c2t1, name='form'),
    path('reservationform/5/2/2', views.d5c2t2, name='form'),
    path('reservationform/5/2/3', views.d5c2t3, name='form'),
    path('reservationform/5/2/4', views.d5c2t4, name='form'),
    path('reservationform/5/2/5', views.d5c2t5, name='form'),
    path('reservationform/5/2/6', views.d5c2t6, name='form'),
    #Court 3
    path('reservationform/5/3/1', views.d5c3t1, name='form'),
    path('reservationform/5/3/2', views.d5c3t2, name='form'),
    path('reservationform/5/3/3', views.d5c3t3, name='form'),
    path('reservationform/5/3/4', views.d5c3t4, name='form'),
    path('reservationform/5/3/5', views.d5c3t5, name='form'),
    path('reservationform/5/3/6', views.d5c3t6, name='form'),
    #Court 4
    path('reservationform/5/4/1', views.d5c4t1, name='form'),
    path('reservationform/5/4/2', views.d5c4t2, name='form'),
    path('reservationform/5/4/3', views.d5c4t3, name='form'),
    path('reservationform/5/4/4', views.d5c4t4, name='form'),
    path('reservationform/5/4/5', views.d5c4t5, name='form'),
    path('reservationform/5/4/6', views.d5c4t6, name='form'),
    #Court 5
    path('reservationform/5/5/1', views.d5c5t1, name='form'),
    path('reservationform/5/5/2', views.d5c5t2, name='form'),
    path('reservationform/5/5/3', views.d5c5t3, name='form'),
    path('reservationform/5/5/4', views.d5c5t4, name='form'),
    path('reservationform/5/5/5', views.d5c5t5, name='form'),
    path('reservationform/5/5/6', views.d5c5t6, name='form'),
    #Court 6
    path('reservationform/5/6/1', views.d5c6t1, name='form'),
    path('reservationform/5/6/2', views.d5c6t2, name='form'),
    path('reservationform/5/6/3', views.d5c6t3, name='form'),
    path('reservationform/5/6/4', views.d5c6t4, name='form'),
    path('reservationform/5/6/5', views.d5c6t5, name='form'),
    path('reservationform/5/6/6', views.d5c6t6, name='form'),
    #Court 7
    path('reservationform/5/7/1', views.d5c7t1, name='form'),
    path('reservationform/5/7/2', views.d5c7t2, name='form'),
    path('reservationform/5/7/3', views.d5c7t3, name='form'),
    path('reservationform/5/7/4', views.d5c7t4, name='form'),
    path('reservationform/5/7/5', views.d5c7t5, name='form'),
    path('reservationform/5/7/6', views.d5c7t6, name='form'),
    #Court 8
    path('reservationform/5/8/1', views.d5c8t1, name='form'),
    path('reservationform/5/8/2', views.d5c8t2, name='form'),
    path('reservationform/5/8/3', views.d5c8t3, name='form'),
    path('reservationform/5/8/4', views.d5c8t4, name='form'),
    path('reservationform/5/8/5', views.d5c8t5, name='form'),
    path('reservationform/5/8/6', views.d5c8t6, name='form'),
    #Court 9
    path('reservationform/5/9/1', views.d5c9t1, name='form'),
    path('reservationform/5/9/2', views.d5c9t2, name='form'),
    path('reservationform/5/9/3', views.d5c9t3, name='form'),
    path('reservationform/5/9/4', views.d5c9t4, name='form'),
    path('reservationform/5/9/5', views.d5c9t5, name='form'),
    path('reservationform/5/9/6', views.d5c9t6, name='form'),
    #Court 10
    path('reservationform/5/10/1', views.d5c10t1, name='form'),
    path('reservationform/5/10/2', views.d5c10t2, name='form'),
    path('reservationform/5/10/3', views.d5c10t3, name='form'),
    path('reservationform/5/10/4', views.d5c10t4, name='form'),
    path('reservationform/5/10/5', views.d5c10t5, name='form'),
    path('reservationform/5/10/6', views.d5c10t6, name='form'),
    #Court 11
    path('reservationform/5/11/1', views.d5c11t1, name='form'),
    path('reservationform/5/11/2', views.d5c11t2, name='form'),
    path('reservationform/5/11/3', views.d5c11t3, name='form'),
    path('reservationform/5/11/4', views.d5c11t4, name='form'),
    path('reservationform/5/11/5', views.d5c11t5, name='form'),
    path('reservationform/5/11/6', views.d5c11t6, name='form'),
    #Court 12
    path('reservationform/5/12/1', views.d5c12t1, name='form'),
    path('reservationform/5/12/2', views.d5c12t2, name='form'),
    path('reservationform/5/12/3', views.d5c12t3, name='form'),
    path('reservationform/5/12/4', views.d5c12t4, name='form'),
    path('reservationform/5/12/5', views.d5c12t5, name='form'),
    path('reservationform/5/12/6', views.d5c12t6, name='form'),

    #Day 6
     #Court 1
    path('reservationform/6/1/1', views.d6c1t1, name='form'),
    path('reservationform/6/1/2', views.d6c1t2, name='form'),
    path('reservationform/6/1/3', views.d6c1t3, name='form'),
    path('reservationform/6/1/4', views.d6c1t4, name='form'),
    path('reservationform/6/1/5', views.d6c1t5, name='form'),
    path('reservationform/6/1/6', views.d6c1t6, name='form'),
    #Court 2
    path('reservationform/6/2/1', views.d6c2t1, name='form'),
    path('reservationform/6/2/2', views.d6c2t2, name='form'),
    path('reservationform/6/2/3', views.d6c2t3, name='form'),
    path('reservationform/6/2/4', views.d6c2t4, name='form'),
    path('reservationform/6/2/5', views.d6c2t5, name='form'),
    path('reservationform/6/2/6', views.d6c2t6, name='form'),
    #Court 3
    path('reservationform/6/3/1', views.d6c3t1, name='form'),
    path('reservationform/6/3/2', views.d6c3t2, name='form'),
    path('reservationform/6/3/3', views.d6c3t3, name='form'),
    path('reservationform/6/3/4', views.d6c3t4, name='form'),
    path('reservationform/6/3/5', views.d6c3t5, name='form'),
    path('reservationform/6/3/6', views.d6c3t6, name='form'),
    #Court 4
    path('reservationform/6/4/1', views.d6c4t1, name='form'),
    path('reservationform/6/4/2', views.d6c4t2, name='form'),
    path('reservationform/6/4/3', views.d6c4t3, name='form'),
    path('reservationform/6/4/4', views.d6c4t4, name='form'),
    path('reservationform/6/4/5', views.d6c4t5, name='form'),
    path('reservationform/6/4/6', views.d6c4t6, name='form'),
    #Court 5
    path('reservationform/6/5/1', views.d6c5t1, name='form'),
    path('reservationform/6/5/2', views.d6c5t2, name='form'),
    path('reservationform/6/5/3', views.d6c5t3, name='form'),
    path('reservationform/6/5/4', views.d6c5t4, name='form'),
    path('reservationform/6/5/5', views.d6c5t5, name='form'),
    path('reservationform/6/5/6', views.d6c5t6, name='form'),
    #Court 6
    path('reservationform/6/6/1', views.d6c6t1, name='form'),
    path('reservationform/6/6/2', views.d6c6t2, name='form'),
    path('reservationform/6/6/3', views.d6c6t3, name='form'),
    path('reservationform/6/6/4', views.d6c6t4, name='form'),
    path('reservationform/6/6/5', views.d6c6t5, name='form'),
    path('reservationform/6/6/6', views.d6c6t6, name='form'),
    #Court 7
    path('reservationform/6/7/1', views.d6c7t1, name='form'),
    path('reservationform/6/7/2', views.d6c7t2, name='form'),
    path('reservationform/6/7/3', views.d6c7t3, name='form'),
    path('reservationform/6/7/4', views.d6c7t4, name='form'),
    path('reservationform/6/7/5', views.d6c7t5, name='form'),
    path('reservationform/6/7/6', views.d6c7t6, name='form'),
    #Court 8
    path('reservationform/6/8/1', views.d6c8t1, name='form'),
    path('reservationform/6/8/2', views.d6c8t2, name='form'),
    path('reservationform/6/8/3', views.d6c8t3, name='form'),
    path('reservationform/6/8/4', views.d6c8t4, name='form'),
    path('reservationform/6/8/5', views.d6c8t5, name='form'),
    path('reservationform/6/8/6', views.d6c8t6, name='form'),
    #Court 9
    path('reservationform/6/9/1', views.d6c9t1, name='form'),
    path('reservationform/6/9/2', views.d6c9t2, name='form'),
    path('reservationform/6/9/3', views.d6c9t3, name='form'),
    path('reservationform/6/9/4', views.d6c9t4, name='form'),
    path('reservationform/6/9/5', views.d6c9t5, name='form'),
    path('reservationform/6/9/6', views.d6c9t6, name='form'),
    #Court 10
    path('reservationform/6/10/1', views.d6c10t1, name='form'),
    path('reservationform/6/10/2', views.d6c10t2, name='form'),
    path('reservationform/6/10/3', views.d6c10t3, name='form'),
    path('reservationform/6/10/4', views.d6c10t4, name='form'),
    path('reservationform/6/10/5', views.d6c10t5, name='form'),
    path('reservationform/6/10/6', views.d6c10t6, name='form'),
    #Court 11
    path('reservationform/6/11/1', views.d6c11t1, name='form'),
    path('reservationform/6/11/2', views.d6c11t2, name='form'),
    path('reservationform/6/11/3', views.d6c11t3, name='form'),
    path('reservationform/6/11/4', views.d6c11t4, name='form'),
    path('reservationform/6/11/5', views.d6c11t5, name='form'),
    path('reservationform/6/11/6', views.d6c11t6, name='form'),
    #Court 12
    path('reservationform/6/12/1', views.d6c12t1, name='form'),
    path('reservationform/6/12/2', views.d6c12t2, name='form'),
    path('reservationform/6/12/3', views.d6c12t3, name='form'),
    path('reservationform/6/12/4', views.d6c12t4, name='form'),
    path('reservationform/6/12/5', views.d6c12t5, name='form'),
    path('reservationform/6/12/6', views.d6c12t6, name='form'),

    #Day 7
     #Court 1
    path('reservationform/7/1/1', views.d7c1t1, name='form'),
    path('reservationform/7/1/2', views.d7c1t2, name='form'),
    path('reservationform/7/1/3', views.d7c1t3, name='form'),
    path('reservationform/7/1/4', views.d7c1t4, name='form'),
    path('reservationform/7/1/5', views.d7c1t5, name='form'),
    path('reservationform/7/1/6', views.d7c1t6, name='form'),
    #Court 2
    path('reservationform/7/2/1', views.d7c2t1, name='form'),
    path('reservationform/7/2/2', views.d7c2t2, name='form'),
    path('reservationform/7/2/3', views.d7c2t3, name='form'),
    path('reservationform/7/2/4', views.d7c2t4, name='form'),
    path('reservationform/7/2/5', views.d7c2t5, name='form'),
    path('reservationform/7/2/6', views.d7c2t6, name='form'),
    #Court 3
    path('reservationform/7/3/1', views.d7c3t1, name='form'),
    path('reservationform/7/3/2', views.d7c3t2, name='form'),
    path('reservationform/7/3/3', views.d7c3t3, name='form'),
    path('reservationform/7/3/4', views.d7c3t4, name='form'),
    path('reservationform/7/3/5', views.d7c3t5, name='form'),
    path('reservationform/7/3/6', views.d7c3t6, name='form'),
    #Court 4
    path('reservationform/7/4/1', views.d7c4t1, name='form'),
    path('reservationform/7/4/2', views.d7c4t2, name='form'),
    path('reservationform/7/4/3', views.d7c4t3, name='form'),
    path('reservationform/7/4/4', views.d7c4t4, name='form'),
    path('reservationform/7/4/5', views.d7c4t5, name='form'),
    path('reservationform/7/4/6', views.d7c4t6, name='form'),
    #Court 5
    path('reservationform/7/5/1', views.d7c5t1, name='form'),
    path('reservationform/7/5/2', views.d7c5t2, name='form'),
    path('reservationform/7/5/3', views.d7c5t3, name='form'),
    path('reservationform/7/5/4', views.d7c5t4, name='form'),
    path('reservationform/7/5/5', views.d7c5t5, name='form'),
    path('reservationform/7/5/6', views.d7c5t6, name='form'),
    #Court 6
    path('reservationform/7/6/1', views.d7c6t1, name='form'),
    path('reservationform/7/6/2', views.d7c6t2, name='form'),
    path('reservationform/7/6/3', views.d7c6t3, name='form'),
    path('reservationform/7/6/4', views.d7c6t4, name='form'),
    path('reservationform/7/6/5', views.d7c6t5, name='form'),
    path('reservationform/7/6/6', views.d7c6t6, name='form'),
    #Court 7
    path('reservationform/7/7/1', views.d7c7t1, name='form'),
    path('reservationform/7/7/2', views.d7c7t2, name='form'),
    path('reservationform/7/7/3', views.d7c7t3, name='form'),
    path('reservationform/7/7/4', views.d7c7t4, name='form'),
    path('reservationform/7/7/5', views.d7c7t5, name='form'),
    path('reservationform/7/7/6', views.d7c7t6, name='form'),
    #Court 8
    path('reservationform/7/8/1', views.d7c8t1, name='form'),
    path('reservationform/7/8/2', views.d7c8t2, name='form'),
    path('reservationform/7/8/3', views.d7c8t3, name='form'),
    path('reservationform/7/8/4', views.d7c8t4, name='form'),
    path('reservationform/7/8/5', views.d7c8t5, name='form'),
    path('reservationform/7/8/6', views.d7c8t6, name='form'),
    #Court 9
    path('reservationform/7/9/1', views.d7c9t1, name='form'),
    path('reservationform/7/9/2', views.d7c9t2, name='form'),
    path('reservationform/7/9/3', views.d7c9t3, name='form'),
    path('reservationform/7/9/4', views.d7c9t4, name='form'),
    path('reservationform/7/9/5', views.d7c9t5, name='form'),
    path('reservationform/7/9/6', views.d7c9t6, name='form'),
    #Court 10
    path('reservationform/7/10/1', views.d7c10t1, name='form'),
    path('reservationform/7/10/2', views.d7c10t2, name='form'),
    path('reservationform/7/10/3', views.d7c10t3, name='form'),
    path('reservationform/7/10/4', views.d7c10t4, name='form'),
    path('reservationform/7/10/5', views.d7c10t5, name='form'),
    path('reservationform/7/10/6', views.d7c10t6, name='form'),
    #Court 11
    path('reservationform/7/11/1', views.d7c11t1, name='form'),
    path('reservationform/7/11/2', views.d7c11t2, name='form'),
    path('reservationform/7/11/3', views.d7c11t3, name='form'),
    path('reservationform/7/11/4', views.d7c11t4, name='form'),
    path('reservationform/7/11/5', views.d7c11t5, name='form'),
    path('reservationform/7/11/6', views.d7c11t6, name='form'),
    #Court 12
    path('reservationform/7/12/1', views.d7c12t1, name='form'),
    path('reservationform/7/12/2', views.d7c12t2, name='form'),
    path('reservationform/7/12/3', views.d7c12t3, name='form'),
    path('reservationform/7/12/4', views.d7c12t4, name='form'),
    path('reservationform/7/12/5', views.d7c12t5, name='form'),
    path('reservationform/7/12/6', views.d7c12t6, name='form'),
]