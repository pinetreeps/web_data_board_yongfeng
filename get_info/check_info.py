# _*_ coding:utf-8 _*_
# Filename: check_info.py
# Author: pang song
# python 3.6
# Date: 2018/12/26
'''
三、信息接口
'''
# --------------1、项目概况模块 ------------------

'''
园区概况
占地面积	29450
建筑数量	8
总建筑面积	58900
容积率	2.0
绿地率	30
入驻企业统计	345
园区人员统计	4589
招商企业分析	239
'''

def get_area_overview():
    '''
    查询园区概况
    :return: dict
    '''
    # # 测试数据
    test_data_area_overview = {
        "land_area": "29450",
        "buildings_amount": "8",
        "buildings_area": "58900",
        "floor_area_ratio": "2.0",
        "greening_rate": "30",
        "company_amount": "345",
        "area_people_amount": "4589",
        "companys_ratio": [
            {
                "ratio_name": "高科技企业",
                "ratio_value": "5"
            },
            {
                "ratio_name": "其他企业",
                "ratio_value": "1"
            }]
    }
    return test_data_area_overview

'''
建筑概况
建筑名称	永丰B5综合服务楼
使用功能	综合服务楼
建筑面积	7643m²
建筑高度	25m
建筑时间	2018
建筑层数	5
'''

def get_building_overview():
    '''
    查询建筑概况
    :return: dict
    '''
    # # 测试数据
    test_data_building_overview = {
        "building_name":"永丰B5综合服务楼",
        "building_function":"综合服务楼",
        "building_area":"7643",
        "building_time":"2018",
        "building_height":"25",
        "building_floors":"5"
    }
    return test_data_building_overview


def get_env_outdoor():
    '''
    查询室外环境 实时
    :return: dict

    '''
    # # 测试数据
    test_data_env_outdoor = {
        "temperature":"-6",
        "humidity":"15",
        "wind_direction":"东南",
        "wind_speed":"1.2",
        "precipitation":"0",
        "air_pressure":"102.3",
        "pm2.5":"120"
    }
    return test_data_env_outdoor

