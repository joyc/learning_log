#! python3
# -*- coding:utf-8 -*-
# @Time    : 2017/9/10 18:46
# @Author  : Hython.com
# @File    : urls.py
# @IDE     : PyCharm
"""为应用程序users定义URL模式"""
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 登陆页面
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    # 注册页面
    url(r'^register/$', views.register, name='register'),
    # 注销页面
    url(r'^logout/$', views.logout_view, name='logout'),
]