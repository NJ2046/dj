from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from django.template import Template, Context
from django.shortcuts import render
import sys
import os
from bs.models import Users, Orders
# noinspection PyUnusedLocal


def hello(request):
    """
    取数据,id是列名,name也是列名字
    l = test.objects.all()
    r = test.objects.get(id=1)
    r = r.name

    插数据
    t1 = test(name='hhhh')
    t1.save()

    更新数据
    t1 = test.objects.get(id=1)
    t1.name = '更新'
    t1.save()

    删除数据
    # 1
    t1 = test.objects.get(id=2)
    t1.delete()
    # 2
    test.objects.filter(id=3).delete()
    """
    l = Orders.objects.get(id=97)
    name = l.o_u.u_pw
    return HttpResponse(name)


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s</body></html>' % now
    return HttpResponse(html)


def current_datetime_t(requset):
    now = datetime.datetime.now()
    t = Template('<html><body>It is now {{current_date}}</body></html>')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def current_datetime_f(request):
    """
    打开文件加载
    fp = open('C:\\Users\\NJ\\PycharmProjects\\dj\\dj\\template\\test.html', 'r', encoding='utf-8')
    t = Template(fp.read())
    fp.close()
    now = datetime.datetime.now()
    html = t.render(Context({'current_date': now}))
    """
    now = datetime.datetime.now()
    t = get_template('test.html')
    d =dict()
    d['current_date'] = now
    html = t.render(Context(d))
    return HttpResponse(html)

# 最简单，可取
def current_datetime_r(request):
    now = datetime.datetime.now()
    return render(request, 'test.html', {'current_date': now})
    pass


def display_meta(request):
    values = request.META.items()
    # values.sort()
    html = list()
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    pass


def test_extend(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
    pass

if __name__ == '__main__':
    fp = open('./template/test.html', 'r', encoding='utf-8')
    print(fp.read())
    fp.close()
    print('hhhh')
    pass

