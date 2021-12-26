from django.shortcuts import render

# Create your views here.

from django import views
from django.contrib import auth
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.authtoken.models import Token


from commom.utils import pack_msg
from commom.define import SUCCESS, ERROR
from account.models import UserProfile


def register(request):
    # post请求提交注册数据
    data = request.POST
    username = data.get('username')
    password = data.get('password')
    if UserProfile.objects.filter(username=username):
        return JsonResponse(pack_msg(status=ERROR))
    else:
        # 帐号可用，去掉多余密码，在数据库创建记录
        obj = UserProfile.objects.create_user(username=username, password=password)  # 创建普通用户
        return JsonResponse(pack_msg(status=SUCCESS, result={'id': obj.id}))


# 用户登录视
def login(request):
    data = request.POST
    # 获取用户登录信息
    username = data.get("username")
    password = data.get("password")

    # 使用django的auth模块进行用户名密码验证
    user = auth.authenticate(username=username, password=password)
    if user:
        # 将用户名存入session中
        request.session["user"] = username
        auth.login(request, user)  # 将用户信息添加到session中
        old_token = Token.objects.filter(user=user)
        old_token.delete()
        # 创建新的token并传递给前端
        token = Token.objects.create(user=user)
        print(token)
        return JsonResponse(pack_msg(status=SUCCESS, result={'id': user.id, 'token': token.key}))
    else:
        return JsonResponse(pack_msg(status=ERROR))


def get_all_user(request):
    result = []
    for user in UserProfile.objects.all():
        result.append(model_to_dict(user))
    return JsonResponse(pack_msg(status=SUCCESS, result=result))
