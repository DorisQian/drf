# -*- coding: utf-8 -*-

import drf.response_message as em
from drf.response_message import get_message
from hulaquan.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


def rename_response_data(obj, data):
    """
    重新定制返回参数
    :param obj:
    :param data:
    :return:
    """
    response_json = {
        'count': obj.page.paginator.count,
        'next': obj.get_next_link(),
        'previous': obj.get_previous_link(),
        'data': data
    }
    return response_json


class ArticleList(APIView):
    """文章列表"""

    def get(self, request, *args, **kwargs):
        article = Article.objects.all().order_by('-create_time')
        page = PageNumberPagination()
        article_page = page.paginate_queryset(article, request)
        article_list = ArticleListSerializer(instance=article_page, many=True)
        return Response(rename_response_data(page, article_list.data))


class ArticleView(APIView):
    """文章详情"""

    def get(self, request, *args, **kwargs):
        try:
            pk = args[0]
            try:
                article = Article.objects.get(pk=pk)
                article_detail = ArticleSerializer(instance=article)
                return Response(get_message(data=article_detail.data))
            except Exception as e:
                return Response(get_message(em.NO_DATA))
        except IndexError as e:
            return Response({"code": 1, "message": "获取失败，缺少id"})

    def post(self, request, *args, **kwargs):
        data = request.data
        ser_data = ArticleAddSerializer(data=data)
        if ser_data.is_valid():
            new_ar = ser_data.save(author_id=1)
            ser_content = ArticleContentSerializer(data=data)
            if ser_content.is_valid():
                ser_content.save(article=new_ar)
                return Response(get_message(em.SUCCESS))
            else:
                return Response(ser_content.errors)
        else:
            return Response(ser_data.errors)


class CommentView(APIView):
    """评论"""

    def get(self, request, *args, **kwargs):
        article = request.query_params.get('article')
        if article:
            try:
                comment = Comment.objects.filter(article_id=article)
                ser_comment = CommentSerializer(instance=comment, many=True)
                return Response(get_message(data=ser_comment.data))
            except Exception as e:
                return Response(get_message(em.NO_DATA))
        else:
            return Response(get_message(em.NO_PARAM))

    def post(self, request, *args, **kwargs):
        data = request.data
        ser_comment = CommentSerializer(data=data)
        if ser_comment.is_valid():
            ser_comment.save(user_id=1)
            return Response(get_message(em.SUCCESS))
        else:
            return Response(ser_comment.errors)
