from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from django.template import Template, Context
from django.shortcuts import render
import sys
import os

# noinspection PyUnusedLocal


def hello(request):
    return HttpResponse("hello")


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

