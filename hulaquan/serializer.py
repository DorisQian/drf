# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/9 15:48
@Auth ： Doris
"""

from rest_framework import serializers
from hulaquan.models import *


class ArticleListSerializer(serializers.ModelSerializer):
    """文章列表"""
    summary = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    tag = serializers.ChoiceField(choices=Article.tag_choice, source='get_tag_display')
    author = serializers.CharField(source='author.username')
    
    class Meta:
        model = Article
        field = ['title', 'summary', 'img', 'view_times', 'tag', 'comment_count', 'author', 'create_time']

    def get_summary(self, obj):
        """
        文章概括，取content中前10个字符
        :param obj:
        :return:
        """
        return obj.articlecontent.content[:10]

    def get_comment_count(self, obj):
        """
        评论数
        :param obj:
        :return:
        """
        return obj.comment_set.all().count()


class ArticleSerializer(serializers.ModelSerializer):
    """文章"""
    content = serializers.CharField(source='articlecontent.content')
    tag = serializers.ChoiceField(choices=Article.tag_choice, source='get_tag_display')
    author = serializers.CharField(source='author.username')

    class Meta:
        model = Article
        field = '__all__'


class ArticleAddSerializer(serializers.ModelSerializer):
    """文章添加"""
    class Meta:
        model = Article
        exclude = ['author']


class ArticleContentSerializer(serializers.ModelSerializer):
    """文章内容"""

    class Meta:
        model = ArticleContent
        exclude = ['article']


class CommentSerializer(serializers.ModelSerializer):
    """评论"""

    class Meta:
        model = Comment
        # field = '__all__'
        exclude = ['user']
