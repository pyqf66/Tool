#!/usr/bin/env python
# coding=utf-8
###########################################
# File: crmMock.py
# Desc: crmMock视图层
# Author: 张羽锋
# History: 2015/12/28 张羽锋 新建
###########################################

from util.logger import logger


# 大悦城数据字典
def ytdycDict(cardno, datetime_str_register, salesamt, datetime_str_buy):
    try:
        ytdyc_data = dict()
        ytdyc_data["card_no"] = cardno
        ytdyc_data["vipcardno"] = ""
        ytdyc_data["jointdate"] = datetime_str_register
        ytdyc_data["openid"] = ""
        ytdyc_data["points_flag"] = "0"
        ytdyc_data["score_type"] = "1"
        ytdyc_data["score"] = "13"
        ytdyc_data["time"] = datetime_str_buy
        ytdyc_data["salesamt"] = salesamt
        ytdyc_data["storecode"] = "1FD151"
        ytdyc_data["storename"] = u"奢侈品眼镜"
        return ytdyc_data
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")


def oyjtDict(amount, orderDate):
    try:
        oyjt_data = dict()
        oyjt_data["orderID"] = "307900"
        oyjt_data["orderPoint"] = "3.104"
        oyjt_data["mallName"] = "欧亚卖场"
        oyjt_data["storeName"] = "欧亚卖场"
        oyjt_data["productName"] = "辉山小枕240ml"
        oyjt_data["quantity"] = "16"
        oyjt_data["unitPice"] = "1.94"
        oyjt_data["amount"] = amount
        oyjt_data["orderDate"] = orderDate
        return oyjt_data
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
