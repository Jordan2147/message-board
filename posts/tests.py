from django.test import TestCase

from .models import Post
from django.urls import reverse

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test")

    def test_url_exists_at_current_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


    def test_homepage(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response, "This is a test")
    