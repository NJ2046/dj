"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
import dj.view as view
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles


urlpatterns = [
     path('admin/', admin.site.urls),
     path('hello/', view.hello),
     path(r'search_form/', view.search_form),
     path(r'search/', view.search),
     path(r'index/', view.index),
     # 注册
     path(r'index/register/', view.register),
     url(r'index/register/reg*', view.reg),
     # 登陆
     path(r'index/login/', view.login),
     url(r'index/login/log*', view.log),
]

urlpatterns += staticfiles_urlpatterns()
