from django.contrib import admin
from blogs.models import PostWeiboModel, SuggestModel

# Register your models here.


class PostWeiboAdmin(admin.ModelAdmin):
    list_display = ['user', 'to_user', 'to_name']


class SuggestAdmin(admin.ModelAdmin):
    list_display = ['user', 'to_user', 'to_name']


admin.site.register(PostWeiboModel, PostWeiboAdmin)
admin.site.register(SuggestModel, SuggestAdmin)

