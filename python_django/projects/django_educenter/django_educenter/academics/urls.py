from django.urls import path
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from academics import views as academics_views

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [
    # Course CRUDs
    path('courses/', cache_page(CACHE_TTL)(academics_views.CourseListView.as_view()), name='course-list'),
    path('course/<int:pk>/', cache_page(CACHE_TTL)(academics_views.CourseDetailView.as_view()), name='course-detail'),
    path('course/new/', academics_views.CourseCreateView.as_view(), name='course-create'),
    path('course/<int:pk>/update/', academics_views.CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete/', academics_views.CourseDeleteView.as_view(), name='course-delete'),

    # Scholarship CRUDs
    path('scholarships/', cache_page(CACHE_TTL)(academics_views.ScholarshipListView.as_view()), name='scholarship-list'),
    path('scholarship/new/', academics_views.ScholarshipCreateView.as_view(), name='scholarship-create'),
    path('scholarship/<int:pk>/update/', academics_views.ScholarshipUpdateView.as_view(), name='scholarship-update'),
    path('scholarship/<int:pk>/delete/', academics_views.ScholarshipDeleteView.as_view(), name='scholarship-delete'),
]