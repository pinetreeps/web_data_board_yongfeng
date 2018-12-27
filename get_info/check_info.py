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

def get_env_indoor():
    '''
    查询室内环境 实时
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
        "voc": "2.7",
        "pm2.5":"120"
    }
    return test_data_env_outdoor


def env_indoor_history(data_type):
    '''
    查询室内环境 历史数据
    :return: dict
    '''
    # # 测试数据
    test_data_env_indoor_history = {}
    if 'year' == data_type:
        test_data_env_indoor_history = {
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