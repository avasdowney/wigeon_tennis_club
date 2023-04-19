from django.test import TestCase
from django.test import SimpleTestCase

from news.models import AddNews
from django.urls import reverse
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

    def test_news_title_creation_fail(self):
        news = self.create_news()
        self.assertTrue(isinstance(news, AddNews))
        self.assertNotEqual("this is not expected", news.title)

    def test_news_story_creation_fail(self):
        news = self.create_news()
        self.assertTrue(isinstance(news, AddNews))
        self.assertNotEqual("this is not expected", news.story)

class NewsHomepageTests(SimpleTestCase):

    def test_news_url_exists_at_correct_location(self):
        response = self.client.get("/news")
        self.assertEqual(response.status_code, 301)

    def test_news_url_available_by_name(self):  
        response = self.client.get(reverse("news"))
        self.assertEqual(response.status_code, 200)

    def test_news_home_template_name_correct(self):  
        response = self.client.get(reverse("news"))
        self.assertTemplateUsed(response, "news/news_home.html")