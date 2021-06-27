from django.urls import path

from posts.views import CreatePost, like_post, get_like_statistics, bulk_post_like

urlpatterns = [
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('like_post/', like_post, name='like_post'),
    path('bulk_post_like/', bulk_post_like, name='bulk_post_like'),
    path('get_like_statistics/', get_like_statistics, name='like_post'),

]
