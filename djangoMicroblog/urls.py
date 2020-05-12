"""djangoMicroblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from djangoMicroblog.settings import MEDIA_ROOT
from users.views import IndexView, LoginView
from blogs.views import PostWeiboView, SuggestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LoginView.as_view(), name="logout"),
    path('captcha/', include('captcha.urls')),
    path('users/', include(('users.urls', 'users'), namespace='user')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('postweibo/', PostWeiboView.as_view(), name="postweibo"),
    path('Suggest/', SuggestView.as_view(), name="Suggest"),

]
