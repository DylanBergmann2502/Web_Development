from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User

# These are unit tests
class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username="Tester1", password="testing1")
        self.post1 = Post.objects.create(
            title='Test Post 1',
            content='Test content 1',
            author=self.user1
        )

    def test_post_exists(self): # the post is created
        self.assertEquals(Post.objects.all().count(), 1)
        self.assertNotEquals(Post.objects.all().count(), 0)

    def test_post_str(self): # string method
        self.assertEquals(str(self.post1), 'Test Post 1')
        self.assertNotEquals(str(self.post1), 'Post Object 1')

    def test_post_deleted(self): # the post is deleted
        Post.objects.get(author=self.user1).delete()
        self.assertEquals(Post.objects.all().count(), 0)
        self.assertNotEquals(Post.objects.all().count(), 1)