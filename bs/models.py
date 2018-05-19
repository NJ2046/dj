from django.db import models

# Create your models here.

"""
class users(models.Model):
    u_name = models.CharField(max_length=50)
    u_pw = models.CharField(max_length=50)
    u_address = models.CharField(max_length=50)
    u_nickname = models.CharField(max_length=50)
    u_createdate = models.DateTimeField()
    u_type = models.IntegerField()
    pass


class classes(models.Model):
    c_name = models.CharField(max_length=100)
    pass


class books(models.Model):
    b_isbn = models.CharField(max_length=20)
    b_name = models.CharField(max_length=100)
    b_writer = models.CharField(max_length=100)
    b_publish = models.CharField(max_length=100)
    b_class = models.ForeignKey(classes)
    b_ps = models.TextField(max_length=1000)
    b_price = models.DecimalField()
    b_cover = models.CharField(max_length=20)
    b_total = models.IntegerField(max_length=20)
    b_createdate = models.DateField()


class cart(models.Model):
    c_u_id = models.ForeignKey(users)
    c_b_id = models.ForeignKey(books)
    c_amount = models.IntegerField()
    c_createdate = models.DateTimeField(default='')
    pass


class orders(models.Model):

    pass


class orderdetails(models.Model):
    pass


"""


class Classes(models.Model):
    c_name = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return u'%s' % (self.c_name)


class Users(models.Model):
    u_name = models.CharField(max_length=45, blank=True, null=True)
    u_pw = models.CharField(max_length=45, blank=True, null=True)
    u_address = models.CharField(max_length=100, blank=True, null=True)
    u_nickname = models.CharField(max_length=45, blank=True, null=True)
    u_creatdate = models.DateTimeField(blank=True, null=True)
    u_type = models.CharField(max_length=45, blank=True, null=True)
    u_sex = models.CharField(max_length=45, blank=True, null=True)
    u_question = models.CharField(max_length=45, blank=True, null=True)
    u_answer = models.CharField(max_length=45, blank=True, null=True)
    u_phone = models.CharField(max_length=45, blank=True, null=True)
    u_email = models.CharField(max_length=45, blank=True, null=True)
    u_balance = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return u'%s' % (self.u_name,)


class Books(models.Model):
    b_isbn = models.CharField(max_length=13, blank=True, null=True)
    b_name = models.CharField(max_length=100, blank=True, null=True)
    b_writer = models.CharField(max_length=50, blank=True, null=True)
    b_publish = models.CharField(max_length=45, blank=True, null=True)
    b_class = models.ForeignKey('Classes', models.DO_NOTHING, db_column='b_class')
    b_ps = models.CharField(max_length=1000, blank=True, null=True)
    b_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    b_cover = models.CharField(max_length=100, blank=True, null=True)
    b_total = models.IntegerField(blank=True, null=True)
    b_createdate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return u'%s %s %s %s %s %s' % (self.b_name, self.b_writer, self.b_publish, self.b_isbn, self.b_price, self.b_ps)


class Orders(models.Model):
    o_u = models.ForeignKey(Users,models.DO_NOTHING)
    o_code = models.CharField(max_length=45, blank=True, null=True)
    o_createdate = models.DateTimeField(blank=True, null=True)
    o_cost = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    o_ps = models.CharField(max_length=45, blank=True, null=True)
    o_state = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return u'%s %s %s %s %s' % (self.o_u, self.o_code, self.o_cost, self.o_ps, self.o_state)


class Orderdetails(models.Model):
    od_o = models.ForeignKey('Orders', models.DO_NOTHING)
    od_b = models.ForeignKey('Books', models.DO_NOTHING)
    od_amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return u'%s %s %s' % (self.od_o, self.od_b, self.od_amount)
    class Meta:
        db_table = 'orderdetails'
        unique_together = (('od_o', 'od_b'),)


class Cart(models.Model):
    c_u = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    c_b = models.ForeignKey(Books, models.DO_NOTHING)
    c_amount = models.IntegerField(blank=True, null=True)
    c_createdate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return u'%s %s %s' % (self.c_u, self.c_b, self.c_amount)

    class Meta:
        managed = False
        db_table = 'cart'
        unique_together = (('c_u', 'c_b'),)


