from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post

# These are integration tests
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.post_list_view_url = reverse('blog-home')
        self.user1 = User.objects.create(username="Tester1", password="testing1")
        self.post1 = Post.objects.create(
                        title='Test Post 1',
                        content='Test content 1',
                        author=self.user1
                    )
        # After post is created => pk = 1 is assigned to it
        self.post_detail_view_url = reverse('post-detail', args = ['1'])

    def test_post_list_view(self):
        response = self.client.get(self.post_list_view_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_detail_view(self):
        response = self.client.get(self.post_detail_view_url)
        self.assertEquals(response.status_code, 200)
        self.assertNotEquals(response.status_code, 404)
        self.assertTemplateUsed(response, 'blog/post_detail.html') # Should already be checked by Django's devs

    def test_post_create_view(self):
        url = reverse('post-create')
        self.client.force_login(self.user1) # log the user in to be able to create post
        response = self.client.post(url, { # set response variable to save the post
            'title': 'Test Post 2',
            'content': 'Test Content 2'
        })
        self.assertEquals(Post.objects.all().count(), 2)
        post2 = Post.objects.get(content='Test Content 2')
        self.assertEquals(post2.author, self.post1.author)

    def test_post_update_view_same_author(self):
        url = reverse('post-update', kwargs={'pk':'1'})
        self.client.force_login(self.user1)
        response = self.client.post(url, {
            'title': 'Updated Test Post 1',
            'content': 'Test Content 1'
        })
        self.post1.refresh_from_db()
        self.assertEquals(self.post1.title, 'Updated Test Post 1')
        self.assertNotEquals(self.post1.title, 'Test Post 1')

    def test_post_update_view_different_author(self):
        url = reverse('post-update', kwargs={'pk':'1'})
        user2 = User.objects.create(username='tim')
        self.client.force_login(user2)
        response = self.client.post(url, {
            'title': 'Updated Test Post 1',
            'content': 'Test Content 1'
        })
        self.post1.refresh_from_db()
        self.assertNotEquals(self.post1.title, 'Updated Test Post 1')
        self.assertEquals(self.post1.title, 'Test Post 1')

    def test_post_delete_view_same_author(self):
        url = reverse('post-delete', kwargs={'pk':'1'})
        self.client.force_login(self.user1)
        response = self.client.delete(url)
        self.assertEquals(Post.objects.all().count(), 0)
        self.assertNotEquals(Post.objects.all().count(), 1)

    def test_post_delete_view_different_author(self):
        url = reverse('post-delete', kwargs={'pk':'1'})
        user2 = User.objects.create(username='tim')
        self.client.force_login(user2)
        response = self.client.delete(url)
        self.assertEquals(Post.objects.all().count(), 1)
        self.assertNotEquals(Post.objects.all().count(), 0)

    def test_user_post_list_view(self):
        response_fake_user = self.client.get(reverse('user-posts', args = ['Fake Tester']))
        self.assertEquals(response_fake_user.status_code, 404)

        response_real_user = self.client.get(reverse('user-posts', args=['Tester1']))
        self.assertEquals(response_real_user.status_code, 200)
        self.assertTemplateUsed(response_real_user, 'blog/user_posts.html')

    def test_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')