# -*- coding:utf8 -*-
###########################################
# File: GetSms.py
# Desc: 获取短信验证码
# Author: zhangyufeng
# History: 2016/3/7 zhangyufeng 新建
###########################################
import redis
from mysql import connector


class GetSms(object):
    def __init__(self, redis_host=None, redis_port=6379, redis_password=None, mysql_user=None, mysql_host=None,
                 mysql_port=3306, mysql_password=None, mysql_db=None):
        self.__redis_host = redis_host
        self.__redis_port = redis_port
        self.__redis_password = redis_password
        self.__mysql_user = mysql_user
        self.__mysql_host = mysql_host
        self.__mysql_port = mysql_port
        self.__mysql_password = mysql_password
        self.__mysql_db = mysql_db

    def get_sms_num_from_redis(self, redis_key_phone_number):
        r = redis.StrictRedis(host=self.__redis_host, port=self.__redis_port, password=self.__redis_password)
        redis_key = str(redis_key_phone_number) + "authUserSendCode"
        # 由于取验证码时获取的是二进制数据，所以字符串化以后切片取值
        redis_value = str(r.get(redis_key))
        sms_num = redis_value[-5:-1]
        return sms_num

    def get_sms_num_from_db(self, redis_key_phone_number):
        select_sql = "select sms_content from member_sms_log where sms_phone=" + str(
            redis_key_phone_number) + " order by log_id desc"
        m = connector.connect(user=self.__mysql_user, password=self.__mysql_password, host=self.__mysql_host,
                              port=self.__mysql_port, database=self.__mysql_db)
        cursor = m.cursor()
        cursor.execute(select_sql)
        sms_num_list = list()
        for (num,) in cursor:
            sms_num_list.append(num)
        cursor.close()
        m.close()
        sms_num = sms_num_list[0]
        return sms_num
