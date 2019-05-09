from django.urls import path
from .views import index
from .views import post_detail
from .views import tags_list
from .views import tag_detail
urlpatterns = [
    path('', index, name='posts_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>', tag_detail, name='tag_detail_url')
]