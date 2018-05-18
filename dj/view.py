# encoding: utf-8
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.template.loader import get_template
import datetime
from django.template import Template, Context
from django.shortcuts import render
from django.db import connection
from django.shortcuts import render_to_response, get_object_or_404
import sys
import os
from bs.models import Users, Orders, Books
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


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.POST:
        message = 'You searched for %r' % request.POST['q']
    else:
        message = 'You submitted an empty form'
    return HttpResponse(message)


def search1(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Books.objects.filter(b_name__icontains=q)
        return render(request, 'search_results.html', {'books': books, 'query': q})


def index(request):
    cursor = connection.cursor()
    cursor.execute('''select o.od_b_id,sum(b.b_price) t
                    from orderdetails o INNER JOIN bs_books b on o.od_b_id = b.id
                    group by o.od_b_id
                    ORDER BY t desc
                    limit 10'''
                   );
    row = cursor.fetchall()
    ids = [t[0] for t in row]
    hots_s = (Books.objects.filter(id__in=ids[:5]))
    hots_x = (Books.objects.filter(id__in=ids[5:]))
    # books = Books.objects.filter(b_writer='谭浩强')
    books = Books.objects.order_by('b_price')[0:5]
    return render(request, 'index.html', {'books': books, 'hots_s': hots_s, 'hots_x': hots_x})
    pass


def register(request):
    return render(request, 'register.html')


def reg(request):
    email = request.GET['email']
    name = request.GET['name']
    pw = request.GET['password']
    sex = request.GET['sex']
    phone = request.GET['phone']
    address = request.GET['address']
    question = request.GET['select']
    answer = request.GET['answer']
    u1 = Users(u_name=name, u_email=email, u_pw=pw, u_sex=sex, u_phone=phone, u_address=address, u_question=question, u_answer=answer)
    u1.save()
    return render(request, 'success.html')


def login(request):
    return render(request, 'login.html')


def log(request):
    username = request.COOKIES.get('name', '')
    name = request.POST['name']
    if name != username or username:
        books = Books.objects.order_by('b_price')[0:5]
        return render(request, 'my.html', {'books': books})
        pass
    else:
        pw = request.POST['pw']
        books = Books.objects.order_by('b_price')[0:5]
        try:
            db = Users.objects.get(u_name=name)
            if db.u_pw == pw:
                response = render_to_response('my.html', {'books': books})
                name = smart_str(name)
                response.set_cookie('name', name)
                return response
                # return render(request, 'my.html', {'books': books})
            else:
                return HttpResponse('密码不对')
        except:
            return HttpResponse('用户名不存在')


def modif(request):
    username = request.COOKIES.get('name', '')
    return render(request, 'modifyuserinfo.html', {'name': username})

def mod(request):
    username = request.COOKIES.get('name', '')
    pw = request.POST['pw']
    phone = request.POST['phone']
    sex = request.POST['sex']
    address = request.POST['address']
    question = request.POST['select']
    answer = request.POST['answer']
    db = Users.objects.get(u_name=username)
    db.u_pw = pw
    db.u_phone = phone
    db.u_address = address
    db.u_question = question
    db.u_answer = answer
    db.u_sex = sex
    db.save()
    return render(request, 'mod_success.html')



