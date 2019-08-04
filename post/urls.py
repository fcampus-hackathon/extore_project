from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('', main_page, name='main'),
    path('post/list/', post_list, name='list'),
    path('post/create/', post_create, name='create'),
    path('post/detail/<int:post_id>', post_detail, name='detail'),
    path('post/update/<int:post_id>', post_update, name='update'),
    path('post/delete/<int:post_id>', post_delete, name='delete'),
    path('tags/<tag>/', PostTaggedObjectList.as_view(), name='post_taggedlist'),
    path('post/comments/<int:post_id>/', comment_create, name='comment_create'),
    path('post/like/<int:post_id>/', post_like, name='post_like'),
    path('post/saved/<int:post_id>/', post_saved, name='post_saved'),
    path('post/comment/<int:comment_id>/', comment_like, name='comment_like'),
    path('last_memory/', last_memory, name='last_memory'),
]