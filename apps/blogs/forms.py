#!/usr/bin/env python
# encoding: utf-8
"""
@version: Python 3.7.0
@author: Xingyu Bu
@license: Apache Licence 
@contact: 1774142766@qq.com
@site: 
@software: PyCharm
@file: forms.py
@time: 2020/5/11 20:46
"""
from django import forms
from captcha.fields import CaptchaField

from blogs.models import PostWeiboModel


# 判定以及提示功能 form自带seld.errors值判定错误
class PostWeiboForm(forms.Form):
    # required = True(意为如果字段为空就报错)  min_length=5(即最小长度）
    # 这个名称必须和前端HTML页面的name一致（即name="username"）
    to_name = forms.CharField(required=True)
    # class Meta:
    #     model = PostWeiboModel
    #     fields = ['to_name']
