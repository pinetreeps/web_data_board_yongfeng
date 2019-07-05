# _*_ coding:utf-8 _*_

import json, logging

logger = logging.getLogger('main')
# json格式检查工具
def is_json(json_str):
    try:
        # json_object = json.loads(json_str, strict=False)
        json_object = json.loads(json_str)
        json_object
    except Exception as e:
        # ValueError as e:
        logger.error(repr(e))
        return False
    return True


if __name__ == '__main__':
    # print(is_json('{"security_time":"2019-06-19 23:39:01","device_id":"f1_16_102_bp_bj","device_name":"B5项目一层库房102的防区16的玻璃破碎探测器报警","security_msg":"高报","security_level":"低级","security_state":"未确认"  \n} , \n'))
    json_str = '{"security_time":"2019-06-19 23:39:01","device_id":"f1_16_102_bp_bj","device_name":"B5项目一层库房102的防区16的玻璃破碎探测器报警","security_msg":"高报","security_level":"低级","security_state":"未确认"  \n} , \n'
    json.loads(json_str)