# _*_ coding:utf-8 _*_
import json

# json格式化函数
def post_json(code=1, msg='error', data=''):
    json_dict = dict(
        code=code,
        msg=msg,
        data=data,
    )
    return json.dumps(json_dict, ensure_ascii=False)
