from django.urls import path
from . import views

app_name = "members"
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path("directory/", views.DirectoryView.as_view(), name="directory"),
]