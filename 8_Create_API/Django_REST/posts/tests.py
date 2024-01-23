from django.test import TestCase
from .models import Posts
from django.contrib.auth.models import User


# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #testuser1 = User.objects.create(username = 'testuser', password = 'abc123')
        #testuser1.save()
        test_post = Posts.objects.create(title = 'Hello', content = 'Hello123')
        test_post.save()


    def test_blog_content(self):
        post = Posts.objects.get(id = 1)
        #author = f'{post.author}'
        title = f'{post.title}'
        content = f'{post.content}'
        #self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Hello')
        self.assertEqual(content, 'Hello123')