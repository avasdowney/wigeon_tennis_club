from django.contrib import admin
from django.urls import path
from news import views as news_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_news/', add_news_views.add_news_view, name='add_news'),
]
