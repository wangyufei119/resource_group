from django.urls import path

from account import views

urlpatterns = [
    path('login', views.login),
    path('all', views.get_all_user)
]
