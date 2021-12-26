import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from commom.utils import format_data, pack_msg
from commom.define import ERROR, SUCCESS

from group.models import CustomGroup, GroupUserMap
from account.models import UserProfile
from product.models import Product


# Create your views here.

def update_group_user(request):
    params = request.POST
    try:
        group_name = params.get('group_name', '')
        user_name = params.get('user_name', '')
        group_name = group_name.strip()
        user_name = user_name.strip()
        if not group_name or not user_name:
            error = 'Params need group_name and user_name! params is {}'.format(params)
            logging.error(error)
            return JsonResponse(pack_msg(status=ERROR, error=error))
        user = UserProfile.objects.filter(username=user_name).first()
        if not user:
            error = 'User not exist'
            logging.error(error)
            return JsonResponse(pack_msg(status=ERROR, error=error))
        group = CustomGroup.objects.filter(name=group_name).first()
        if not group:
            error = 'Group not exist'
            logging.error(error)
            return JsonResponse(pack_msg(status=ERROR, error=error))
        obj, _ = GroupUserMap.objects.get_or_create(group_id=group.id, user=user)
        obj.save()
        return JsonResponse(pack_msg(status=SUCCESS, result={'id': obj.id}))
    except Exception as e:
        logging.error('update_group_user params:{} error:{}'.format(params, e))
        return JsonResponse(pack_msg(status=ERROR, error=e))


def get_group_list(request):
    """
    获取所有的资源组
    """
    result = []
    for group in CustomGroup.objects.all():
        result.append(model_to_dict(group))
    return JsonResponse(pack_msg(status=SUCCESS, result=result))


def create_group(request):
    params = request.POST
    try:
        if request.user.is_superuser:
            name = params.get('name', '')
            if not name:
                logging.error('add_group error params:{}'.format(params))
                return JsonResponse(pack_msg(status=ERROR, error='not find group name'))
            obj = CustomGroup.objects.filter(name=name).first()
            if obj:
                return JsonResponse(pack_msg(status=ERROR, error='this group is exist!'))
            key_list = ['name', 'manager_list']
            data = format_data(key_list, params)
            obj = CustomGroup(**data)
            obj.save()
            return JsonResponse(pack_msg(status=SUCCESS, result={'id': obj.id}))
        else:
            res = pack_msg(status=ERROR, error='No permission')
            return JsonResponse(res)
    except Exception as e:
        logging.error('add_group error:{}'.format(e))
        return JsonResponse(pack_msg(status=ERROR, error=e))


def group_add_manager(request):
    """
    添加资源组管理员
    当前只有超级管理员有权限
    """
    params = request.POST
    try:
        group_id = params.get('group_id', '')
        manager = params.get('manager', '')
        if request.user.is_superuser:
            if not group_id or not manager:
                error = 'Params need group_id and manager! params is {}'.format(params)
                logging.error(error)
                return JsonResponse(pack_msg(status=ERROR, error=error))
            group = CustomGroup.objects.filter(id=group_id).first()
            if not group:
                return JsonResponse(pack_msg(status=ERROR, error='No group'))
            user = UserProfile.is_exist_user(username=manager)
            if not user:
                return JsonResponse(pack_msg(status=ERROR, error='No User'))
            manager_list = group.manager_list.split(',') if group.manager_list else []
            if manager not in manager_list:
                manager_list.append(manager)
            group.manager_list = ','.join(manager_list)
            group.save()
            return JsonResponse(pack_msg(status=SUCCESS, result=model_to_dict(group)))
        else:
            return JsonResponse(pack_msg(status=ERROR, error='No permission'))
    except Exception as e:
        logging.error('group_add_manager error:{}'.format(e))
        return JsonResponse(pack_msg(status=ERROR, error=e))


def get_group_user_list(request):
    """
    获取用户的资源组列表
    """
    try:
        username = request.GET.get('username', '')
        user = UserProfile.objects.filter(username=username).first()
        if not user:
            error = 'Not find user! username:{}'.format(username)
            logging.error(error)
            return JsonResponse(pack_msg(status=ERROR, error=error))
        group_list = list(GroupUserMap.objects.filter(user_id=user.id).values('group_id', 'group__name'))
        return JsonResponse(pack_msg(status=SUCCESS, result=group_list))
    except Exception as e:
        logging.error('group_add_manager error:{}'.format(e))
        return JsonResponse(pack_msg(status=ERROR, error=e))


def search_group_product(request):
    """
    获取某个资源组的产品
    """
    params = request.GET
    try:
        result = []
        group_id = params.get('group_id', 0)
        product_list = Product.objects.filter(group_id=group_id)
        for product in product_list:
            result.append(model_to_dict(product))
        return JsonResponse(pack_msg(status=SUCCESS, result=result))
    except Exception as e:
        logging.error('search_group_product error:{}'.format(e))
        return JsonResponse(pack_msg(status=ERROR, error=e))


def get_user_product(request):
    """
    获取用户拥有权限的产品
    """
    try:
        result = []
        username = request.GET.get('username', '')
        if not username:
            username = request.user.username
        user = UserProfile.objects.filter(username=username).first()
        if not user:
            error = 'Not find user! username:{}'.format(username)
            logging.error(error)
            return JsonResponse(pack_msg(status=ERROR, error=error))
        group_list = list(GroupUserMap.objects.filter(user_id=user.id).values_list('group_id', flat=True))
        product_list = Product.objects.filter(group_id__in=group_list)
        for product in product_list:
            result.append(model_to_dict(product))
        return JsonResponse(pack_msg(status=SUCCESS, result=result))
    except Exception as e:
        logging.error('get_user_product error:{}'.format(e))
        return JsonResponse(pack_msg(status=ERROR, error=e))


