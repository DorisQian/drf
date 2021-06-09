# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/9 19:33
@Auth ： Doris
错误信息配置
"""

SUCCESS = [0000, 'OK']
NO_DATA = [1001, '数据不存在']
NO_PARAM = [1002, '缺少传参']


def get_message(message_config=None, data=None):
    if message_config is None:
        message_config = SUCCESS
    if data is None:
        data = []
    response_json = {
        'code': message_config[0],
        'message': message_config[1],
        'data': data
    }
    return response_json
