from django.test import SimpleTestCase
from django.urls import resolve, reverse
from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    about
)

# These are unit tests
class TestUrls(SimpleTestCase):

    def test_post_list_view(self):
        url = reverse('blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_user_post_list_view(self):
        url = reverse('user-posts', args=['Tester'])
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_post_detail_view (self):
        url = reverse('post-detail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_post_create_view(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_post_update_view(self):
        url = reverse('post-update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_post_delete_view(self):
        url = reverse('post-delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)

    def test_about(self):
        url = reverse('blog-about')
        self.assertEquals(resolve(url).func, about)