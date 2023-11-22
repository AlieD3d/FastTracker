from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet, CategoryViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('category', CategoryViewSet, basename='posts')
router_v1.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]