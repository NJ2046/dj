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
     path(r'register/', view.register),
     url(r'reg', view.reg),
     # 登陆
     path(r'login/', view.login),
     path(r'my/', view.my),
     # 修改信息
     path(r'modifyuserinfo/', view.modif),
     path(r'modifyuserinfo/modif', view.mod),
     # 订单查询
     path(r'orderlist/', view.order),
     # 账户余额
     path(r'balance/', view.balance),
     # 充值
     path(r'up/', view.up),

     # 购物车
     path(r'cart/', view.cart),
     path(r'del_cart/', view.del_cart),

     # 订单
     path(r'order/', view.order),
     path(r'orderfinal/', view.final),
     path(r'ordersucess/', view.order_success),

]

urlpatterns += staticfiles_urlpatterns()
