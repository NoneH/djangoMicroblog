from django.db import models
from datetime import datetime

from users.models import UserProfile


# Create your models here.

class PostWeiboModel(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    to_user = models.IntegerField(default=0, verbose_name=u"被提用户id")
    to_name = models.CharField(max_length=50, default="", verbose_name=u"被提用户名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户@其他用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nick_name


class SuggestModel(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    to_user = models.IntegerField(default=0, verbose_name=u"被推荐用户")
    to_name = models.CharField(max_length=50, default="", verbose_name=u"被推荐用户名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户推荐信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nick_name
