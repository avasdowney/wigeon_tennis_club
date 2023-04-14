from django.test import TestCase

from news.models import AddNews
from django.utils import timezone
from news.forms import AddNewsForm


class AddNewsTest(TestCase):
    
    def create_news(self, title="only a test", story="yes, this is only a test"):
        return AddNews.objects.create(title=title, story=story)

    def test_news_title_creation(self):
        news = self.create_news()
        self.assertTrue(isinstance(news, AddNews))
        self.assertEqual("only a test", news.title)

    def test_news_story_creation(self):
        news = self.create_news()
        self.assertTrue(isinstance(news, AddNews))
        self.assertEqual("yes, this is only a test", news.story)