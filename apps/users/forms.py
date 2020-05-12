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
@time: 2020/5/11 16:10
"""
from django import forms
from captcha.fields import CaptchaField
from users.models import UserProfile


class LoginForm(forms.Form):
    # required = True(意为如果字段为空就报错)  min_length=5(即最小长度）
    # 这个名称必须和前端HTML页面的name一致（即name="username"）
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    # student_id = forms.CharField(required=True)
    # 验证码error_messages={"invalid": u"验证码错误"}强行改这个值（invalid）报错的参数
    captcha = CaptchaField()


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # form可以吧文件自动保存
        fields = ['nick_name', 'birday', 'gender', 'address', 'mobile']

