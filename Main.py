# coding=utf-8
from util.logger import logger

class Main(object):
    try:
        tmp_var = 1 + "1"
        logger.debug(tmp_var)
    except:
        logger.exception("捕获到错误")