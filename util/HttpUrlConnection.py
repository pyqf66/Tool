# coding=utf-8
###########################################
# File: HttpUrlConnection.py
# Desc: http接口工具类
# Author: zhangyufeng
# History: 2015/11/15 zhangyufeng 新建
###########################################
import http
from http import client
import urllib
import simplejson

from util.logger import logger


class HttpUrlConnection(object):
    u''' 
        methon为请求方法
        parameter为请求参数
        cookie为获取的cookie
        headers为请求头
    '''

    # 处理预置数据
    def __init__(self, url, method="GET", parameters=None, cookie=None, headers={}):
        try:
            # 解析url
            if type(url) == bytes:
                self.__url = url.decode("utf-8")
            if type(url) == str:
                self.__url = url
            logger.debug(self.__url)
            scheme, rest = urllib.parse.splittype(self.__url)
            # 拆分域名和路径
            logger.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            self.__host_absolutely, self.__path = urllib.parse.splithost(rest)
            host_list = self.__host_absolutely.split(":")
            if len(host_list) == 1:
                self.__host = host_list[0]
                self.__port = 80
            elif len(host_list) == 2:
                self.__host = host_list[0]
                self.__port = host_list[1]
            # 对所传参数进行处理
            self.__method = method
            self.__data = parameters
            self.__cookie = cookie
            if parameters != None:
                self.__parameters_urlencode_deal = urllib.parse.urlencode(parameters)
            else:
                self.__parameters_urlencode_deal = ""
            self.__jdata = simplejson.dumps(parameters, ensure_ascii=False)
            self.__headers = headers
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 发送普通请求,要求完全满足http协议规则
    def request(self):
        try:
            conn = client.HTTPConnection(self.__host, self.__port)
            if self.__method == "GET":
                self.path = self.__path + self.__parameters_urlencode_deal
                conn.request(self.__method, self.__path)
            if self.__method == "POST":
                if self.__headers == {"Content-type": "application/json"}:
                    conn.request(self.__method, self.__path, self.__jdata, self.__headers)
                if self.__headers == {"Content-type": "application/x-www-form-urlencoded"}:
                    conn.request(self.__method, self.__path, self.__data, self.__headers)

            response = conn.getresponse()
            result_origin = response.read()
            try:
                result = result_origin.decode("gb2312").encode("utf8")
            except:
                result = result_origin
            return result
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 使用urllib.request发送带cookie的请求
    def request_with_cookies(self):
        try:
            cookiejar = http.CookieJar()
            cookiejar.set_cookie(self.__cookie)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
            if self.__data is None:
                request = urllib.request.Request(self.__url)
            else:
                request = urllib.request.Request(self.__url, self.__data)
            html = opener.open(request).read()
            return html
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 提供外部host数据    
    def get_host(self):
        try:
            return self.__host
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 提供外部path数据
    def get_path(self):
        try:
            return self.__path
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")

    # 提供外部经过ulrencode处理后的数据
    def get_parameters_urlencode_deal(self):
        try:
            return self.__parameters_urlencode_deal
        except Exception as e:
            logger.error(e)
            logger.exception(u"捕获到错误如下:")
