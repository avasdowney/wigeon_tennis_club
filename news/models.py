import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class AddNews(models.Model):
    title = models.TextField(max_length=100, primary_key=True)
    story = models.TextField()
    date = models.DateField(max_length=8, auto_now_add=True)

    def base(request):
        # grab all stories from database:
        all_stories = AddNews.objects.all()
        return render(request, 'news_home.html', 
            {
            'title': title, 
            'story': story,
            'date': date,
            })
