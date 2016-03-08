# coding=utf-8
from common.util.logger import logger
import pytest

# class Main(object):
#     try:
#         tmp_var = 1 + "1"
#         logger.debug(tmp_var)
#     except:
#         logger.exception("捕获到错误")
pytest.main("-s -v ./test/test_template.py --html=./logs/report.html")
