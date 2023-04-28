from django.urls import path
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from postings import views as postings_views

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [
    # blog CRUDs
    path('blog/', cache_page(CACHE_TTL)(postings_views.BlogListView.as_view()), name='blog-list'),
    path('blog/<int:pk>/', cache_page(CACHE_TTL)(postings_views.BlogDetailView.as_view()), name='blog-detail'),
    path('blog/new/', postings_views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update/', postings_views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', postings_views.BlogDeleteView.as_view(), name='blog-delete'),

    # event CRUDs
    path('events/', cache_page(CACHE_TTL)(postings_views.EventListView.as_view()), name='event-list'),
    path('event/<int:pk>/', cache_page(CACHE_TTL)(postings_views.EventDetailView.as_view()), name='event-detail'),
    path('event/new/', postings_views.EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', postings_views.EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', postings_views.EventDeleteView.as_view(), name='event-delete'),

]