#coding=utf-8
from django.conf.urls import url
from django.urls import path

from app03 import views

# 写法一
# urlpatterns=[
#     url(r'articles/$',views.article_list,name='article-list'),
#     url(r'articles/<int:pk>/$',views.article_detail,name='article-detail'),
#     url(r'categorys/$',views.category_list,name='category-list'),
#     url(r'categorys/<int:pk>/$',views.category_detail,name='category-detail'),
# ]

# 写法二
urlpatterns=[
    # path('users/', views.user_list, name='user-list'),
    path('users/', views.UserList.as_view(), name='user-list'),
    # path('user/<int:pk>/', views.user_detail, name='user-detail'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

]