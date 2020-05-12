import json
from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from users.models import UserProfile
from blogs.models import PostWeiboModel, SuggestModel
from users.forms import LoginForm, UserInfoForm
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 退出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


# 登录
class LoginView(View):
    def get(self, request):
        login_form_captcha = LoginForm(request.POST)
        return render(request, "login.html", {
            "login_form_captcha": login_form_captcha,
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        login_form_captcha = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)  # 内置登陆验证方法
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {
                        "msg": "用户未激活",
                        "login_form_captcha": login_form_captcha,
                    })
            else:
                return render(request, "login.html", {
                    "msg": "用户名或密码错误！",
                    "login_form_captcha": login_form_captcha,
                })
        else:
            return render(request, 'login.html', {
                "login_form": login_form,
                "login_form_captcha": login_form_captcha,
            })


class IndexView(View):
    """
    首页index
    """
    def get(self, request):
        users = UserProfile.objects.all()
        to_users = PostWeiboModel.objects.filter(user=request.user)[:20]
        return render(request, "index.html", {
            "users": users,
            "to_users": to_users,
        })


