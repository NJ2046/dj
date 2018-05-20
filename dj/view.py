# encoding: utf-8
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.shortcuts import render
from django.db import connection
from django.shortcuts import render_to_response, get_object_or_404
import sys
import os
from bs.models import Users, Orders, Books, Orderdetails, Cart
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


def book_info(request):
    if request.GET['bk_name']:
        name = request.GET['bk_name']
        bkinfor = Books.objects.get(b_name=name)

        return render(request, 'info.html', {'bkinfor': bkinfor})
        pass
    else:
        pass
    pass


def all_book(request):
    books = Books.objects.all()
    c_e_name = 'books'
    c_name = '所有类别'
    tot = len(books)
    paginator = Paginator(books, 15)
    try:
        page = request.GET['page']
    except:
        page = 1
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)
    return render(request, 'product_list.html', {'contacts': book, 'tot': tot, 'c_name': c_name, 'c_e_name': c_e_name})


def fiction(request):
    books = Books.objects.filter(b_class__id=4)
    c_e_name = 'fiction'
    c_name = '小说'
    tot = len(books)
    paginator = Paginator(books, 15)
    try:
        page = request.GET['page']
    except:
        page = 1
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)
    return render(request, 'product_list.html', {'contacts': book, 'tot': tot, 'c_name': c_name, 'c_e_name': c_e_name})


def literature(request):
    books = Books.objects.filter(b_class__id=3)
    c_e_name = 'literature'
    c_name = '文化'
    tot = len(books)
    paginator = Paginator(books, 15)
    try:
        page = request.GET['page']
    except:
        page = 1
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)
    return render(request, 'product_list.html', {'contacts': book, 'tot': tot, 'c_name': c_name, 'c_e_name': c_e_name})


def textbook(request):
    books = Books.objects.filter(b_class__id=2)
    c_e_name = 'textbook'
    c_name = '教材'
    tot = len(books)
    paginator = Paginator(books, 15)
    try:
        page = request.GET['page']
    except:
        page = 1
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)
    return render(request, 'product_list.html', {'contacts': book, 'tot': tot, 'c_name': c_name, 'c_e_name': c_e_name})


def youth(request):
    books = Books.objects.filter(b_class__id=5)
    c_e_name = 'youth'
    c_name = '青春'
    tot = len(books)
    paginator = Paginator(books, 15)
    try:
        page = request.GET['page']
    except:
        page = 1
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)
    return render(request, 'product_list.html', {'contacts': book, 'tot': tot, 'c_name': c_name, 'c_e_name': c_e_name})


def biography(request):
    books = Books.objects.filter(b_class__id=6)
    c_e_name = 'biography'
    c_name = '传记'
    tot = len(books)
    paginator = Paginator(books, 15)
    try:
        page = request.GET['page']
    except:
        page = 1
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)
    return render(request, 'product_list.html', {'contacts': book, 'tot': tot, 'c_name': c_name, 'c_e_name': c_e_name})


def history(request):
    books = Books.objects.filter(b_class__id=8)
    c_e_name = 'history'
    c_name = '历史'
    tot = len(books)
    paginator = Paginator(books, 15)
    try:
        page = request.GET['page']
    except:
        page = 1
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)
    return render(request, 'product_list.html', {'contacts': book, 'tot': tot, 'c_name': c_name, 'c_e_name': c_e_name})


def search(request):
    if 'bkname' in request.POST:
        bkname = request.POST['bkname']
        books = Books.objects.filter(b_name__contains=bkname)
        tot = len(books)
        paginator = Paginator(books, 5)
        try:
            page = request.GET['page']
        except:
            page = 1
        try:
            book = paginator.page(page)
        except PageNotAnInteger:
            book = paginator.page(1)
        except EmptyPage:
            book = paginator.page(paginator.num_pages)
        response = render_to_response('search.html', {'contacts': book, 'tot': tot})
        name = smart_str(bkname)
        response.set_cookie('bkname', name)
        return response
    elif request.COOKIES.get('bkname', ''):
        bkname = request.COOKIES.get('bkname', '')
        if request.GET['page']:
            books = Books.objects.filter(b_name__contains=bkname)
            tot = len(books)
            paginator = Paginator(books, 5)
            try:
                page = request.GET['page']
            except:
                page = 1
            try:
                book = paginator.page(page)
            except PageNotAnInteger:
                book = paginator.page(1)
            except EmptyPage:
                book = paginator.page(paginator.num_pages)
        return render(request, 'search.html', {'contacts': book, 'tot': tot})
    else:
        pass


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
    username = request.COOKIES.get('name', '')
    if username:
        return HttpResponseRedirect('http://127.0.0.1:8000/my')
    return render(request, 'login.html')


def my(request):
    username = request.COOKIES.get('name', '')
    if request.POST:
        pw = request.POST['pw']
        name = request.POST['name']
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
    else:
        if username:
            books = Books.objects.order_by('b_price')[0:5]
            return render(request, 'my.html', {'books': books})
    """
    if username:
        if request.POST:
            name = request.POST['name']
            if username == name:
                books = Books.objects.order_by('b_price')[0:5]
                return render(request, 'my.html', {'books': books})
        else:
            books = Books.objects.order_by('b_price')[0:5]
            return render(request, 'my.html', {'books': books})
    else:
        pw = request.POST['pw']
        name = request.POST['name']
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
    """


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


