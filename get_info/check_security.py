# _*_ coding:utf-8 _*_
# Filename: check_security.py
# Author: pang song
# python 3.6
# Date: 2019/06/18

# 安防信息处理接口

import logging
from utils import mysql_utils

logger = logging.getLogger("main")

def dict_assignment(default_dict, data_dict, value='unknown'):
    # 字典赋值，为空设为默认
    for k in default_dict.keys():
        # print(data_dict[k])
        if data_dict.get(k):
            # print(data_dict.get(k))
            default_dict[k] = data_dict.get(k)
        else:
            default_dict[k] = value
    return default_dict


def save_security_msg(data_dict):
    '''

    :param data_dict:
    :return:
    '''
    save_dict = {'security_time':'unknown',
                 'device_id':'unknown',
                 'device_name':'unknown',
                 'security_msg':'unknown',
                 'security_level':'unknown',
                 'security_state':'unknown'}

    save_dict = dict_assignment(save_dict, data_dict)

    data_conn = mysql_utils.Database()
    sql1 = """
            INSERT INTO  yf_bim_security_msg (security_time,device_id,device_name,security_msg,security_level,security_state,ctime, utime) 
            VALUES ('{st}', '{di}', '{dn}', '{sm}', '{sl}', '{ss}', now(), now());
          """.format(st=save_dict['security_time'],
                     di=save_dict['device_id'],
                     dn=save_dict['device_name'],
                     sm=save_dict['security_msg'],
                     sl=save_dict['security_level'],
                     ss=save_dict['security_state'])
    data_conn.insert_del_update(sql1)
    logger.info('save data success')


def get_security_msg():
    '''

    :param data_dict:
    :return:
    '''
    return_list = []

    data_conn = mysql_utils.Database()
    sql1 = "select * from yf_bim_security_msg where security_state = '0' order by utime desc"
    rows = data_conn.query_all(sql1)
    # logger.debug('unity_id:{a}, wlw_id and name :{b}'.format(a=unity_id, b=row1))
    # print(rows)
    for row in rows:
        logger.debug(row)
        return_dict = {
            'security_id': '',
            'security_time': '',
            'device_id': '',
            'device_name': '',
            'security_msg': '',
            'security_level': '',
            'security_state': ''
        }
        return_dict['security_id'] = row[0]
        return_dict['security_time'] = row[1]
        return_dict['device_id'] = row[2]
        return_dict['device_name'] = row[3]
        return_dict['security_msg'] = row[4]
        return_dict['security_level'] = row[5]
        return_dict['security_state'] = row[6]
        return_list.append(return_dict)

    return {'security_msg_list':return_list}

def update_security_msg(data_dict):
    '''

    :param data_dict:
    :return:
    '''
    save_dict = {
        'security_id':'unknown',
        'security_update_code':'0',
    }
    save_dict = dict_assignment(save_dict, data_dict)
    return_label = False

    data_conn = mysql_utils.Database()
    sql1 = """
            UPDATE yf_bim_security_msg SET security_state='{ss}', utime = now() where id = {si};
          """.format(si=int(save_dict['security_id']),
                     ss=save_dict['security_update_code'])
    try:
        data_conn.insert_del_update(sql1)
        return_label = True
    except Exception as e:
        logger.error(repr(e))
    logger.info('update success')
    return return_label

if __name__ == '__main__':
    print('aaa')
    dict1 = {'security_time': '',
                 'device_id': '',
                 'device_name': '',
                 'security_msg': '',
                 'security_level': '',
                 'security_state': ''}

    dict2 = {'security_time': '2019-06-17',
                 'device_id': '9123',
                 'device_name': '厕所2',
                 'security_msg': '空调异常3',
                 'security_level': '1',
                 'security_state': '1'}
    # print(dict_assignment(dict1, dict2, 'unk'))
    save_dict = {
        'security_id': '1',
        'security_update_code': '1',
    }
    update_security_msg(save_dict)

    exit()



    # save_security_msg(dict2)
    data = get_security_msg()
    print(len(data['security_msg_list']))
    print(data)
    for ddd in data['security_msg_list']:
        print(ddd)