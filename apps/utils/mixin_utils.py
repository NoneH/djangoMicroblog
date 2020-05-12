#!/usr/bin/env python
# encoding: utf-8
"""
@version: Python 3.7.0
@author: Xingyu Bu
@license: Apache Licence 
@contact: 1774142766@qq.com
@site: 
@software: PyCharm
@file: mixin_utils.py
@time: 2020/4/6 11:40
"""
__author__ = '卜星宇'
# 让view中 只有登录才能访问view 用于view的继承

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
