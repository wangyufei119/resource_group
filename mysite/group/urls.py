from django.urls import path

from group import views

urlpatterns = [
    path('group/add', views.create_group),
    path('group/list', views.get_group_list),
    path('group_user/update', views.update_group_user),
    path('group_manager/add', views.group_add_manager),
    path('group_user_list/list', views.get_group_user_list),
    path('group_product/search', views.search_group_product),
    path('group_user_product/list', views.get_user_product),
]
