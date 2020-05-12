from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# 覆盖user表 解决方案：删除数据库中 除了auth_user的其他表，然后重新来一次。
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'姓名', default='')
    birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name=u"性别")
    address = models.CharField(max_length=100, default=u'', verbose_name=u"地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"电话")
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100, verbose_name=u"头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


# class SecondUserProfile(UserProfile):
#     class Meta:
#         verbose_name = u"被提用户"
#         verbose_name_plural = verbose_name
#         proxy = True
