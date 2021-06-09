# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/9 15:44
@Auth ： Doris
"""

from django.urls import path, re_path
from hulaquan import views

urlpatterns = [
    path('article_list/', views.ArticleList.as_view()),
    path('article/', views.ArticleView.as_view()),
    re_path(r'article/(\d{1,6})/', views.ArticleView.as_view()),
    path('comment/', views.CommentView.as_view()),
]
