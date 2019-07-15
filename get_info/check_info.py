# _*_ coding:utf-8 _*_
# Filename: check_info.py
# Author: pang song
# python 3.6
# Date: 2018/12/26
'''
三、信息接口
'''
import random, datetime
import logging
from utils import mysql_utils
# from utils import sqlserver_util

logger = logging.getLogger("main")

WEEK_NAMES = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
# voc对照 0，1，2，3
# VOC_LEVEL = {'0':'空气良好', '1':'轻度污染', '2':'中度污染', '3':'重度污染'}
VOC_LEVEL = {'0':'优', '1':'良好', '2':'一般', '3':'差'}

PROPERTY_DICT = {
    'gas_boiler':'锅炉用气',
    'gas_kitchen': '厨房用气',
    'gas_other': '其他用气',
    'water_live': '生活用水',
    'water_ac': '空调用水',
    'water_kitchen': '厨房用水',
    'water_other': '其他用水',
}

# --------------mysql 取数据 ------------------

def get_name_by_id(check_id):
    '''
    get name by check_id
    :return: name
    '''
    check_name = ''
    data_conn = mysql_utils.Database()
    sql1 = "select position_name from yf_bim_position_info where position_id = '{pid}'".format(pid=check_id)
    row1 = data_conn.query_one(sql1)
    logger.debug(row1)
    if row1 != None:
        check_name = row1[0]
    return check_name

def get_device_name_by_id(check_id):
    '''
    get name by check_id
    :return: name
    '''
    logger.debug(check_id)
    device_info = {
        "device_name":"",
        "device_code":"",
        "device_type":"",
        "device_position_id":""
    }
    data_conn = mysql_utils.Database()
    sql1 = "select device_name, device_code, device_type, device_position_id from yf_bim_device_info where device_id = '{did}'".format(did=check_id)
    row1 = data_conn.query_one(sql1)
    logger.debug(row1)
    if row1 != None:
        device_info["device_name"] = row1[0]
        device_info["device_code"] = row1[1]
        device_info["device_type"] = row1[2]
        device_info["device_position_id"] = row1[3]
    return device_info


def get_property_data_by_date_type(start_time, end_time, value_type):
    # 获取物业数据
    '''
    get name by check_id
    :return: name
    '''
    value_list = []
    # value_list = [
    #     {
    #         "date": "2018-01-10",
    #         "value": "345",
    #         "user": "admin",
    #         "update_time": "2018-01-10 16:52:30",
    #     },
    #     {
    #         "date": "2018-01-11",
    #         "value": "245",
    #         "user": "admin",
    #         "update_time": "2018-01-11 15:21:30",
    #     },
    # ]
    table_name = 'yf_bim_energy_water'
    if value_type.split('_')[0] == 'gas':
        table_name = 'yf_bim_energy_gas'

    data_conn = mysql_utils.Database()
    sql1 = """
          SELECT DATE_FORMAT(g.value_date,'%Y-%m-%d') as date, g.value, g.value_type, u.uname, DATE_FORMAT(g.utime,'%Y-%m-%d %T') as utime 
          FROM {tn} g LEFT JOIN yf_bim_user_info u ON g.uid = u.uid
          WHERE value_type = '{vt}' AND value_date BETWEEN '{st}' AND '{et}'
          """.format(tn=table_name, vt=value_type, st=start_time, et=end_time)
    print(sql1)
    rows = data_conn.query_all_no_params(sql1)
    # rows = data_conn.query_one(sql1)

    # logger.debug(rows)
    if rows != None:
        # print(rows)
        for row in rows:
            value_list.append({
                "date": row[0],
                "value": row[1],
                "user": row[3],
                "update_time": row[4]})
    return value_list

def update_property_data_by_date_type(update_type, date_time, value_type, update_value, uid):
    # 更新物业数据
    '''
    get name by check_id
    :return: name
    '''
    table_name = 'yf_bim_energy_water'
    if value_type.split('_')[0] == 'gas':
        table_name = 'yf_bim_energy_gas'

    data_conn = mysql_utils.Database()

    if update_type == 'add':

        sql1 = """
            INSERT INTO  {tn} (position_id, position_name, value_date, value, value_type, uid, ctime, utime) 
            VALUES ('empty', 'empty', '{vd}', '{v}', '{vt}', '{uid}', now(), now());
            """.format(tn=table_name, vd=date_time, v=update_value, vt=value_type, uid=uid)

    elif update_type == 'delete':
        sql1 = """
            DELETE FROM {tn} WHERE value_date = '{vd}' and value_type = '{vt}'
            """.format(tn=table_name, vd=date_time, vt=value_type)

    elif update_type == 'update':
        sql1 = """
            UPDATE {tn} SET value = '{v}', uid='{uid}', utime=now()
            WHERE value_date = '{vd}' and value_type = '{vt}'
            """.format(tn=table_name, vd=date_time, v=update_value, vt=value_type, uid=uid)
    else:
        logger.error('unknown update_type')
        return 0
    data_conn.insert_del_update(sql1)
    logger.info('save data success')
    # print('')
    print(sql1)
    return 1


# --------------物联网取数据 ------------------
def get_data_sql_server(check_id):
    sql_server_conn = sqlserver_util.Database_sql_server()
    # 室外温度
    # check_id = 'QXZ_Temperature'
    check_value = ''
    sql1 = "SELECT TOP 1 * FROM LASTDAVEDATA WHERE TAGNAME = '{name}' ORDER BY UPDATETIME DESC".format(name=check_id)
    row1 = sql_server_conn.query_one(sql1)
    logger.debug(row1)
    if row1 != None:
        check_value = row1[2].strip()
    return check_value


# --------------1、项目概况模块 ------------------

def get_area_overview():
    '''
    查询园区概况
    :return: dict
    '''
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
    # # 测试数据
    test_data_area_overview = {
        "land_area": "29450",
        "buildings_amount": "1",
        "buildings_area": "7643",
        "floor_area_ratio": "2.0",
        "greening_rate": "30",
        "company_amount": "1",
        "area_people_amount": "300",
        # 建筑总用电、建筑单位平米用电、室外pm2.5、室内平均pm2.5
        "electricity_overview": "451.23",
        "electricity_per_m2": "1.23",
        "outdoor_pm25": "120",
        "indoor_pm25": "80",
        "companys_ratio":[
            {
                "ratio_name":"高科技企业",
                "ratio_value":"5"
            },
            {
                "ratio_name":"其他企业",
                "ratio_value":"1"
            }]
    }
    return test_data_area_overview


def get_building_overview():
    '''
    查询建筑概况
    :return: dict
    '''
    '''
    建筑概况
    建筑名称	永丰B5综合服务楼
    使用功能	综合服务楼
    建筑面积	7643m²
    建筑高度	25m
    建筑时间	2018
    建筑层数	5
    '''
    # # 测试数据
    test_data_building_overview = {
        "building_name":"西北旺镇政务服务中心",
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
        "temperature":"10",
        "humidity":"52",
        # "wind_direction":"西",
        "wind_direction":"135.5",
        "wind_speed":"1.0",
        "precipitation":"0",
        "air_pressure":"102.3",
        "pm2.5":"29"
    }
    return test_data_env_outdoor

