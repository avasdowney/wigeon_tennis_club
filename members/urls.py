from . import views
from django.conf.urls import include
from django.urls import path
 
urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
]