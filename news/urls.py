from django.contrib import admin
from django.urls import path
from news import views as news_views

app_name = "news"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_news/', news_views.add_news_view, name='add_news'),
    path('news/', news_views.NewsView.as_view(), name='news'),
]
