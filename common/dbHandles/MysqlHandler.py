# -*- coding:utf-8 -*-
from mysql import connector


class MysqlHandler(object):
    def __init__(self, mysql_user=None, mysql_host=None, mysql_port=3306, mysql_password=None, mysql_db=None):
        self.__mysql_user = mysql_user
        self.__mysql_host = mysql_host
        self.__mysql_port = mysql_port
        self.__mysql_password = mysql_password
        self.__mysql_db = mysql_db

    def get_mysql_data(self, sql):
        '''
        :param sql: sql语句
        :return: 返回结果list，每组结果存在一个元组里
        '''
        mysql_object = connector.connect(user=self.__mysql_user, password=self.__mysql_password, host=self.__mysql_host,
                              port=self.__mysql_port, database=self.__mysql_db)
        cursor = mysql_object.cursor()
        cursor.execute(sql)
        data_list = list()
        for data in cursor:
            data_list.append(data)
        cursor.close()
        mysql_object.close()
        return data_list
