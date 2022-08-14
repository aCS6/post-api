from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create(
            username = "testuser",
            email = "example@test.com",
            password ="test",
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "Nice title",
            body = "Nice body"
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username , "testuser")
        self.assertEqual(self.post.title, "Nice title")
        self.assertEqual(self.post.body, "Nice body")
        self.assertEqual(str(self.post), "Nice title")