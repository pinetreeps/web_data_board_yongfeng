# _*_ coding:utf-8 _*_

import json

# json格式检查工具
def is_json(json_str):
    try:
        json_object = json.loads(json_str)
        json_object
    except ValueError as e:
        print(repr(e))
        return False
    return True
