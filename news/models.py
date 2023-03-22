from django.db import models


class AddNews(models.Model):
    title = models.TextField(max_length=100, primary_key=True)
    story = models.TextField()
    date = models.DateField(max_length=8)