def env_outdoor_history(data_type):
    '''
        查询室外环境 历史数据
        :return: dict
        '''
    # # 测试数据
    test_data_env_outdoor_history = { "data_list":[]}
    if 'year' == data_type:
        test_data_env_outdoor_history["data_list"] = [
            {"data_time": "1", "temperature_high":"", "temperature_low":"", "humidity": "", "wind_speed": "", "precipitation": "", "air_pressure": "",   "pm2.5": ""},
            {"data_time": "2", "temperature_high":"", "temperature_low":"", "humidity": "", "wind_speed": "", "precipitation": "", "air_pressure": "",   "pm2.5": ""},
            {"data_time": "3", "temperature_high":"", "temperature_low":"", "humidity": "", "wind_speed": "", "precipitation": "", "air_pressure": "",   "pm2.5": ""},
            {"data_time": "4", "temperature_high":"", "temperature_low":"", "humidity": "", "wind_speed": "", "precipitation": "", "air_pressure": "",   "pm2.5": ""},
            {"data_time": "5", "temperature_high":"37.9", "temperature_low":"18.4", "humidity": "53.6", "wind_speed": "1.5", "precipitation": "0.3", "air_pressure": "101.9",   "pm2.5": "40.7"},
            # {"data_time": "2", "temperature_high":"8", "temperature_low":"-8", "humidity": "40", "wind_speed": "2.2", "precipitation": "20", "air_pressure": "102.3",   "pm2.5": "120"},
            # {"data_time": "3", "temperature_high":"13", "temperature_low":"0", "humidity": "40", "wind_speed": "0.5", "precipitation": "60", "air_pressure": "102.3",   "pm2.5": "120"},
            # {"data_time": "4", "temperature_high":"20", "temperature_low":"1", "humidity": "40", "wind_speed": "0.8", "precipitation": "50", "air_pressure": "102.3",   "pm2.5": "120"},
            # {"data_time": "5", "temperature_high":"26", "temperature_low":"16", "humidity": "40", "wind_speed": "0.7", "precipitation": "50", "air_pressure": "102.3",   "pm2.5": "120"},
            # {"data_time": "6", "temperature_high":"28", "temperature_low":"18", "humidity": "40", "wind_speed": "0.9", "precipitation": "100", "air_pressure": "102.3",   "pm2.5": "120"},
            # {"data_time": "7", "temperature_high":"30", "temperature_low":"22", "humidity": "40", "wind_speed": "0.5", "precipitation": "200", "air_pressure": "102.3",   "pm2.5": "120"},
            # {"data_time": "8", "temperature_high":"35", "temperature_low":"22", "humidity": "40", "wind_speed": "0.6", "precipitation": "180", "air_pressure": "102.3",   "pm2.5": "120"},
            # {"data_time": "9", "temperature_high":"34", "temperature_low":"18", "humidity": "40", "wind_speed": "0.9", "precipitation": "80", "air_pressure": "102.3",   "pm2.5": "120"},
            # {"data_time": "10", "temperature_high":"26", "temperature_low":"16", "humidity": "40", "wind_speed": "1.3", "precipitation": "20", "air_pressure": "102.3",   "pm2.5": "120"},
            # {"data_time": "11", "temperature_high":"16", "temperature_low":"8", "humidity": "40", "wind_speed": "2.1", "precipitation": "10", "air_pressure": "102.3",   "pm2.5": "500"},
            # {"data_time": "12", "temperature_high":"7", "temperature_low":"-6", "humidity": "40", "wind_speed": "1.2", "precipitation": "0", "air_pressure": "102.3",   "pm2.5": "420"},
            ]
    elif 'month' == data_type:
        for i in range(1, 31):
            row_data = {
                "data_time": str(i),
                "temperature_high": str(random.randint(1, 10)),
                "temperature_low": str(random.randint(-10, 3)),
                "humidity": str(random.randint(10, 35)),
                "wind_speed": str(random.randint(0, 3)) + '.' + str(random.randint(0, 10)),
                "precipitation": str(random.randint(0, 200)),
                "air_pressure": str(random.randint(100, 105)),
                "pm2.5": str(random.randint(80, 500))
            }
            test_data_env_outdoor_history["data_list"].append(row_data)

    elif 'day' == data_type:
        # 获取当前小时数
        time_hour = datetime.datetime.now().strftime('%H')

        # 模拟数据
        temperature_high_list = [-3,-3,-2,-1,-1,0,0,1,4,6,7,10,11,11,12,11,10,9,8,5,4,3,2,1]
        for i in range(0, 24):
            row_data = {
                "data_time": str(i),
                "temperature_high": str(temperature_high_list[i]),
                "temperature_low": str(temperature_high_list[i] - random.randint(0, 4)),
                "humidity": str(random.randint(10, 35)),
                "wind_speed": str(random.randint(0, 3)) + '.' + str(random.randint(0, 10)),
                "precipitation": str(random.randint(0, 200)),
                "air_pressure": str(random.randint(100, 105)),
                "pm2.5": str(random.randint(80, 500))
            }

            row_data_zeros = {
                "data_time": str(i),
                "temperature_high": '',
                "temperature_low": '',
                "humidity": '',
                "wind_speed": '',
                "precipitation": '',
                "air_pressure": '',
                "pm2.5": ''
            }
            if i <= int(time_hour):
                test_data_env_outdoor_history["data_list"].append(row_data)
            else:
                test_data_env_outdoor_history["data_list"].append(row_data_zeros)
    return test_data_env_outdoor_history

def get_env_indoor(position_id):
    '''
    查询室内环境 实时
    :return: dict
    '''
    '''
    温度	K2_121_4C2_205_SWD
    湿度	K2_121_4C2_205_SSD
    PM2.5 K2_121_4C2_205_PMZ
    VOC	K2_121_4C2_205_VOC
    '''
    position_name = get_name_by_id(position_id)

    # # 测试数据
    test_data = {
        "position_name":"{}".format(position_name),
        "temperature": str(random.randint(22, 24)),
        "humidity": str(random.randint(30, 40)),
        "voc": VOC_LEVEL.get(str(random.randint(0, 3))),
        "pm2.5": str(random.randint(5, 15))
    }
    '''
    real_data = {
        "position_name":"{}".format(position_name),
        "temperature": get_data_sql_server('K2_121_4C2_205_SWD'),
        "humidity": get_data_sql_server('K2_121_4C2_205_SSD'),
        "voc": VOC_LEVEL.get(get_data_sql_server('K2_121_4C2_205_VOC')),
        "pm2.5": get_data_sql_server('K2_121_4C2_205_PMZ')
    }
    '''
    return test_data
    # return real_data


