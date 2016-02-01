# coding=utf-8
###########################################
# File: logger.py
# Desc: 日志工具类
# Author: zhangyufeng
# History: 2016/1/28 zhangyufeng 新建
###########################################
import os
import platform
import logging
import logging.config

# 定义文件路径常量
BASE_CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = BASE_CURRENT_DIR
if platform.system() == "Windows":
    BASE_DIR = BASE_CURRENT_DIR.replace("\\", "/")
LOGGING_CONF_DIR = os.path.join(BASE_DIR + "/conf/", "logging.conf")
LOGS_DIR = BASE_DIR + "/logs/"
ALL_DIR = LOGS_DIR + "all.log"
FILE_DIR = LOGS_DIR + "file.log"

# 判断文件是否存在，不存在则建立
if os.path.exists(ALL_DIR):
    pass
else:
    f = open(ALL_DIR, 'a')
    f.close()

if os.path.exists(FILE_DIR):
    pass
else:
    f = open(FILE_DIR, 'a')
    f.close()

# 读取配置文件并建立日志对象
logging.config.fileConfig(LOGGING_CONF_DIR)
logger = logging.getLogger()