def search_order(request):
    username = request.COOKIES.get('name', '')
    db = Orderdetails.objects.filter(od_o__o_u__u_name=username)
    return render(request, 'orderlist.html', {'orders': db})


def balance(request):
    username = request.COOKIES.get('name', '')
    db = Users.objects.get(u_name=username)
    b = db.u_balance
    return render(request, 'balance.html', {'balance': b})


def up(request):
    money = request.POST['money']
    money = int(money)
    username = request.COOKIES.get('name', '')
    db = Users.objects.get(u_name=username)
    db.u_balance = db.u_balance + money
    db.save()
    return render(request, 'up_success.html')


def cart(request):
    if request.POST:
        username = request.COOKIES.get('name', '')
        username = str(username)
        username = username.replace(username,"'" + username + "'")
        bkname = request.POST['bkname']
        bkname = str(bkname)
        bkname = bkname.replace(bkname, "'" + bkname + "'")
        cursor = connection.cursor()
        exe = 'delete from bs.cart where bs.cart.c_u_id in (select id from bs.bs_users where bs.bs_users.u_name = ' + username + ') and bs.cart.c_b_id in (select id from bs.bs_books where bs.bs_books.b_name = ' + bkname + ')'
        cursor.execute(exe)
        # Cart.objects.filter(c_u__u_name=username, c_b__b_name=bkname).delete()

        return HttpResponseRedirect('http://127.0.0.1:8000/cart')
    else:
        username = request.COOKIES.get('name', '')
        db = Cart.objects.filter(c_u__u_name=username)
        amount = 0
        for car in db:
            amount += car.c_b.b_price * car.c_amount
        return render(request, 'cart.html', {'carts': db, 'amount': amount})


def del_cart(request):
    username = request.COOKIES.get('name', '')
    username = str(username)
    username = username.replace(username, "'" + username + "'")
    bkname = request.POST['bkname']
    bkname = str(bkname)
    bkname = bkname.replace(bkname, "'" + bkname + "'")
    cursor = connection.cursor()
    exe = 'delete from bs.cart where bs.cart.c_u_id in (select id from bs.bs_users where bs.bs_users.u_name = ' + username + ') and bs.cart.c_b_id in (select id from bs.bs_books where bs.bs_books.b_name = ' + bkname + ')'
    cursor.execute(exe)
    # Cart.objects.filter(c_u__u_name=username, c_b__b_name=bkname).delete()

    return HttpResponseRedirect('http://127.0.0.1:8000/cart')


def add_cart(request):
    username = request.COOKIES.get('name', '')
    if username:
        bkid = request.GET['bk_id']
        if bkid:
            """
            u = Users.objects.get(u_name=username)
            b = Books.objects.get(id=bkid)
            uid = u.id
            c1 = Cart(c_u=u, c_b=b, c_amount=1)
            c1.save()
            """
            u = Users.objects.get(u_name=username)
            uid = u.id
            sql = 'insert into cart(c_u_id, c_b_id, c_amount) values(' + str(uid) + ',' + str(bkid) + ', 1)'
            cursor = connection.cursor()
            cursor.execute(sql)
            return HttpResponseRedirect('http://127.0.0.1:8000/cart')
    else:
        # 请登录
        return HttpResponseRedirect('http://127.0.0.1:8000/login')
        pass

    pass


def order(request):
    username = request.COOKIES.get('name', '')
    db = Cart.objects.filter(c_u__u_name=username)
    amount = 0
    for car in db:
        amount += car.c_b.b_price * car.c_amount
    u = Users.objects.get(u_name=username)
    phone = u.u_phone
    address = u.u_address
    return render(request, 'order.html', {'carts': db, 'amount': amount, 'u_name': username, 'phone': phone, 'address':address})


def final(request):
    username = request.COOKIES.get('name', '')
    db = Cart.objects.filter(c_u__u_name=username)
    amount = 0
    for car in db:
        amount += car.c_b.b_price * car.c_amount
    u = Users.objects.get(u_name=username)
    phone = u.u_phone
    address = u.u_address
    return render(request, 'orderfinal.html', {'carts': db, 'amount': amount, 'u_name': username, 'phone': phone, 'address':address})


def order_success(request):
    username = request.COOKIES.get('name', '')
    # 减少余额
    amount = 0
    db = Cart.objects.filter(c_u__u_name=username)
    bkid = list()
    num = list()
    for car in db:
        amount += car.c_b.b_price * car.c_amount
        bkid.append(car.c_b.id)
        num.append(car.c_amount)
    u = Users.objects.get(u_name=username)
    u_id = u.id
    u.u_balance = u.u_balance - amount
    u.save()

    # 插入订单表
    u1 = Orders(o_u_id=u_id, o_cost=amount)
    u1.save()
    oid = 'SELECT @@IDENTITY'
    cursor = connection.cursor()
    cursor.execute(oid)
    row = cursor.fetchall()
    # 获得订单主键
    oid = row[0][0]
    for i in range(len(bkid)):
        sql = 'insert into bs.orderdetails(od_o_id, od_b_id, od_amount) values(' + str(oid) + ',' + str(bkid[i]) + ',' + str(num[i]) +')'
        cursor.execute(sql)
    # 插入订单详情表
    return render(request, 'order_success.html')
    pass



