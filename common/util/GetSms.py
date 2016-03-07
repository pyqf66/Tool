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
    def __init__(self, REDIS_HOST=None, REDIS_PORT=6379, REDIS_PASSWORD=None, MYSQL_USER=None, MYSQL_HOST=None,
                 MYSQL_PORT=3306, MYSQL_PASSWORD=None, MYSQL_DB=None):
        self.__redis_host = REDIS_HOST
        self.__redis_port = REDIS_PORT
        self.__redis_password = REDIS_PASSWORD
        self.__mysql_user = MYSQL_USER
        self.__mysql_host = MYSQL_HOST
        self.__mysql_port = MYSQL_PORT
        self.__mysql_password = MYSQL_PASSWORD
        self.__mysql_db = MYSQL_DB

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
