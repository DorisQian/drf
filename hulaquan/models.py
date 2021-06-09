from django.db import models
# from django.contrib.auth.models import User, Group


class Article(models.Model):
    """
    文章表
    """
    tag_choice = (
        (1, '资讯'),
        (2, '公司动态'),
        (3, '分享'),
        (4, '答疑'),
        (5, '其他')
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    img = models.CharField(max_length=100, null=True, blank=True, verbose_name='图片')
    view_times = models.IntegerField(default=0, verbose_name='访问量')
    tag = models.IntegerField(choices=tag_choice, verbose_name='标签')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(default='已注销', to='auth.User',  on_delete=models.SET_DEFAULT, verbose_name='作者')


class ArticleContent(models.Model):
    """
    文章内容表
    """
    content = models.TextField()
    article = models.OneToOneField(to='Article', on_delete=models.CASCADE, verbose_name='文章')

    class Meta:
        db_table = "hulaquan_article_content"


class Comment(models.Model):
    u"""
    文章评论表
    """
    comment = models.CharField(max_length=200, verbose_name='评论')
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE, verbose_name='文章')
    user = models.ForeignKey(default='已注销', to='auth.User', on_delete=models.SET_DEFAULT, verbose_name='评论者')
