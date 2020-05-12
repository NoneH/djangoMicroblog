from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from blogs.forms import PostWeiboForm
from blogs.models import PostWeiboModel, SuggestModel
from users.models import UserProfile

# Create your views here.


class PostWeiboView(View):

    def post(self, request):
        user_form = PostWeiboForm(request.POST)
        if user_form.is_valid():
            to_name = request.POST.get("to_name", "")
            to_user = UserProfile.objects.get(username=to_name)
            postweibo = PostWeiboModel()
            postweibo.user = request.user
            postweibo.to_user = to_user.id
            postweibo.to_name = to_name
            postweibo.save()

            user_to_list = []
            to_user_id = request.user.id
            user_tos = PostWeiboModel.objects.filter(to_user=to_user_id)
            for user_to in user_tos:
                user_to_list.append(user_to.user.id)
            need_users = PostWeiboModel.objects.filter(user_id__in=user_to_list)
            for need_user in need_users:
                need_id = need_user.to_user
                need_name = need_user.to_name
                if need_id != request.user.id:
                    user_suggest = SuggestModel()
                    user_suggest.user = request.user
                    user_suggest.to_name = need_name
                    user_suggest.to_user = need_id
                    user_suggest.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "出错"}', content_type='application/json')


class SuggestView(View):
    def get(self, request):
        suggests = SuggestModel.objects.filter(user=request.user)
        return render(request, 'test.html', {
            "suggests": suggests,
        })

