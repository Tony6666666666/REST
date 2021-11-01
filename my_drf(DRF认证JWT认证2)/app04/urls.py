#coding=utf-8
from django.conf.urls import url
from django.urls import path

from app04 import views

# 写法一
# urlpatterns=[
#     url(r'articles/$',views.article_list,name='article-list'),
#     url(r'articles/<int:pk>/$',views.article_detail,name='article-detail'),
#     url(r'categorys/$',views.category_list,name='category-list'),
#     url(r'categorys/<int:pk>/$',views.category_detail,name='category-detail'),
# ]

# 写法二
# urlpatterns=[
#     url(r'games/$',views.GameList.as_view(),name='game-list'),
#     url(r'games/<int:pk>/$',views.GameDetail.as_view(),name='game-detail'),
# ]

urlpatterns=[
    path(r'games/',views.GameList.as_view(),name='game-list'),
    path(r'games/<int:pk>/',views.GameDetail.as_view(),name='game-detail'),
]