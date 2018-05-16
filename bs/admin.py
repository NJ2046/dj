from django.contrib import admin
from .models import Users, Books, Classes, Orderdetails, Orders
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('u_name', 'u_nickname', 'u_pw', 'u_address')
    search_fields = ('u_name',)


class BooksAdmin(admin.ModelAdmin):
    list_display = ('b_name', 'b_writer', 'b_publish', 'b_isbn', 'b_price', 'b_ps')
    search_fields = ('b_name', 'b_writer')


class ClassAdmin(admin.ModelAdmin):
    list_display = ('c_name',)
    search_fields = ('c_name',)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('o_u', 'o_code', 'o_cost', 'o_ps', 'o_state')
    search_fields = ('o_u__u_name',)


class OrderdetailsAdmin(admin.ModelAdmin):
    list_display = ('od_o', 'od_b', 'od_amount')
    search_fields = ('od_o__o_u__u_name',)


admin.site.register(Users, UsersAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Classes, ClassAdmin)
admin.site.register(Orderdetails, OrderdetailsAdmin)
admin.site.register(Orders, OrdersAdmin)
