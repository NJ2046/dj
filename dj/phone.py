# coding:utf-8
import http.client as httplib
import urllib
 
host = '106.ihuyi.com'
sms_send_uri = '/webservice/sms.php?method=Submit'
 
account = 'C27007733'
password = 'd3d853951f272af55caa41df8a4e2db7'


def send_sms(v_code, mobile):
    params = urllib.parse.urlencode({'account': account, 'password' : password, 'content': v_code, 'mobile':mobile,'format':'json' })
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = '18903911198'
    text = "您的验证码是：5201314。请不要把验证码泄露给其他人。"
    print(send_sms(text, mobile))
