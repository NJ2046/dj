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
from dj.view import hello, current_datetime,\
     current_datetime_t, current_datetime_f, \
     display_meta, current_datetime_r, test_extend

urlpatterns = [
     path('admin/', admin.site.urls),
     path('hello/', hello),
     path('current_datetime/', current_datetime),
     path('current_datetime_t/', current_datetime_t),
     path('current_datetime_f/', current_datetime_f),
     path('current_datetime_r/', current_datetime_r),
     path('display_meta/', display_meta),
     path('test_extend/', test_extend),
]