def env_outdoor_history(data_type):
    '''
        查询室外环境 历史数据
        :return: dict

        '''
    # # 测试数据
    test_data_env_outdoor_history = {}
    if 'year' == data_type:
        test_data_env_outdoor_history = {
            "data_list":[
            {"data_time": "1", "temperature_high":"5", "temperature_low":"-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
            {"data_time": "2", "temperature_high":"8", "temperature_low":"-8", "humidity": "40", "wind_speed": "1.2", "precipitation": "20", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "3", "temperature_high":"13", "temperature_low":"0", "humidity": "40", "wind_speed": "1.2", "precipitation": "100", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "4", "temperature_high":"20", "temperature_low":"1", "humidity": "40", "wind_speed": "1.2", "precipitation": "200", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "5", "temperature_high":"26", "temperature_low":"16", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "6", "temperature_high":"28", "temperature_low":"18", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "7", "temperature_high":"30", "temperature_low":"22", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "8", "temperature_high":"35", "temperature_low":"22", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "9", "temperature_high":"34", "temperature_low":"18", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "10", "temperature_high":"26", "temperature_low":"16", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3",   "pm2.5": "120"},
            {"data_time": "11", "temperature_high":"16", "temperature_low":"8", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3",   "pm2.5": "500"},
            {"data_time": "12", "temperature_high":"7", "temperature_low":"-6", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3",   "pm2.5": "420"},
            ]
        }
    elif 'month' == data_type:
        test_data_env_outdoor_history = {
            "data_list": [
                {"data_time": "1", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "2", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "3", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "4", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "5", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "6", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "7", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "8", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "9", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "10", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "11", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "12", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "13", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "14", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "15", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "16", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "17", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "18", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "19", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "20", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "21", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "22", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "23", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "24", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "25", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "26", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "27", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "28", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "29", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "30", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
            ]
        }

    elif 'day' == data_type:
        test_data_env_outdoor_history = {
            "data_list": [
                {"data_time": "1", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "2", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "3", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "4", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "5", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "6", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "7", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "8", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "9", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "10", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "11", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "12", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "13", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "14", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "15", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "16", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "17", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "18", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "19", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "20", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "21", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "22", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "23", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
                {"data_time": "0", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "320"},
            ]
        }
    return test_data_env_outdoor_history

def get_env_indoor(position_id):
    '''
    查询室内环境 实时
    :return: dict

    '''
    # # 测试数据
    test_data = {
        "position_name":"1号楼{}位置".format(position_id),
        "temperature":"26",
        "humidity":"40",
        "voc":"0",
        "pm2.5":"120"
    }
    return test_data


def env_indoor_history(position_id, data_type):
    '''
    查询室内环境 历史数据
    :return: dict
    '''
    # # 测试数据
    test_data_env_indoor_history = {}
    if 'year' == data_type:
        test_data_env_indoor_history = {
            "position_name": "位置在{}".format(position_id),
            "data_list":[
            {"data_time": "1", "temperature_high":"5", "temperature_low":"-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
            {"data_time": "2", "temperature_high":"8", "temperature_low":"-8", "humidity": "40", "wind_speed": "1.2", "precipitation": "20", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "120"},
            {"data_time": "3", "temperature_high":"13", "temperature_low":"0", "humidity": "40", "wind_speed": "1.2", "precipitation": "100", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "120"},
            {"data_time": "4", "temperature_high":"20", "temperature_low":"1", "humidity": "40", "wind_speed": "1.2", "precipitation": "200", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "120"},
            {"data_time": "5", "temperature_high":"26", "temperature_low":"16", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "120"},
            {"data_time": "6", "temperature_high":"28", "temperature_low":"18", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "120"},
            {"data_time": "7", "temperature_high":"30", "temperature_low":"22", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "120"},
            {"data_time": "8", "temperature_high":"35", "temperature_low":"22", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "120"},
            {"data_time": "9", "temperature_high":"34", "temperature_low":"18", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "120"},
            {"data_time": "10", "temperature_high":"26", "temperature_low":"16", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "120"},
            {"data_time": "11", "temperature_high":"16", "temperature_low":"8", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "500"},
            {"data_time": "12", "temperature_high":"7", "temperature_low":"-6", "humidity": "40", "wind_speed": "1.2", "precipitation": "300", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "420"},
            ]
        }
    elif 'month' == data_type:
        test_data_env_indoor_history = {
            "position_name": "位置在{}".format(position_id),
            "data_list": [
                {"data_time": "1", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "2", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "3", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "4", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "5", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "6", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "7", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "8", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "9", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "10", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "11", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "12", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "13", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "14", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "15", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "16", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "17", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "18", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "19", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "20", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "21", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "22", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "23", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "24", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "25", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "26", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "27", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "28", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "29", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "30", "temperature_high": "5", "temperature_low": "-10", "humidity": "40", "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
            ]
        }

    elif 'day' == data_type:
        test_data_env_indoor_history = {
            "position_name": "位置在{}".format(position_id),
            "data_list": [
                {"data_time": "1", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "2", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "3", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "4", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "5", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "6", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "7", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "8", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "9", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "10", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "11", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "12", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "13", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "14", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "15", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "16", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "17", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "18", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "19", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "20", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "21", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "22", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "23", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
                {"data_time": "0", "temperature_high": "5", "temperature_low": "-10", "humidity": "40",
                 "wind_speed": "1.2", "precipitation": "10", "air_pressure": "102.3", "voc":"2.7", "pm2.5": "320"},
            ]
        }
    return test_data_env_indoor_history

def get_energy_overview(check_id):
    '''
    查询用能概况
    :return: dict
    '''
    # # 测试数据
    test_data = {
        "check_name":"{}用能情况".format(check_id),
        "electricity":[
            {
                "time":"周一",
                "value_list":[{"name":"建筑","value":"231",},{"name":"空调", "value":"3523",},{"name":"电器","value":"2223",},{"name":"其他","value":"1123",},],
            },
            {
                "time": "周二",
                "value_list": [{"name": "建筑", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周三",
                "value_list": [{"name": "建筑", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周四",
                "value_list": [{"name": "建筑", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周五",
                "value_list": [{"name": "建筑", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周六",
                "value_list": [{"name": "建筑", "value": "31", }, {"name": "空调", "value": "33", },
                               {"name": "电器", "value": "2223", }, {"name": "其他", "value": "3", }, ],
            },
            {
                "time": "周日",
                "value_list": [{"name": "建筑", "value": "10", }, {"name": "空调", "value": "23", },
                               {"name": "电器", "value": "20", }, {"name": "其他", "value": "23", }, ],
            },

        ],
        "gas":[
            {
                "time":"周一",
                "value_list":[{"name":"采暖","value":"231",},{"name":"厨房", "value":"3523",},{"name":"其他","value":"1123",},],
            },
            {
                "time": "周二",
                "value_list": [{"name":"采暖","value":"231",},{"name":"厨房", "value":"3523",},{"name":"其他","value":"1123",},],
            },
            {
                "time": "周三",
                "value_list": [{"name":"采暖","value":"231",},{"name":"厨房", "value":"3523",},{"name":"其他","value":"1123",},],
            },
            {
                "time": "周四",
                "value_list": [{"name":"采暖","value":"231",},{"name":"厨房", "value":"3523",},{"name":"其他","value":"1123",},],
            },
            {
                "time": "周五",
                "value_list": [{"name":"采暖","value":"231",},{"name":"厨房", "value":"3523",},{"name":"其他","value":"1123",},],
            },
            {
                "time": "周六",
                "value_list": [{"name":"采暖","value":"21",},{"name":"厨房", "value":"3",},{"name":"其他","value":"11",},],
            },
            {
                "time": "周日",
                "value_list": [{"name":"采暖","value":"31",},{"name":"厨房", "value":"52",},{"name":"其他","value":"12",},],
            },

        ],
        "water":[
            {
                "time":"周一",
                "value_list":[{"name":"生活","value":"231",},{"name":"空调", "value":"3523",},{"name":"厨房","value":"2223",},{"name":"其他","value":"1123",},],
            },
            {
                "time": "周二",
                "value_list": [{"name": "生活", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "厨房", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周三",
                "value_list": [{"name": "生活", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "厨房", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周四",
                "value_list": [{"name": "生活", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "厨房", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周五",
                "value_list": [{"name": "生活", "value": "231", }, {"name": "空调", "value": "3523", },
                               {"name": "厨房", "value": "2223", }, {"name": "其他", "value": "1123", }, ],
            },
            {
                "time": "周六",
                "value_list": [{"name": "生活", "value": "31", }, {"name": "空调", "value": "33", },
                               {"name": "厨房", "value": "2223", }, {"name": "其他", "value": "3", }, ],
            },
            {
                "time": "周日",
                "value_list": [{"name": "生活", "value": "10", }, {"name": "空调", "value": "23", },
                               {"name": "厨房", "value": "20", }, {"name": "其他", "value": "23", }, ],
            },

        ],
    }
    return test_data


def get_energy_electricity_overview(check_id):
    '''
    用电情况通用查询接口1，使用唯一id进行查询，园区用电、建筑用电返回各建筑、各层用电占比
    :return: dict
    '''
    # # 测试数据
    test_data = {
        "check_name":"永丰B5综合服务楼 {}".format(check_id),
        "electricity":"178",
        "history_year_list":[
            {"history_time": "1", "history_value":"326" },
            {"history_time": "2", "history_value":"226" },
            {"history_time": "3", "history_value":"76" },
            {"history_time": "4", "history_value":"126" },
            {"history_time": "5", "history_value":"326" },
            {"history_time": "6", "history_value":"426" },
            {"history_time": "7", "history_value":"626" },
            {"history_time": "8", "history_value":"596" },
            {"history_time": "9", "history_value":"86" },
            {"history_time":"10", "history_value":"126" },
            {"history_time":"11", "history_value":"156" },
            {"history_time":"12", "history_value":"526" },
        ],
        "history_month_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "526"},
            {"history_time": "19", "history_value": "526"},
            {"history_time": "20", "history_value": "326"},
            {"history_time": "21", "history_value": "426"},
            {"history_time": "22", "history_value": "526"},
            {"history_time": "23", "history_value": "526"},
            {"history_time": "24", "history_value": "526"},
            {"history_time": "25", "history_value": "526"},
            {"history_time": "26", "history_value": "526"},
            {"history_time": "27", "history_value": "526"},
            {"history_time": "28", "history_value": "526"},
            {"history_time": "29", "history_value": "526"},
            {"history_time": "30", "history_value": "526"},
        ],
        "history_day_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "426"},
            {"history_time": "19", "history_value": "436"},
            {"history_time": "20", "history_value": "526"},
            {"history_time": "21", "history_value": "226"},
            {"history_time": "22", "history_value": "126"},
            {"history_time": "23", "history_value": "226"},
            {"history_time": "0", "history_value": "26"},
        ],
        "electricity_ratio1":[
            {"ratio_id":"floor01", "ratio_name":"1号楼*层01房间", "ratio_value":"45"},
            {"ratio_id":"floor02", "ratio_name":"1号楼*层02房间", "ratio_value":"85"},
            {"ratio_id":"floor03", "ratio_name":"1号楼*层03房间", "ratio_value":"95"},
            {"ratio_id":"floor04", "ratio_name":"1号楼*层04房间", "ratio_value":"25"},
            {"ratio_id":"floor05", "ratio_name":"1号楼*层05房间", "ratio_value":"15"},
        ],
        "electricity_ratio2": [
            {"ratio_id": "b01","ratio_name": "照明","ratio_value": "345"},
            {"ratio_id": "b02","ratio_name": "空调","ratio_value": "3145"},
            {"ratio_id": "b03","ratio_name": "电器","ratio_value": "1345"},
            {"ratio_id": "b03","ratio_name": "其他","ratio_value": "145"},
        ]
    }
    return test_data


def get_energy_electricity(check_id):
    '''
    用电情况通用查询接口2，使用唯一id 查询设备用电（空调、电器）
    :return: dict
    '''
    # # 测试数据
    test_data = {
        "check_name":"设备用电 {}".format(check_id),
        "electricity":"178",
        "history_year_list":[
            {"history_time": "1", "history_value":"326" },
            {"history_time": "2", "history_value":"226" },
            {"history_time": "3", "history_value":"76" },
            {"history_time": "4", "history_value":"126" },
            {"history_time": "5", "history_value":"326" },
            {"history_time": "6", "history_value":"426" },
            {"history_time": "7", "history_value":"626" },
            {"history_time": "8", "history_value":"596" },
            {"history_time": "9", "history_value":"86" },
            {"history_time":"10", "history_value":"126" },
            {"history_time":"11", "history_value":"156" },
            {"history_time":"12", "history_value":"526" },
        ],
        "history_month_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "526"},
            {"history_time": "19", "history_value": "526"},
            {"history_time": "20", "history_value": "326"},
            {"history_time": "21", "history_value": "426"},
            {"history_time": "22", "history_value": "526"},
            {"history_time": "23", "history_value": "526"},
            {"history_time": "24", "history_value": "526"},
            {"history_time": "25", "history_value": "526"},
            {"history_time": "26", "history_value": "526"},
            {"history_time": "27", "history_value": "526"},
            {"history_time": "28", "history_value": "526"},
            {"history_time": "29", "history_value": "526"},
            {"history_time": "30", "history_value": "526"},
        ],
        "history_day_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "426"},
            {"history_time": "19", "history_value": "436"},
            {"history_time": "20", "history_value": "526"},
            {"history_time": "21", "history_value": "226"},
            {"history_time": "22", "history_value": "126"},
            {"history_time": "23", "history_value": "226"},
            {"history_time": "0", "history_value": "26"},
        ]
    }
    return test_data

def get_energy_gas(check_id):
    '''
    查询用气情况
    :return: dict
    '''
    # # 测试数据
    test_data = {
        "check_name":"设备用气 {}".format(check_id),
        "ac_gas": {
            "class_name": "采暖用气",
            "history_year_list":[
                {"history_time": "1", "history_value":"326" },
                {"history_time": "2", "history_value":"226" },
                {"history_time": "3", "history_value":"76" },
                {"history_time": "4", "history_value":"126" },
                {"history_time": "5", "history_value":"326" },
                {"history_time": "6", "history_value":"426" },
                {"history_time": "7", "history_value":"626" },
                {"history_time": "8", "history_value":"596" },
                {"history_time": "9", "history_value":"86" },
                {"history_time":"10", "history_value":"126" },
                {"history_time":"11", "history_value":"156" },
                {"history_time":"12", "history_value":"526" },
            ],
            "history_month_list":[
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list":[
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ]
        },
        "kitchen_gas": {
            "class_name": "厨房用气",
            "history_year_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
            ],
            "history_month_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ]
        }
    }
    return test_data

def get_energy_water_overview(check_id):
    '''
    查询用气情况
    :return: dict
    '''
    # # 测试数据
    test_data = {
        "check_name":"{} 用水总览".format(check_id),
        "live_water": {
            "class_name": "生活用水",
            "history_year_list":[
                {"history_time": "1", "history_value":"326" },
                {"history_time": "2", "history_value":"226" },
                {"history_time": "3", "history_value":"76" },
                {"history_time": "4", "history_value":"126" },
                {"history_time": "5", "history_value":"326" },
                {"history_time": "6", "history_value":"426" },
                {"history_time": "7", "history_value":"626" },
                {"history_time": "8", "history_value":"596" },
                {"history_time": "9", "history_value":"86" },
                {"history_time":"10", "history_value":"126" },
                {"history_time":"11", "history_value":"156" },
                {"history_time":"12", "history_value":"526" },
            ],
            "history_month_list":[
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list":[
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ],
            "ratio_list":[
                {"ratio_id":"floor01", "ratio_name":"1号楼*层01房间", "ratio_value":"45"},
                {"ratio_id":"floor02", "ratio_name":"1号楼*层02房间", "ratio_value":"85"},
                {"ratio_id":"floor03", "ratio_name":"1号楼*层03房间", "ratio_value":"95"},
                {"ratio_id":"floor04", "ratio_name":"1号楼*层04房间", "ratio_value":"25"},
                {"ratio_id":"floor05", "ratio_name":"1号楼*层05房间", "ratio_value":"15"},
            ]
        },
        "kitchen_water": {
            "class_name": "厨房用水",
            "history_year_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
            ],
            "history_month_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ],
            "ratio_list": [
                {"ratio_id": "floor01", "ratio_name": "1号厨房", "ratio_value": "45"},
                {"ratio_id": "floor02", "ratio_name": "2号厨房", "ratio_value": "85"},
            ]
        },
        "ac_water": {
            "class_name": "空调用水",
            "history_year_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
            ],
            "history_month_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "526"},
                {"history_time": "19", "history_value": "526"},
                {"history_time": "20", "history_value": "326"},
                {"history_time": "21", "history_value": "426"},
                {"history_time": "22", "history_value": "526"},
                {"history_time": "23", "history_value": "526"},
                {"history_time": "24", "history_value": "526"},
                {"history_time": "25", "history_value": "526"},
                {"history_time": "26", "history_value": "526"},
                {"history_time": "27", "history_value": "526"},
                {"history_time": "28", "history_value": "526"},
                {"history_time": "29", "history_value": "526"},
                {"history_time": "30", "history_value": "526"},
            ],
            "history_day_list": [
                {"history_time": "1", "history_value": "326"},
                {"history_time": "2", "history_value": "226"},
                {"history_time": "3", "history_value": "76"},
                {"history_time": "4", "history_value": "126"},
                {"history_time": "5", "history_value": "326"},
                {"history_time": "6", "history_value": "426"},
                {"history_time": "7", "history_value": "626"},
                {"history_time": "8", "history_value": "596"},
                {"history_time": "9", "history_value": "86"},
                {"history_time": "10", "history_value": "126"},
                {"history_time": "11", "history_value": "156"},
                {"history_time": "12", "history_value": "526"},
                {"history_time": "13", "history_value": "526"},
                {"history_time": "14", "history_value": "526"},
                {"history_time": "15", "history_value": "526"},
                {"history_time": "16", "history_value": "526"},
                {"history_time": "17", "history_value": "526"},
                {"history_time": "18", "history_value": "426"},
                {"history_time": "19", "history_value": "436"},
                {"history_time": "20", "history_value": "526"},
                {"history_time": "21", "history_value": "226"},
                {"history_time": "22", "history_value": "126"},
                {"history_time": "23", "history_value": "226"},
                {"history_time": "0", "history_value": "26"},
            ]
        }
    }
    return test_data

def get_energy_check_hot(check_id):
    '''
    用电情况通用查询接口2，使用唯一id 查询设备用电（空调、电器）
    :return: dict
    '''
    # # 测试数据
    test_data = {
        "check_name":"设备用热 {}".format(check_id),
        "hot":"178",
        "history_year_list":[
            {"history_time": "1", "history_value":"326" },
            {"history_time": "2", "history_value":"226" },
            {"history_time": "3", "history_value":"76" },
            {"history_time": "4", "history_value":"126" },
            {"history_time": "5", "history_value":"326" },
            {"history_time": "6", "history_value":"426" },
            {"history_time": "7", "history_value":"626" },
            {"history_time": "8", "history_value":"596" },
            {"history_time": "9", "history_value":"86" },
            {"history_time":"10", "history_value":"126" },
            {"history_time":"11", "history_value":"156" },
            {"history_time":"12", "history_value":"526" },
        ],
        "history_month_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "526"},
            {"history_time": "19", "history_value": "526"},
            {"history_time": "20", "history_value": "326"},
            {"history_time": "21", "history_value": "426"},
            {"history_time": "22", "history_value": "526"},
            {"history_time": "23", "history_value": "526"},
            {"history_time": "24", "history_value": "526"},
            {"history_time": "25", "history_value": "526"},
            {"history_time": "26", "history_value": "526"},
            {"history_time": "27", "history_value": "526"},
            {"history_time": "28", "history_value": "526"},
            {"history_time": "29", "history_value": "526"},
            {"history_time": "30", "history_value": "526"},
        ],
        "history_day_list":[
            {"history_time": "1", "history_value": "326"},
            {"history_time": "2", "history_value": "226"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "126"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "126"},
            {"history_time": "11", "history_value": "156"},
            {"history_time": "12", "history_value": "526"},
            {"history_time": "13", "history_value": "526"},
            {"history_time": "14", "history_value": "526"},
            {"history_time": "15", "history_value": "526"},
            {"history_time": "16", "history_value": "526"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "426"},
            {"history_time": "19", "history_value": "436"},
            {"history_time": "20", "history_value": "526"},
            {"history_time": "21", "history_value": "226"},
            {"history_time": "22", "history_value": "126"},
            {"history_time": "23", "history_value": "226"},
            {"history_time": "0", "history_value": "26"},
        ]
    }
    return test_data



def get_device_data(check_id):
    '''
    设备通用查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    # # 测试数据
    if check_id[0] == 'a':
        test_data = {
            "device_name":"空调-风机盘管，{}".format(check_id),
            "device_pic":"ac_wind.jpg",
            "device_sn":"ABC123",
            "device_factory":"西门子",
            "device_version":"cv100",
            "device_location":"1号楼1层",
            "device_info":[
                {
                    "device_info_name":"供热量",
                    "device_info_value":"126",
                },
                {
                    "device_info_name":"供冷量",
                    "device_info_value":"216",
                },
                {
                    "hot_history_time":"风量",
                    "hot_history_value":"611",
                }
            ],
            "device_status":[
                {
                    "device_status_name":"室内温度",
                    "device_status_value":"23",
                },
                {
                    "device_status_name":"冷水阀开关状态",
                    "device_status_value":"1",
                },
                {
                    "device_status_name":"报警信息",
                    "device_status_value":"无故障",
                }
            ]
        }
    else:
        test_data = {
            "device_name": "智能插座，{}".format(check_id),
            "device_pic": "switch01.jpg",
            "device_sn": "ABC123{}".format(check_id),
            "device_factory": "小米",
            "device_version": "小米智能插座",
            "device_location": "1号楼2层控制室",
            "device_info": [
                {
                    "device_info_name": "供热量",
                    "device_info_value": "126",
                },
                {
                    "device_info_name": "供冷量",
                    "device_info_value": "216",
                },
                {
                    "hot_history_time": "风量",
                    "hot_history_value": "611",
                }
            ],
            "device_status": [
                {
                    "device_status_name": "开关状态",
                    "device_status_value": "on",
                },
                {
                    "device_status_name": "实时电流",
                    "device_status_value": "20mA",
                }
            ]
        }
    return test_data