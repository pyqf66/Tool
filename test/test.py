# coding=utf-8
from http import cookiejar
import urllib.parse
import urllib.request
from util.HttpUrlConnection import HttpUrlConnection

post_data = {'username': 'admin@suolong', 'password': '123456'}
# post_data_urlencode = urllib.parse.urlencode(post_data).encode("utf-8")
loginUrl = "http://test2.ishop-city.com/reconciliation/admin/user/login.json"
testUrl = 'http://test2.ishop-city.com/reconciliation/repayCheck/gethuizong.json'
# cj = cookiejar.CookieJar()
# openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# 伪装成一个正常的浏览器，避免有些web服务器拒绝访问。
# openner.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
# tmp1 = openner.open(loginUrl, post_data_urlencode)
# tmp2 = openner.open(testUrl)
# print(tmp2.readlines())

# 查看具体的值
# for cookiedata in enumerate(cj):
#     print cookiedata[1]

http_object = HttpUrlConnection( get_cookie_url=loginUrl, get_cookie_request_data=post_data)
result=http_object.request_with_cookies(url=testUrl)
print(result.readlines())
