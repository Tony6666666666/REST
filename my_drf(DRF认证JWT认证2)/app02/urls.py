#coding=utf-8
from django.conf.urls import url
from django.urls import path

from app02 import views

# 写法一
# urlpatterns=[
#     url(r'articles/$',views.article_list,name='article-list'),
#     url(r'articles/<int:pk>/$',views.article_detail,name='article-detail'),
#     url(r'categorys/$',views.category_list,name='category-list'),
#     url(r'categorys/<int:pk>/$',views.category_detail,name='category-detail'),
# ]

# 写法二
urlpatterns=[
    path('articles/', views.article_list, name='article-list'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),

    path('categorys/',views.category_list,name='category-list'),
    path('categorys/<int:pk>/',views.category_detail,name='category-detail'),

    path('tags/',views.tag_list,name='tag-list'),
    path('tags/<int:pk>/',views.tag_detail,name='tag-detail'),
]