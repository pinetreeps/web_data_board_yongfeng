# _*_ coding:utf-8 _*_
# Filename: check_info_wlw.py
# Author: pang song
# python 2.7
# Date: 2019/06/09

# import urllib
import urllib2
import logging
import json
from utils.post_json import post_json
from utils import mysql_utils

logger = logging.getLogger("main")


def get_wlw_id_by_unity_id(unity_id):
    '''
    get name by check_id
    :return: name
    '''
    wlw_id = ''
    bim_name = ''
    data_conn = mysql_utils.Database()
    sql1 = "select wlw_id, name from yf_bim_unity_wlw_id_check where unity_id = '{unid}'".format(unid=unity_id)
    row1 = data_conn.query_one(sql1)
    logger.debug('unity_id:{a}, wlw_id and name :{b}'.format(a=unity_id, b=row1))
    print(row1)
    if row1 != None:
        wlw_id = row1[0]
        bim_name = row1[1]
    return wlw_id, bim_name



def get_info_wlw(url, post_data_json):
    '''
    check info from wlw, direct get return data which is string of json
    :param url: wlw url
    :param post_data_json: string in json
    :return: wlw return json data
    '''
    return_json =  post_json(data='物联网数据获取失败')
    try:
        req = urllib2.Request(url=url, data=post_data_json)
        # print req
        res_data = urllib2.urlopen(req)

        return_json = res_data.read()
        logger.debug('wlw return json: {}'.format(return_json))
        return_json = return_json.replace('"code": "0"','"code": 0').replace('succes', 'success').replace('-9999.0', '')
    except Exception as e:
        logger.error('get data error, {}'.format(repr(e)))
    logger.debug('replaced return json: {}'.format(return_json))

    return return_json

# def get_info_wlw_change_id(url, web_data_dict):


if __name__ == '__main__':
    print(get_wlw_id_by_unity_id('room_a1f101'))
    exit()


    test_url = 'http://39.105.61.38:8291/env_indoor_history'
    test_data = {
        "uid":"b58f6e1d-e0cd-11e8-98ce-00163e10c840",
        "position_id":"1",
        "data_type":"day"
    }

    req = urllib2.Request(url = test_url,data =json.dumps(test_data))
    # print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    # json str
    # print res