def env_indoor_history(position_id, data_type):
    '''
    查询室内环境 历史数据
    :return: dict
    '''
    # # 测试数据
    position_name = get_name_by_id(position_id)
    test_data_env_indoor_history = {
        "position_name": "{}".format(position_name),
        "data_list": []
    }
    if 'year' == data_type:
        test_data_env_indoor_history["data_list"] = [
            {"data_time": "1", "temperature_high":"5", "temperature_low":"-10", "humidity": "10", "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}],"pm2.5": "15"},
            {"data_time": "2", "temperature_high":"8", "temperature_low":"-8", "humidity": "14",  "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "15"},
            {"data_time": "3", "temperature_high":"13", "temperature_low":"0", "humidity": "15",  "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "10"},
            {"data_time": "4", "temperature_high":"20", "temperature_low":"1", "humidity": "21",  "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "5"},
            {"data_time": "5", "temperature_high":"26", "temperature_low":"16", "humidity": "30", "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "12"},
            {"data_time": "6", "temperature_high":"28", "temperature_low":"18", "humidity": "34", "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "12"},
            {"data_time": "7", "temperature_high":"30", "temperature_low":"22", "humidity": "45", "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "13"},
            {"data_time": "8", "temperature_high":"35", "temperature_low":"22", "humidity": "35", "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "5"},
            {"data_time": "9", "temperature_high":"34", "temperature_low":"18", "humidity": "41", "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "8"},
            {"data_time": "10", "temperature_high":"26", "temperature_low":"16", "humidity": "22","voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "11"},
            {"data_time": "11", "temperature_high":"16", "temperature_low":"8", "humidity": "19", "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "14"},
            {"data_time": "12", "temperature_high":"7", "temperature_low":"-6", "humidity": "20", "voc":[{"name":"良好", "value":"11"},
                                                                                                         {"name":"轻污染", "value":"16"},
                                                                                                         {"name":"中污染", "value":"2"},
                                                                                                         {"name":"重污染", "value":"1"}], "pm2.5": "6"},
            ]
    elif 'month' == data_type:
        for i in range(1, 31):
            row_data = {
                "data_time": str(i),
                "temperature_high": str(random.randint(16, 24)),
                "temperature_low": str(random.randint(10, 16)),
                "humidity": str(random.randint(25, 35)),
                "voc":[{"name":"良好", "value":"1"},{"name":"轻污染", "value":"0"},{"name":"中污染", "value":"0"},{"name":"重污染", "value":"0"}],
                "pm2.5": str(random.randint(5, 15))
            }
            test_data_env_indoor_history["data_list"].append(row_data)

    elif 'day' == data_type:
        # 获取当前小时数
        time_hour = datetime.datetime.now().strftime('%H')

        for i in range(0, 24):
            row_data = {
                "data_time": str(i),
                "temperature_high": str(random.randint(16, 24)),
                "temperature_low": str(random.randint(10, 16)),
                "humidity": str(random.randint(25, 35)),
                "voc": [{"name":"良好", "value":"0"},{"name":"轻污染", "value":"1"},{"name":"中污染", "value":"0"},{"name":"重污染", "value":"0"}],
                "pm2.5": str(random.randint(5, 15))
            }

            row_data_zeros = {
                "data_time": str(i),
                "temperature_high": '',
                "temperature_low": '',
                "humidity": '',
                "voc": '',
                "pm2.5": ''
            }
            if i <= int(time_hour):
                test_data_env_indoor_history["data_list"].append(row_data)
            else:
                test_data_env_indoor_history["data_list"].append(row_data_zeros)
        # logger.debug(test_data_env_indoor_history)

    return test_data_env_indoor_history

def get_energy_overview(check_id):
    '''
    查询用能概况
    :return: dict
    '''
    check_name = get_name_by_id(check_id)
    # # 测试数据
    energy_overview_data = {
        "check_name":"{}".format(check_name),
        "electricity":[],
        "gas":[],
        "water":[]}

    for i in range(7):
        # 用电
        row_data1 = {
                "time": WEEK_NAMES[i],
                "value_list": [{"name":"照明","value": str(random.randint(1000, 1500))},
                               {"name":"空调", "value":"0",},
                               {"name":"插座","value": str(random.randint(200, 400))},
                               {"name":"厨房","value":"0",},
                               {"name":"其他","value":"0",},],
            }
        energy_overview_data["electricity"].append(row_data1)
        # 用气
        row_data2 = {
                        "time": WEEK_NAMES[i],
                        "value_list":[{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",}]
                    }
        energy_overview_data["gas"].append(row_data2)
        # 用水
        row_data3 = {
                        "time": WEEK_NAMES[i],
                        "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                                       {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ]
                    }
        energy_overview_data["water"].append(row_data3)

    test_data = {
        "check_name":"{}".format(check_name),
        "electricity":[
            {
                "time":"周一",
                "value_list": [{"name":"建筑","value":"231",},
                               {"name":"空调", "value":"3523",},
                               {"name":"电器","value":"2223",},
                               {"name":"其他","value":"1123",},],
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
                "value_list":[{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周二",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周三",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周四",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周五",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周六",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"3",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周日",
                "value_list": [{"name":"采暖","value":"0",},{"name":"厨房", "value":"0",},{"name":"其他","value":"0",},],
            },

        ],
        "water":[
            {
                "time":"周一",
                "value_list":[{"name":"生活","value":"0",},{"name":"空调", "value":"0",},{"name":"厨房","value":"0",},{"name":"其他","value":"0",},],
            },
            {
                "time": "周二",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周三",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周四",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周五",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周六",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },
            {
                "time": "周日",
                "value_list": [{"name": "生活", "value": "0", }, {"name": "空调", "value": "0", },
                               {"name": "厨房", "value": "0", }, {"name": "其他", "value": "0", }, ],
            },

        ],
    }
    # return test_data
    return energy_overview_data


def get_energy_electricity_overview(check_id):
    '''
    用电情况通用查询接口1，使用唯一id进行查询，园区用电、建筑用电返回各建筑、各层用电占比
    :return: dict
    '''
    check_name = get_name_by_id(check_id)
    # # 测试数据
    energy_electricity_overview_data = {
        "check_name":"{}".format(check_name),
        # "electricity":str(random.randint(1200, 1900)),
        "electricity": "12241.2",
        "history_year_list":[
            {"history_time": "1", "history_value": ""},
            {"history_time": "2", "history_value": ""},
            {"history_time": "3", "history_value": ""},
            {"history_time": "4", "history_value": ""},
            {"history_time": "5", "history_value": "1846.6"},
        ],
        "history_month_list": [

            {"history_time": "1", "history_value": ""},
            {"history_time": "2", "history_value": ""},
            {"history_time": "3", "history_value": ""},
            {"history_time": "4", "history_value": ""},
            {"history_time": "5", "history_value": ""},
            {"history_time": "6", "history_value": ""},
            {"history_time": "7", "history_value": ""},
            {"history_time": "8", "history_value": ""},
            {"history_time": "9", "history_value": ""},
            {"history_time": "10","history_value": "6565.03"},
            {"history_time": "11","history_value": "1487.81"},
            {"history_time": "12","history_value": ""},
            {"history_time": "13","history_value": "1536.87"},
            {"history_time": "14","history_value": "1499.53"},
            {"history_time": "15","history_value": "1511.08"},
            {"history_time": "16","history_value": "1560.42"},
            {"history_time": "17","history_value": "1582.03"},
            {"history_time": "18","history_value": "1583.86"},
            {"history_time": "19","history_value": "1564.58"}
        ],
        "history_day_list":[
            {"history_time": "0", "history_value": "16"},
            {"history_time": "1", "history_value": "12"},
            {"history_time": "2", "history_value": "96"},
            {"history_time": "3", "history_value": "76"},
            {"history_time": "4", "history_value": "66"},
            {"history_time": "5", "history_value": "87"},
            {"history_time": "6", "history_value": "81"},
            {"history_time": "7", "history_value": "92"},
            {"history_time": "8", "history_value": "126"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "26"},
            {"history_time": "11", "history_value": "56"},
            {"history_time": "12", "history_value": "26"},
            {"history_time": "13", "history_value": "26"},
            {"history_time": "14", "history_value": "61"},
            {"history_time": "15", "history_value": "26"},
            {"history_time": "16", "history_value": "26"},
            {"history_time": "17", "history_value": "21"},
            {"history_time": "18", "history_value": "26"},
            {"history_time": "19", "history_value": "36"},
            {"history_time": "20", "history_value": "26"},
            {"history_time": "21", "history_value": "26"},
            {"history_time": "22", "history_value": "26"},
            {"history_time": "23", "history_value": "26"},
        ],
        "electricity_ratio1": [
            {"ratio_id": "b01f01", "ratio_name": "1层", "ratio_value": "66465.4"},
            {"ratio_id": "b01f02", "ratio_name": "2层", "ratio_value": "19305.6"},
            {"ratio_id": "b01f03", "ratio_name": "3层", "ratio_value": "34685.8"},
            {"ratio_id": "b01f04", "ratio_name": "4层", "ratio_value": "18645.5"},
            {"ratio_id": "b01f05", "ratio_name": "5层", "ratio_value": "19255.4"},
            {"ratio_id": "b01f06", "ratio_name": "6层", "ratio_value": "304.08"},
        ],
        "electricity_ratio2": [
            {"ratio_id": "b01", "ratio_name": "照明", "ratio_value": "77027.8"},
            {"ratio_id": "b02", "ratio_name": "空调", "ratio_value": "43455.8"},
            {"ratio_id": "b03", "ratio_name": "电器", "ratio_value": "387062.3"},
            {"ratio_id": "b03", "ratio_name": "其他", "ratio_value": "0"},
        ]
    }
    # for i in range(1, 13):
    #     row_data = {"history_time": str(i), "history_value":str(random.randint(1200, 1900)) }
    #     energy_electricity_overview_data["history_year_list"].append(row_data)
    #
    # for i in range(1, 31):
    #     row_data = {"history_time": str(i), "history_value":str(random.randint(1200, 1900)) }
    #     energy_electricity_overview_data["history_month_list"].append(row_data)


    test_data = {
        "check_name":"{}".format(check_name),
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
            {"history_time": "3", "history_value": "376"},
            {"history_time": "4", "history_value": "526"},
            {"history_time": "5", "history_value": "326"},
            {"history_time": "6", "history_value": "426"},
            {"history_time": "7", "history_value": "626"},
            {"history_time": "8", "history_value": "596"},
            {"history_time": "9", "history_value": "86"},
            {"history_time": "10", "history_value": "226"},
            {"history_time": "11", "history_value": "456"},
            {"history_time": "12", "history_value": "326"},
            {"history_time": "13", "history_value": "326"},
            {"history_time": "14", "history_value": "426"},
            {"history_time": "15", "history_value": "563"},
            {"history_time": "16", "history_value": "626"},
            {"history_time": "17", "history_value": "526"},
            {"history_time": "18", "history_value": "526"},
            {"history_time": "19", "history_value": "526"},
            {"history_time": "20", "history_value": "326"},
            {"history_time": "21", "history_value": "426"},
            {"history_time": "22", "history_value": "156"},
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
            {"ratio_id":"floor01", "ratio_name":"1层", "ratio_value":"115"},
            {"ratio_id":"floor02", "ratio_name":"2层", "ratio_value":"85"},
            {"ratio_id":"floor03", "ratio_name":"3层", "ratio_value":"95"},
            {"ratio_id":"floor04", "ratio_name":"4层", "ratio_value":"75"},
            {"ratio_id":"floor05", "ratio_name":"5层", "ratio_value":"56"},
        ],
        "electricity_ratio2": [
            {"ratio_id": "b01","ratio_name": "照明","ratio_value": "2345"},
            {"ratio_id": "b02","ratio_name": "空调","ratio_value": "0"},
            {"ratio_id": "b03","ratio_name": "电器","ratio_value": "545"},
            {"ratio_id": "b03","ratio_name": "其他","ratio_value": "0"},
        ]
    }
    # return test_data
    return energy_electricity_overview_data


def get_energy_electricity(check_id):
    '''
    用电情况通用查询接口2，使用唯一id 查询设备用电（空调、电器）
    :return: dict
    '''
    check_name = get_name_by_id(check_id)
    # # 测试数据
    energy_electricity_data = {
        "check_name": "{}".format(check_name),
        "electricity": str(random.randint(100, 200)),
        "history_year_list": [],
        "history_month_list": [],
        "history_day_list":[
            {"history_time": "1", "history_value": "1"},
            {"history_time": "2", "history_value": "2"},
            {"history_time": "3", "history_value": "3"},
            {"history_time": "4", "history_value": "2"},
            {"history_time": "5", "history_value": "1"},
            {"history_time": "6", "history_value": "3"},
            {"history_time": "7", "history_value": "4"},
            {"history_time": "8", "history_value": "8"},
            {"history_time": "9", "history_value": "9"},
            {"history_time": "10", "history_value": "11"},
            {"history_time": "11", "history_value": "12"},
            {"history_time": "12", "history_value": "13"},
            {"history_time": "13", "history_value": "12"},
            {"history_time": "14", "history_value": "13"},
            {"history_time": "15", "history_value": "8"},
            {"history_time": "16", "history_value": "6"},
            {"history_time": "17", "history_value": "11"},
            {"history_time": "18", "history_value": "12"},
            {"history_time": "19", "history_value": "5"},
            {"history_time": "20", "history_value": "6"},
            {"history_time": "21", "history_value": "8"},
            {"history_time": "22", "history_value": "2"},
            {"history_time": "23", "history_value": "2"},
            {"history_time": "0", "history_value": "1"},
        ]
    }
    for i in range(1, 13):
        row_data = {"history_time": str(i), "history_value":str(random.randint(200, 300)) }
        energy_electricity_data["history_year_list"].append(row_data)

    for i in range(1, 31):
        row_data = {"history_time": str(i), "history_value":str(random.randint(100, 200)) }
        energy_electricity_data["history_month_list"].append(row_data)


    test_data = {
        "check_name":"{}".format(check_name),
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
    # return test_data
    return energy_electricity_data

def get_energy_gas(check_id):
    '''
    查询用气情况
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    # # 测试数据
    energy_gas_data = {
        "check_name":"{}".format(check_name),
        "ac_gas": {
            "class_name": "采暖用气",
            "history_year_list":[],
            "history_month_list":[],
            "history_day_list":[]
        },
        "kitchen_gas": {
            "class_name": "厨房用气",
            "history_year_list": [],
            "history_month_list": [],
            "history_day_list": []
        }
    }
    for i in range(1, 13):
        row_data = {"history_time": str(i), "history_value":"0" }
        energy_gas_data["ac_gas"]["history_year_list"].append(row_data)
        energy_gas_data["kitchen_gas"]["history_year_list"].append(row_data)
    for i in range(1, 31):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_gas_data["ac_gas"]["history_month_list"].append(row_data)
        energy_gas_data["kitchen_gas"]["history_month_list"].append(row_data)
    for i in range(0, 24):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_gas_data["ac_gas"]["history_day_list"].append(row_data)
        energy_gas_data["kitchen_gas"]["history_day_list"].append(row_data)

    test_data = {
        "check_name":"{}".format(check_name),
        "ac_gas": {
            "class_name": "采暖用气",
            "history_year_list":[
                {"history_time": "1", "history_value":"0" },
                {"history_time": "2", "history_value":"0" },
                {"history_time": "3", "history_value":"0" },
                {"history_time": "4", "history_value":"0" },
                {"history_time": "5", "history_value":"0" },
                {"history_time": "6", "history_value":"93679.9" },
                # {"history_time": "7", "history_value":"626" },
                # {"history_time": "8", "history_value":"596" },
                # {"history_time": "9", "history_value":"86" },
                # {"history_time":"10", "history_value":"126" },
                # {"history_time":"11", "history_value":"156" },
                # {"history_time":"12", "history_value":"526" },
            ],
            "history_month_list":[
                {"history_time": "1", "history_value": "0"},
                {"history_time": "2", "history_value": "0"},
                {"history_time": "3", "history_value": "0"},
                {"history_time": "4", "history_value": "0"},
                {"history_time": "5", "history_value": "0"},
                {"history_time": "6", "history_value": "0"},
                {"history_time": "7", "history_value": "0"},
                {"history_time": "8", "history_value": "0"},
                {"history_time": "9", "history_value": "0"},
                {"history_time": "10", "history_value": "0"},
                {"history_time": "11", "history_value": "0"},
                {"history_time": "12", "history_value": "0"},
                {"history_time": "13", "history_value": "93679.9"},
                # {"history_time": "14", "history_value": "526"},
                # {"history_time": "15", "history_value": "526"},
                # {"history_time": "16", "history_value": "526"},
                # {"history_time": "17", "history_value": "526"},
                # {"history_time": "18", "history_value": "526"},
                # {"history_time": "19", "history_value": "526"},
                # {"history_time": "20", "history_value": "326"},
                # {"history_time": "21", "history_value": "426"},
                # {"history_time": "22", "history_value": "526"},
                # {"history_time": "23", "history_value": "526"},
                # {"history_time": "24", "history_value": "526"},
                # {"history_time": "25", "history_value": "526"},
                # {"history_time": "26", "history_value": "526"},
                # {"history_time": "27", "history_value": "526"},
                # {"history_time": "28", "history_value": "526"},
                # {"history_time": "29", "history_value": "526"},
                # {"history_time": "30", "history_value": "526"},
            ],
            # "history_day_list":[
            #     {"history_time": "1", "history_value": "326"},
            #     {"history_time": "2", "history_value": "226"},
            #     {"history_time": "3", "history_value": "76"},
            #     {"history_time": "4", "history_value": "126"},
            #     {"history_time": "5", "history_value": "326"},
            #     {"history_time": "6", "history_value": "426"},
            #     {"history_time": "7", "history_value": "626"},
            #     {"history_time": "8", "history_value": "596"},
            #     {"history_time": "9", "history_value": "86"},
            #     {"history_time": "10", "history_value": "126"},
            #     {"history_time": "11", "history_value": "156"},
            #     {"history_time": "12", "history_value": "526"},
            #     {"history_time": "13", "history_value": "526"},
            #     {"history_time": "14", "history_value": "526"},
            #     {"history_time": "15", "history_value": "526"},
            #     {"history_time": "16", "history_value": "526"},
            #     {"history_time": "17", "history_value": "526"},
            #     {"history_time": "18", "history_value": "426"},
            #     {"history_time": "19", "history_value": "436"},
            #     {"history_time": "20", "history_value": "526"},
            #     {"history_time": "21", "history_value": "226"},
            #     {"history_time": "22", "history_value": "126"},
            #     {"history_time": "23", "history_value": "226"},
            #     {"history_time": "0", "history_value": "26"},
            # ]
        },
        "kitchen_gas": {
            "class_name": "厨房用气",
            "history_year_list": [
                {"history_time": "1", "history_value": "0"},
                {"history_time": "2", "history_value": "0"},
                {"history_time": "3", "history_value": "0"},
                {"history_time": "4", "history_value": "0"},
                {"history_time": "5", "history_value": "0"},
                {"history_time": "6", "history_value": "59026.61"},
                # {"history_time": "7", "history_value": "626"},
                # {"history_time": "8", "history_value": "596"},
                # {"history_time": "9", "history_value": "86"},
                # {"history_time": "10", "history_value": "126"},
                # {"history_time": "11", "history_value": "156"},
                # {"history_time": "12", "history_value": "526"},
            ],
            "history_month_list": [
                {"history_time": "1", "history_value": "0"},
                {"history_time": "2", "history_value": "0"},
                {"history_time": "3", "history_value": "0"},
                {"history_time": "4", "history_value": "0"},
                {"history_time": "5", "history_value": "0"},
                {"history_time": "6", "history_value": "0"},
                {"history_time": "7", "history_value": "0"},
                {"history_time": "8", "history_value": "0"},
                {"history_time": "9", "history_value": "0"},
                {"history_time": "10", "history_value": "0"},
                {"history_time": "11", "history_value": "0"},
                {"history_time": "12", "history_value": "59026.61"},
                # {"history_time": "13", "history_value": "526"},
                # {"history_time": "14", "history_value": "526"},
                # {"history_time": "15", "history_value": "526"},
                # {"history_time": "16", "history_value": "526"},
                # {"history_time": "17", "history_value": "526"},
                # {"history_time": "18", "history_value": "526"},
                # {"history_time": "19", "history_value": "526"},
                # {"history_time": "20", "history_value": "326"},
                # {"history_time": "21", "history_value": "426"},
                # {"history_time": "22", "history_value": "526"},
                # {"history_time": "23", "history_value": "526"},
                # {"history_time": "24", "history_value": "526"},
                # {"history_time": "25", "history_value": "526"},
                # {"history_time": "26", "history_value": "526"},
                # {"history_time": "27", "history_value": "526"},
                # {"history_time": "28", "history_value": "526"},
                # {"history_time": "29", "history_value": "526"},
                # {"history_time": "30", "history_value": "526"},
            ],
            # "history_day_list": [
            #     {"history_time": "1", "history_value": "326"},
            #     {"history_time": "2", "history_value": "226"},
            #     {"history_time": "3", "history_value": "76"},
            #     {"history_time": "4", "history_value": "126"},
            #     {"history_time": "5", "history_value": "326"},
            #     {"history_time": "6", "history_value": "426"},
            #     {"history_time": "7", "history_value": "626"},
            #     {"history_time": "8", "history_value": "596"},
            #     {"history_time": "9", "history_value": "86"},
            #     {"history_time": "10", "history_value": "126"},
            #     {"history_time": "11", "history_value": "156"},
            #     {"history_time": "12", "history_value": "526"},
            #     {"history_time": "13", "history_value": "526"},
            #     {"history_time": "14", "history_value": "526"},
            #     {"history_time": "15", "history_value": "526"},
            #     {"history_time": "16", "history_value": "526"},
            #     {"history_time": "17", "history_value": "526"},
            #     {"history_time": "18", "history_value": "426"},
            #     {"history_time": "19", "history_value": "436"},
            #     {"history_time": "20", "history_value": "526"},
            #     {"history_time": "21", "history_value": "226"},
            #     {"history_time": "22", "history_value": "126"},
            #     {"history_time": "23", "history_value": "226"},
            #     {"history_time": "0", "history_value": "26"},
            # ]
        }
    }
    return test_data
    # return energy_gas_data

def get_energy_water_overview(check_id):
    '''
    查询用水情况
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    # # 测试数据
    energy_water_overview_data = {
        "check_name":"{} 用水总览".format(check_name),
        "live_water": {
            "class_name": "生活用水",
            "history_year_list":[],
            "history_month_list":[],
            "history_day_list":[],
            "ratio_list":[
                {"ratio_id":"floor01", "ratio_name":"1层", "ratio_value":"0"},
                {"ratio_id":"floor02", "ratio_name":"2层", "ratio_value":"0"},
                {"ratio_id":"floor03", "ratio_name":"3层", "ratio_value":"0"},
                {"ratio_id":"floor04", "ratio_name":"4层", "ratio_value":"0"},
                {"ratio_id":"floor05", "ratio_name":"5层", "ratio_value":"0"},
            ]
        },
        "kitchen_water": {
            "class_name": "厨房用水",
            "history_year_list": [],
            "history_month_list": [],
            "history_day_list": [],
            "ratio_list": [
                {"ratio_id": "floor01", "ratio_name": "1号厨房", "ratio_value": "0"},
                {"ratio_id": "floor02", "ratio_name": "2号厨房", "ratio_value": "0"},
            ]
        },
        "ac_water": {
            "class_name": "空调用水",
            "history_year_list": [],
            "history_month_list": [],
            "history_day_list": []
        }
    }
    for i in range(1, 13):
        row_data = {"history_time": str(i), "history_value":"0" }
        energy_water_overview_data["live_water"]["history_year_list"].append(row_data)
        energy_water_overview_data["kitchen_water"]["history_year_list"].append(row_data)
        energy_water_overview_data["ac_water"]["history_year_list"].append(row_data)
    for i in range(1, 31):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_water_overview_data["live_water"]["history_month_list"].append(row_data)
        energy_water_overview_data["kitchen_water"]["history_month_list"].append(row_data)
        energy_water_overview_data["ac_water"]["history_month_list"].append(row_data)
    for i in range(0, 24):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_water_overview_data["live_water"]["history_day_list"].append(row_data)
        energy_water_overview_data["kitchen_water"]["history_day_list"].append(row_data)
        energy_water_overview_data["ac_water"]["history_day_list"].append(row_data)


    test_data = {
        "check_name":"{} 用水总览".format(check_name),
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
    # return test_data
    return energy_water_overview_data

def get_energy_check_hot(check_id):
    '''
    用电情况通用查询接口2，使用唯一id 查询设备用电（空调、电器）
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    energy_check_hot_data = {
        "check_name": "设备用热 {}".format(check_name),
        "hot": "178",
        "history_year_list": [],
        "history_month_list": [],
        "history_day_list": []
    }
    for i in range(1, 13):
        row_data = {"history_time": str(i), "history_value":"0" }
        energy_check_hot_data["history_year_list"].append(row_data)
    for i in range(1, 31):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_check_hot_data["history_month_list"].append(row_data)
    for i in range(0, 24):
        row_data = {"history_time": str(i), "history_value": "0"}
        energy_check_hot_data["history_day_list"].append(row_data)


    # # 测试数据
    test_data = {
        "check_name":"设备用热 {}".format(check_name),
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
    # return test_data
    return energy_check_hot_data



def get_device_ac_data(check_id):
    '''
    设备通用查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    device_info = get_device_name_by_id(check_id)

    # # 测试数据
    if device_info.get("device_code") == 'FP03':
        # 空调 风机管盘 FP03
        test_data = {
            "device_name":"{}".format(device_info.get("device_name")),
            "device_pic": "FP03.jpg",
            "device_sn": device_info.get("device_code") ,
            "device_factory":"美的",
            "device_version": device_info.get("device_code") ,
            "device_location":"",
            "device_info":[
                {"device_info_name": "冷量kW", "device_info_value":"2.82" },
                {"device_info_name": "热量kW", "device_info_value": "4.4" },
                {"device_info_name": "风量m3/h", "device_info_value": "550" },
                {"device_info_name": "电机功率W", "device_info_value": "54" },
                {"device_info_name": "出口静压Pa", "device_info_value": "30" },
            ],
            "device_status":[
                {"device_status_name":"开关", "device_status_value":"关机"},
                {"device_status_name":"控制模式", "device_status_value":"自动模式"},
                {"device_status_name":"过滤器使用时长设置", "device_status_value":"0-4320小时"},
                {"device_status_name":"PM2.5浓度设置", "device_status_value":"0-200"},
                {"device_status_name":"季度设置", "device_status_value":"冬季"},
                {"device_status_name":"夏季温度最小值设置", "device_status_value":"15"},
                {"device_status_name":"冬季温度最大值设置", "device_status_value":"28"},
                {"device_status_name":"PM2.5阈值设置", "device_status_value":"0-24"},
                {"device_status_name":"温度阈值设置", "device_status_value":"0.5"},
                {"device_status_name":"控制器LCD亮度值设置", "device_status_value":"20%"},
                {"device_status_name":"过滤器运行时间", "device_status_value": str(random.randint(0, 10))},
                {"device_status_name":"运行风速", "device_status_value":"低速"},
                {"device_status_name":"电磁阀运行状态", "device_status_value":"关闭"},
                {"device_status_name":"水离子运行状态", "device_status_value":"关闭"},
                {"device_status_name":"过滤器运行状态", "device_status_value":"关闭"},
            ]
        }
    elif device_info.get("device_code") == 'FP04':
        # 空调 风机管盘 FP04
        test_data = {
            "device_name":"{}".format(device_info.get("device_name")),
            "device_pic": "FP04.jpg",
            "device_sn": device_info.get("device_code") ,
            "device_factory":"美的",
            "device_version": device_info.get("device_code") ,
            "device_location":"",
            "device_info":[
                {"device_info_name": "冷量kW", "device_info_value": "3.74"},
                {"device_info_name": "热量kW", "device_info_value": "6.26"},
                {"device_info_name": "风量m3/h", "device_info_value": "750"},
                {"device_info_name": "电机功率W", "device_info_value": "72"},
                {"device_info_name": "出口静压Pa", "device_info_value": "30"},
            ],
            "device_status":[
                {"device_status_name":"开关", "device_status_value":"关机"},
                {"device_status_name":"控制模式", "device_status_value":"自动模式"},
                {"device_status_name":"过滤器使用时长设置", "device_status_value":"0-4320小时"},
                {"device_status_name":"PM2.5浓度设置", "device_status_value":"0-200"},
                {"device_status_name":"季度设置", "device_status_value":"冬季"},
                {"device_status_name":"夏季温度最小值设置", "device_status_value":"15"},
                {"device_status_name":"冬季温度最大值设置", "device_status_value":"28"},
                {"device_status_name":"PM2.5阈值设置", "device_status_value":"0-24"},
                {"device_status_name":"温度阈值设置", "device_status_value":"0.5"},
                {"device_status_name":"控制器LCD亮度值设置", "device_status_value":"20%"},
                {"device_status_name":"过滤器运行时间", "device_status_value": str(random.randint(0, 10))},
                {"device_status_name":"运行风速", "device_status_value":"低速"},
                {"device_status_name":"电磁阀运行状态", "device_status_value":"关闭"},
                {"device_status_name":"水离子运行状态", "device_status_value":"关闭"},
                {"device_status_name":"过滤器运行状态", "device_status_value":"关闭"},
            ]
        }
    elif device_info.get("device_code") == 'FP05':
        # 空调 风机管盘 FP05
        test_data = {
            "device_name":"{}".format(device_info.get("device_name")),
            "device_pic": "FP05.jpg",
            "device_sn": device_info.get("device_code") ,
            "device_factory":"美的",
            "device_version": device_info.get("device_code") ,
            "device_location":"",
            "device_info":[
                {"device_info_name": "冷量kW", "device_info_value": "5.23"},
                {"device_info_name": "热量kW", "device_info_value": "8.4"},
                {"device_info_name": "风量m3/h", "device_info_value": "1060"},
                {"device_info_name": "电机功率W", "device_info_value": "112"},
                {"device_info_name": "出口静压Pa", "device_info_value": "30"},
            ],
            "device_status":[
                {"device_status_name":"开关", "device_status_value":"关机"},
                {"device_status_name":"控制模式", "device_status_value":"自动模式"},
                {"device_status_name":"过滤器使用时长设置", "device_status_value":"0-4320小时"},
                {"device_status_name":"PM2.5浓度设置", "device_status_value":"0-200"},
                {"device_status_name":"季度设置", "device_status_value":"冬季"},
                {"device_status_name":"夏季温度最小值设置", "device_status_value":"15"},
                {"device_status_name":"冬季温度最大值设置", "device_status_value":"28"},
                {"device_status_name":"PM2.5阈值设置", "device_status_value":"0-24"},
                {"device_status_name":"温度阈值设置", "device_status_value":"0.5"},
                {"device_status_name":"控制器LCD亮度值设置", "device_status_value":"20%"},
                {"device_status_name":"过滤器运行时间", "device_status_value": str(random.randint(0, 10))},
                {"device_status_name":"运行风速", "device_status_value":"低速"},
                {"device_status_name":"电磁阀运行状态", "device_status_value":"关闭"},
                {"device_status_name":"水离子运行状态", "device_status_value":"关闭"},
                {"device_status_name":"过滤器运行状态", "device_status_value":"关闭"},
            ]
        }
    elif device_info.get("device_code") == 'FP06' or device_info.get("device_code") == 'FP08':
        # 空调 风机管盘 FP06 or 08
        test_data = {
            "device_name":"{}".format(device_info.get("device_name")),
            "device_pic": "FP06.jpg",
            "device_sn": device_info.get("device_code") ,
            "device_factory":"美的",
            "device_version": device_info.get("device_code") ,
            "device_location":"",
            "device_info":[
                {"device_info_name": "冷量kW", "device_info_value": "7.3"},
                {"device_info_name": "热量kW", "device_info_value": "8.4"},
                {"device_info_name": "风量m3/h", "device_info_value": "1060"},
                {"device_info_name": "电机功率W", "device_info_value": "112"},
                {"device_info_name": "出口静压Pa", "device_info_value": "30"},
            ],
            "device_status":[
                {"device_status_name":"开关", "device_status_value":"关机"},
                {"device_status_name":"控制模式", "device_status_value":"自动模式"},
                {"device_status_name":"过滤器使用时长设置", "device_status_value":"0-4320小时"},
                {"device_status_name":"PM2.5浓度设置", "device_status_value":"0-200"},
                {"device_status_name":"季度设置", "device_status_value":"冬季"},
                {"device_status_name":"夏季温度最小值设置", "device_status_value":"15"},
                {"device_status_name":"冬季温度最大值设置", "device_status_value":"28"},
                {"device_status_name":"PM2.5阈值设置", "device_status_value":"0-24"},
                {"device_status_name":"温度阈值设置", "device_status_value":"0.5"},
                {"device_status_name":"控制器LCD亮度值设置", "device_status_value":"20%"},
                {"device_status_name":"过滤器运行时间", "device_status_value": str(random.randint(0, 10))},
                {"device_status_name":"运行风速", "device_status_value":"低速"},
                {"device_status_name":"电磁阀运行状态", "device_status_value":"关闭"},
                {"device_status_name":"水离子运行状态", "device_status_value":"关闭"},
                {"device_status_name":"过滤器运行状态", "device_status_value":"关闭"},
            ]
        }
    elif device_info.get("device_code") == 'OA01':
        test_data = {
            "device_name":"{}".format(device_info.get("device_name")),
            "device_pic": "OA01.jpg",
            "device_sn": "AHU" ,
            "device_factory":"美的",
            "device_version": "AHU" ,
            "device_location":"",
            "device_info":[
                {"device_info_name": "冷量kW", "device_info_value": "24"},
                {"device_info_name": "热量kW", "device_info_value": "28"},
                {"device_info_name": "风量m3/h", "device_info_value": "2000"},
                {"device_info_name": "380V功率kW", "device_info_value": "0.55"},
                {"device_info_name": "出口静压Pa", "device_info_value": "300"},
            ],
            "device_status":[
                {"device_status_name":"命令控制/时间表模式设定", "device_status_value":"时间表控制"},
                {"device_status_name":"命令控制模式", "device_status_value":"停止"},
                {"device_status_name":"防冻开关状态", "device_status_value":"正常"},
                {"device_status_name":"滤网压差状态", "device_status_value":"正常"},
                {"device_status_name":"风机手/自动状态", "device_status_value":"自动"},
                {"device_status_name":"风机运行状态", "device_status_value":"运行"},
                {"device_status_name":"风机故障状态", "device_status_value":"正常"},
                {"device_status_name":"风机启停控制显示", "device_status_value":"启动"},
                {"device_status_name":"新风阀开关控制显示", "device_status_value":"开启"},
                {"device_status_name":"净化器启停控制显示", "device_status_value":"开启"},
                {"device_status_name":"送风温度传感器", "device_status_value": "24"},
                {"device_status_name":"PM2.5传感器", "device_status_value":"10"},
                {"device_status_name":"送风温度设定", "device_status_value":"20"},
                {"device_status_name":"水阀控制开度显示", "device_status_value":"1"},
            ]
        }
    elif device_info.get("device_code") == 'OA02':
        test_data = {
            "device_name":"{}".format(device_info.get("device_name")),
            "device_pic": "OA01.jpg",
            "device_sn": "AHU" ,
            "device_factory":"美的",
            "device_version": "AHU",
            "device_location":"",
            "device_info":[
                {"device_info_name": "冷量kW", "device_info_value": "38"},
                {"device_info_name": "热量kW", "device_info_value": "43"},
                {"device_info_name": "风量m3/h", "device_info_value": "3000"},
                {"device_info_name": "380V功率kW", "device_info_value": "0.75"},
                {"device_info_name": "出口静压Pa", "device_info_value": "300"},
            ],
            "device_status":[
                {"device_status_name":"命令控制/时间表模式设定", "device_status_value":"时间表控制"},
                {"device_status_name":"命令控制模式", "device_status_value":"停止"},
                {"device_status_name":"防冻开关状态", "device_status_value":"正常"},
                {"device_status_name":"滤网压差状态", "device_status_value":"正常"},
                {"device_status_name":"风机手/自动状态", "device_status_value":"自动"},
                {"device_status_name":"风机运行状态", "device_status_value":"运行"},
                {"device_status_name":"风机故障状态", "device_status_value":"正常"},
                {"device_status_name":"风机启停控制显示", "device_status_value":"启动"},
                {"device_status_name":"新风阀开关控制显示", "device_status_value":"开启"},
                {"device_status_name":"净化器启停控制显示", "device_status_value":"开启"},
                {"device_status_name":"送风温度传感器", "device_status_value": "24"},
                {"device_status_name":"PM2.5传感器", "device_status_value":"10"},
                {"device_status_name":"送风温度设定", "device_status_value": "20"},
                {"device_status_name":"水阀控制开度显示", "device_status_value": "1"},
            ]
        }
    elif device_info.get("device_code") == 'KT01':
        test_data = {
            "device_name":"{}".format(device_info.get("device_name")),
            "device_pic": "KT01.jpg",
            "device_sn": "KT",
            "device_factory":"美的",
            "device_version": "KT",
            "device_location":"",
            "device_info":[
                {"device_info_name": "冷量kW", "device_info_value": "65"},
                {"device_info_name": "热量kW", "device_info_value": "70"},
                {"device_info_name": "380V制冷输入功率kW", "device_info_value": "19.1"},
                {"device_info_name": "380V风机输入功率kW", "device_info_value": "1.8"},
                {"device_info_name": "冷媒", "device_info_value": "R410A"},
                {"device_info_name": "机组运行重量kg", "device_info_value": "640"},
                {"device_info_name": "噪音dB（A）", "device_info_value": "67"},
            ],
            "device_status":[
                {"device_status_name": "开关", "device_status_value": "关机"},
            ]
        }
    elif device_info.get("device_code") == 'BL01':
        test_data = {
            "device_name":"{}".format(device_info.get("device_name")),
            "device_pic": "BL01.jpg",
            "device_sn": "BL01",
            "device_factory":"",
            "device_version": "BL",
            "device_location":"",
            "device_info":[
                {"device_info_name": "扬程m", "device_info_value": "28"},
                {"device_info_name": "流量m3/h", "device_info_value": "80"},
                {"device_info_name": "功率kW", "device_info_value": "11"},
                {"device_info_name": "效率%", "device_info_value": "70"},
                {"device_info_name": "运行重量kg", "device_info_value": "200"},
            ],
            "device_status":[
                {"device_status_name": "开关", "device_status_value": "关机"},
            ]
        }
    else:
        test_data = {
            "device_name":"未选择设备",
            "device_pic":"unknow.jpg",
            "device_sn":"",
            "device_factory":"",
            "device_version":"",
            "device_location":"",
            "device_info":[
                {"device_info_name":"", "device_info_value":"" },
            ],
            "device_status":[
                {"device_status_name":"", "device_status_value":"" },
            ]
        }
    return test_data

def get_device_ea_data(check_id):
    '''
    设备通用查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    device_info = get_device_name_by_id(check_id)

    # # 测试数据
    if device_info.get("device_type") == 'powerduct':
        test_data = {
            "device_name": "{}".format(device_info.get("device_name")),
            "device_pic": "PD.jpg",
            "device_sn": "",
            "device_factory": "",
            "device_version": "",
            "device_location": "",
            "device_info": [
                {
                    "device_info_name": "插座类型",
                    "device_info_value": "3孔",
                },
            ],
            "device_status": [
                {"device_status_name": "智能插座校时", "device_status_value": "正常" },
                {"device_status_name": "当前电能", "device_status_value": "0" },
                {"device_status_name": "信号强度", "device_status_value": "高" },
                {"device_status_name": "定时通断电开关", "device_status_value": "停用" },
            ]
        }
    else:
        test_data = {
            "device_name": "未选择设备",
            "device_pic": "unknow.jpg",
            "device_sn": "",
            "device_factory": "",
            "device_version": "",
            "device_location": "",
            "device_info": [
                {
                    "device_info_name": "",
                    "device_info_value": "",
                },
            ],
            "device_status": [
                {
                    "device_status_name": "",
                    "device_status_value": "",
                },
            ]
        }
    return test_data


def get_security_camera_data(check_id):
    '''
    安防摄像头设备查询接口，使用唯一id 查询设备信息
    :return: dict
    '''

    device_info = get_device_name_by_id(check_id)

    # # 测试数据
    if device_info.get("device_type") == 'cam':
        test_data = {
            "device_name":"{}".format(device_info.get("device_name")),
            "device_pic":"{}.jpg".format(device_info.get("device_code")),
            "device_sn":"cam",
            "device_factory":"宇视",
            "device_version":"cam",
            "device_location":"",
            "device_status":[
                {
                    "device_status_name":"摄像头状态",
                    "device_status_value":"on",
                }
            ],
            "camera_config":{
                "server_ip":"207.101.67.182",
                "user_name":"loadmin",
                "password":"d6bf4bb9a66419380a",
                "cam_code":"EC2004-139_1",
                "video_img":"{}.gif".format(device_info.get("device_position_id")),
            }
        }
    else:
        test_data = {
            "device_name": "摄像头",
            "device_pic": "CAM1.jpg",
            "device_sn": "",
            "device_factory": "",
            "device_version": "",
            "device_location": "",
            "device_status": [
                {
                    "device_status_name": "摄像头状态",
                    "device_status_value": "",
                }
            ],
            "camera_config": {
                "server_ip": "207.101.67.182",
                "user_name": "loadmin",
                "password": "d6bf4bb9a66419380a",
                "cam_code": "EC2004-139_1",
                "video_img": "a16.gif",
            }
        }
    logger.debug(test_data)
    return test_data


def get_security_device_data(check_id):
    '''
    安防设备查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    check_name = get_name_by_id(check_id)
    # # 测试数据
    test_data = {
        "device_name":"红外报警器{}".format(check_name),
        "device_pic":"Infrared_alarm01.jpg",
        "device_sn":"ABC123",
        "device_factory":"西门子",
        "device_version":"ia1001",
        "device_location":"1号楼1层",
        "device_status":[
            {
                "device_status_name":"运行状态",
                "device_status_value":"正常",
            },
        ]
    }
    return test_data


def get_fire_equipment_data(check_id):
    '''
    消防设备查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    check_name = get_name_by_id(check_id)

    # # 测试数据
    test_data = {
        "device_name":"消防报警器 {}".format(check_name),
        "device_pic":"fire_alarm01.jpg",
        "device_sn":"ABC123",
        "device_factory":"西门子",
        "device_version":"fa1032",
        "device_location":"1号楼1层",
        "device_status":[
            {
                "device_status_name":"运行状态",
                "device_status_value":"正常",
            },
        ]
    }
    return test_data


def update_user_data(user_data_dict):
    '''
    :param user_data_dict:
    :return:
    '''
    # # 测试数据
    test_data = {
        "password": user_data_dict.get('password'),
        "nickname": user_data_dict.get('nickname'),
        "phone": user_data_dict.get('phone'),
    }
    return test_data


def update_area_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''
    # # 测试数据
    test_data = {
        "land_area": data_dict.get('land_area'),
        "buildings_amount": data_dict.get('buildings_amount'),
        "buildings_area": data_dict.get('buildings_area'),
        "floor_area_ratio": data_dict.get('floor_area_ratio'),
        "greening_rate": data_dict.get('greening_rate'),
        "company_amount": data_dict.get('company_amount'),
        "area_people_amount": data_dict.get('area_people_amount'),
    }
    return test_data

def update_building_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''
    # # 测试数据
    test_data ={
        "building_id": data_dict.get('building_id'),
        "building_name": data_dict.get('building_name'),
        "building_function": data_dict.get('building_function'),
        "building_area": data_dict.get('building_area'),
        "building_time": data_dict.get('building_time'),
        "building_height": data_dict.get('building_height'),
        "building_floors": data_dict.get('building_floors'),
    }
    return test_data

def check_room_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''
    # # 测试数据
    test_data ={
        "room_id": data_dict.get('room_id'),
        "room_name": data_dict.get('room_name'),
    }
    return test_data

def update_room_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''
    # # 测试数据
    test_data ={
        "room_id": data_dict.get('room_id'),
        "room_name": data_dict.get('room_name'),
    }
    return test_data

def check_property_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''

    return_data = {
        "check_name": PROPERTY_DICT.get(data_dict.get('check_id')),
        "value_list": get_property_data_by_date_type(data_dict.get('start_date'), data_dict.get('end_date'), data_dict.get('check_id'))
    }
    # return test_data
    return return_data

def update_property_data(data_dict):
    '''
    :param data_dict:
    :return:
    '''
    # update_property_data_by_date_type('update', '2019-07-15', 'gas_other', '1230', '6fb50d7e-1e54-11e9-98ce-00163e10c840')
    flag = update_property_data_by_date_type(data_dict.get('update_type'),
                                             data_dict.get('date'),
                                             data_dict.get('check_id'),
                                             data_dict.get('update_value'),
                                             data_dict.get('uid'))

    return flag


def get_control_check_wlw_data(device_type):
    '''
    物联网设备控制命令查询接口，使用唯一id 查询设备类型
    :return: dict
    '''
    # check_name = get_name_by_id(check_id)
    device_type_dict = {"acfresh": "空调_新风机组",
                   "acfan": "空调_风机管盘",
                   "accold": "空调_制冷机组",
                   "socket": "智能插座",
                   "coldwater": "冷水泵"}
    # 测试数据
    test_data = {}
    if device_type == 'acfresh':
        test_data = {
            # "device_name": "空调_新风机组",
            "device_name": device_type_dict.get(device_type),
            "device_status": {
                "acfresh_set_mode_time_or_order": "1",
                "acfresh_set_switch": "1",
                "acfresh_set_temperature": 20,
                "timing_orders_enable": "1"
            },
            "timing_orders": [
                {
                    "timing_set_device_id": "111abc",
                    "timing_set_order_id": "1",
                    "timing_set_order": "1",
                    "timing_set_mode": "1",
                    "timing_set_date": "2019-05-15",
                    "timing_set_time": "00:09:10",
                    "enable": "1",
                },
                {
                    "timing_set_device_id": "112abc",
                    "timing_set_order_id": "1",
                    "timing_set_order": "1",
                    "timing_set_mode": "3",
                    "timing_set_date": "1",
                    "timing_set_time": "00:09:10",
                    "enable": "1",
                },
            ]
        }
    elif device_type == 'acfan':
        test_data = {
            # "device_name": "空调_风机管盘",
            "device_name": device_type_dict.get(device_type),
            "device_status": {
                "acfan_set_switch": "1",
                "acfan_set_mode": "1",
                "acfan_set_pm25": 150,
                "acfan_set_season": "1",
                "acfan_set_summer_min_temperature": 26,
                "acfan_set_winter_max_temperature": 17,
                "acfan_set_pm25_value": 16,
                "acfan_set_temperature_value": 3,
                "acfan_set_lcd_light": "1",
                "timing_orders_enable": "1"
            },
            "timing_orders": [
                {
                    "timing_set_device_id": "111abc",
                    "timing_set_order_id": "1",
                    "timing_set_order": "1",
                    "timing_set_mode": "1",
                    "timing_set_date": "2019-05-15",
                    "timing_set_time": "00:09:10",
                    "enable": "1",
                },
                {
                    "timing_set_device_id": "112abc",
                    "timing_set_order_id": "1",
                    "timing_set_order": "1",
                    "timing_set_mode": "3",
                    "timing_set_date": "1",
                    "timing_set_time": "00:09:10",
                    "enable": "1",
                },
            ]
        }
    elif device_type == 'accold':
        test_data = {
            # "device_name": "空调_制冷机组",
            "device_name": device_type_dict.get(device_type),
            "device_status": {
                "accold_set_input_cold_water_switch": "1",
                "accold_set_output_cold_water_switch": "1",
                "accold_set_input_hot_water_switch": "1",
                "accold_set_output_hot_water_switch": "1",
                "accold_set_ac_switch": "1",
                "timing_orders_enable": "1"
            },
            "timing_orders": [
                {
                    "timing_set_device_id": "111abc",
                    "timing_set_order_id": "1",
                    "timing_set_order": "1",
                    "timing_set_mode": "1",
                    "timing_set_date": "2019-05-15",
                    "timing_set_time": "00:09:10",
                    "enable": "1",
                },
                {
                    "timing_set_device_id": "112abc",
                    "timing_set_order_id": "1",
                    "timing_set_order": "1",
                    "timing_set_mode": "3",
                    "timing_set_date": "1",
                    "timing_set_time": "00:09:10",
                    "enable": "1",
                },
            ]
        }
    elif device_type == 'socket':
        test_data = {
            # "device_name": "智能插座",
            "device_name": device_type_dict.get(device_type),
            "device_status": {
                "socket_set_switch": "1",
                "timing_orders_enable": "1"
            },
            "timing_orders": [
                {
                    "timing_set_device_id": "111abc",
                    "timing_set_order_id": "1",
                    "timing_set_order": "1",
                    "timing_set_mode": "1",
                    "timing_set_date": "2019-05-15",
                    "timing_set_time": "00:09:10",
                    "enable": "0",
                }
            ]
        }
    elif device_type == 'coldwater':
        test_data = {
            # "device_name": "冷水泵",
            "device_name": device_type_dict.get(device_type),
            "device_status": {
                "coldwater_set_switch": "1",
                "timing_orders_enable": "1"
            },
            "timing_orders": [
                {
                    "timing_set_device_id": "111abc",
                    "timing_set_order_id": "1",
                    "timing_set_order": "1",
                    "timing_set_mode": "1",
                    "timing_set_date": "2019-05-15",
                    "timing_set_time": "00:09:10",
                    "enable": "0",
                }
            ]
        }
    else:
        test_data = 'unknown device type'


    return test_data

if __name__ == '__main__':
    # print('---', get_name_by_id('room_a2f228'))

    # print(get_property_data_by_date_type('2019-02-01','2019-02-19','gas_boiler'))

    # update_property_data_by_date_type('add', '2019-07-15', 'gas_other', '1213', '6fb50d7e-1e54-11e9-98ce-00163e10c840')
    update_property_data_by_date_type('update', '2019-07-15', 'gas_other', '1230', '6fb50d7e-1e54-11e9-98ce-00163e10c840')
    # update_property_data_by_date_type('delete', '2019-07-15', 'gas_other', '123', '6fb50d7e-1e54-11e9-98ce-00163e10c840')

