# _*_ coding:utf-8 _*_
# Filename: check_info.py
# Author: pang song
# python 3.6
# Date: 2018/12/26
'''
三、信息接口
'''
import datetime
from utils import mysql_utils

WEEK_NAMES = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']


def get_name_by_id(check_id):
    '''
    get name by check_id
    :return: name
    '''
    data_conn = mysql_utils.Database()
    sql1 = "select position_name from yf_bim_position_info where position_id = '{pid}'".format(pid=check_id)
    row1 = data_conn.query_one(sql1)
    # print(row1)
    if row1 == None:
        row1 = ''
    else:
        row1 = row1[0]
    return row1

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
    data_conn = mysql_utils.Database()
    sql1 = "select * from yf_bim_area_overview"
    row1 = data_conn.query_one(sql1)
    print(row1)

    sql2 = "select company_type, count(1) from yf_bim_companys_info group by company_type"
    row2 = data_conn.query_all(sql2)
    print(row2)

    data_area_overview = {
        "land_area": row1[1],
        "buildings_amount": row1[2],
        "buildings_area": row1[3],
        "floor_area_ratio": row1[4],
        "greening_rate": row1[5],
        "company_amount": row1[6],
        "area_people_amount": row1[7],
        "companys_ratio": [
            {
                "ratio_name": row2[1][0],
                "ratio_value": row2[1][1]
            },
            {
                "ratio_name": row2[0][0],
                "ratio_value": row2[0][1]
            }]
    }
    print(data_area_overview)
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
    print(test_data_area_overview)
    # return test_data_area_overview
    return data_area_overview

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
    data_conn = mysql_utils.Database()
    sql1 = "select * from yf_bim_building_overview where id = {id}".format(id=1)
    row1 = data_conn.query_one(sql1)
    print(row1)
    # # 测试数据
    data_building_overview = {
        "building_name": row1[1],
        "building_function": row1[2],
        "building_area": row1[3],
        "building_time": row1[4],
        "building_height": row1[5],
        "building_floors": row1[6]
    }
    # return test_data_building_overview
    return data_building_overview


def get_env_outdoor():
    '''
    查询室外环境 实时
    :return: dict
    '''
    data_conn = mysql_utils.Database()
    sql1 = "select * from yf_bim_env_outdoor order by ctime desc limit 1"
    row1 = data_conn.query_one(sql1)
    print(row1)
    data_env_outdoor = {
        "temperature": row1[1],
        "humidity": row1[2],
        "wind_direction": row1[3],
        "wind_speed": row1[4],
        "precipitation": row1[5],
        "air_pressure": row1[6],
        "pm2.5": row1[7]
    }
    print(data_env_outdoor)
    return data_env_outdoor

def env_outdoor_history(data_type):
    '''
    查询室外环境 历史数据
    :return: dict
    '''
    data_conn = mysql_utils.Database()

    # 获取查询时间
    # start_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    # print(start_time)

    # end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    # print(type(end_time))
    # print(end_time)

    # 初始化返回数据
    test_data_env_outdoor_history = {}
    data_env_outdoor_history = {"data_list":[]}

    # 按年查询 显示当年每月数据
    if 'year' == data_type:

        # 获取查询时间
        start_time = datetime.datetime.now().strftime("%Y") + "-01-01 00:01"
        # print(start_time)
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        # print(end_time)

        sql1 = """
                select DATE_FORMAT(ctime,'%%Y%%m') cut_time,
                max(temperature), 
                min(temperature),
                avg(humidity),
                avg(wind_speed),
                avg(precipitation),
                avg(air_pressure),
                avg(pm25) 
                from yf_bim_env_outdoor 
                where ctime between '{stime}' and '{etime}'
                group by cut_time;
                """.format(stime=start_time, etime=end_time)
        print(sql1)
        row1 = data_conn.query_all(sql1)
        print(row1)

        for row1_one in row1:
            data_env_outdoor_history['data_list'].append({
                "data_time": row1_one[0][-2:],
                "temperature_high": row1_one[1],
                "temperature_low": row1_one[2],
                "humidity": str(row1_one[3]),
                "wind_speed": str(row1_one[4]),
                "precipitation": str(row1_one[5]),
                "air_pressure": str(row1_one[6]),
                "pm2.5": str(row1_one[7])
            })
        print(data_env_outdoor_history)

    # 按月查询，显示30天内数据
    elif 'month' == data_type:
        # 获取查询时间
        start_time = start_time = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M")
        print(start_time)
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print(end_time)

        sql1 = """
                select DATE_FORMAT(ctime,'%%Y%%m%%d') cut_time,
                max(temperature), 
                min(temperature),
                avg(humidity),
                avg(wind_speed),
                avg(precipitation),
                avg(air_pressure),
                avg(pm25) 
                from yf_bim_env_outdoor 
                where ctime between '{stime}' and '{etime}'
                group by cut_time;
                """.format(stime=start_time, etime=end_time)
        print(sql1)
        row1 = data_conn.query_all(sql1)
        print(row1)

        for row1_one in row1:
            data_env_outdoor_history['data_list'].append({
                "data_time": row1_one[0][-2:],
                "temperature_high": row1_one[1],
                "temperature_low": row1_one[2],
                "humidity": str(row1_one[3]),
                "wind_speed": str(row1_one[4]),
                "precipitation": str(row1_one[5]),
                "air_pressure": str(row1_one[6]),
                "pm2.5": str(row1_one[7])
            })
        print(data_env_outdoor_history)

    # 按天查询，显示最近24小时数据
    elif 'day' == data_type:
        # 获取查询时间
        start_time = start_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        print(start_time)
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print(end_time)

        sql1 = """
                select DATE_FORMAT(ctime,'%%Y%%m%%d%%H') cut_time,
                max(temperature), 
                min(temperature),
                avg(humidity),
                avg(wind_speed),
                avg(precipitation),
                avg(air_pressure),
                avg(pm25) 
                from yf_bim_env_outdoor 
                where ctime between '{stime}' and '{etime}'
                group by cut_time;
                """.format(stime=start_time, etime=end_time)
        print(sql1)
        row1 = data_conn.query_all(sql1)
        print(row1)

        for row1_one in row1:
            data_env_outdoor_history['data_list'].append({
                "data_time": row1_one[0][-2:],
                "temperature_high": row1_one[1],
                "temperature_low": row1_one[2],
                "humidity": str(row1_one[3]),
                "wind_speed": str(row1_one[4]),
                "precipitation": str(row1_one[5]),
                "air_pressure": str(row1_one[6]),
                "pm2.5": str(row1_one[7])
            })
        print(data_env_outdoor_history)

    # return test_data_env_outdoor_history
    return data_env_outdoor_history

def get_env_indoor(position_id):
    '''
    查询室内环境 实时
    :return: dict
    '''

    data_conn = mysql_utils.Database()
    if position_id == "":
        # 默认值，取大厅数据 B5项目风机盘管控制一层自助办理区地址5的控制器
        sql1 = "select * from yf_bim_env_indoor where position_id = 'K1_102_5L_ZZQ' order by ctime desc limit 1"

    else:
        sql1 = "select * from yf_bim_env_indoor where position_id = '{pid}' order by ctime desc limit 1".format(pid=position_id)
    row1 = data_conn.query_one(sql1)
    print(row1)
    # 查不到数据
    if row1 == None:
        data_env_indoor = {
            "position_name": "unknow",
            "temperature": "0",
            "humidity": "0",
            "voc": "0",
            "pm2.5": "0"
        }
    else:
        data_env_indoor = {
            "position_name": row1[2],
            "temperature": row1[3],
            "humidity": row1[4],
            "voc": row1[5],
            "pm2.5": row1[6]
        }
    print('data_env_indoor', data_env_indoor)

    return data_env_indoor


def env_indoor_history(position_id, data_type):
    '''
    查询室内环境 历史数据
    :return: dict
    '''
    data_conn = mysql_utils.Database()

    # 初始化返回数据
    data_env_indoor_history = {"data_list": []}

    if position_id == "":
        # 默认值，取大厅数据 B5项目风机盘管控制一层自助办理区地址5的控制器
        position_id = 'K1_102_5L_ZZQ'

    print(position_id)


    # 按年查询 显示当年每月数据
    if 'year' == data_type:
        # 获取查询时间
        start_time = datetime.datetime.now().strftime("%Y") + "-01-01 00:01"
        # print(start_time)
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        # print(end_time)

        sql1 = """
                select DATE_FORMAT(ctime,'%%Y%%m') cut_time,
                max(temperature), 
                min(temperature),
                avg(humidity),
                avg(voc),
                avg(pm25) 
                from yf_bim_env_indoor 
                where position_id = '{pid}' and ctime between '{stime}' and '{etime}'
                group by cut_time;
                """.format(pid=position_id, stime=start_time, etime=end_time)
        print(sql1)
        row1 = data_conn.query_all(sql1)
        print(row1)
        # 查不到数据
        if len(row1) == 0:
            for row1_one in range(1,13):
                data_env_indoor_history['data_list'].append({
                    "data_time": str(row1_one),
                    "temperature_high": "0",
                    "temperature_low": "0",
                    "humidity": "0",
                    "voc": "0",
                    "pm2.5": "0"
                })
            print(data_env_indoor_history)

        else:
            for row1_one in row1:
                data_env_indoor_history['data_list'].append({
                    "data_time": row1_one[0][-2:],
                    "temperature_high": row1_one[1],
                    "temperature_low": row1_one[2],
                    "humidity": str(row1_one[3]),
                    "voc": str(row1_one[4]),
                    "pm2.5": str(row1_one[5])
                })
            print(data_env_indoor_history)

    elif 'month' == data_type:

        # 获取查询时间
        start_time = start_time = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M")
        print(start_time)
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print(end_time)

        sql1 = """
                select DATE_FORMAT(ctime,'%%Y%%m%%d') cut_time,
                max(temperature), 
                min(temperature),
                avg(humidity),
                avg(voc),
                avg(pm25) 
                from yf_bim_env_indoor 
                where position_id = '{pid}' and ctime between '{stime}' and '{etime}'
                group by cut_time;
                """.format(pid=position_id, stime=start_time, etime=end_time)
        print(sql1)
        row1 = data_conn.query_all(sql1)
        print(row1)
        # 查不到数据
        if len(row1) == 0:
            for row1_one in range(1, 31):
                data_env_indoor_history['data_list'].append({
                    "data_time": str(row1_one),
                    "temperature_high": "0",
                    "temperature_low": "0",
                    "humidity": "0",
                    "voc": "0",
                    "pm2.5": "0"
                })
            print(data_env_indoor_history)

        else:
            for row1_one in row1:
                data_env_indoor_history['data_list'].append({
                    "data_time": row1_one[0][-2:],
                    "temperature_high": row1_one[1],
                    "temperature_low": row1_one[2],
                    "humidity": str(row1_one[3]),
                    "voc": str(row1_one[4]),
                    "pm2.5": str(row1_one[5])
                })
            print(data_env_indoor_history)


    elif 'day' == data_type:
        # 获取查询时间
        start_time = start_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        print(start_time)
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print(end_time)


        sql1 = """
                select DATE_FORMAT(ctime,'%%Y%%m%%d%%H') cut_time,
                max(temperature), 
                min(temperature),
                avg(humidity),
                avg(voc),
                avg(pm25) 
                from yf_bim_env_indoor 
                where position_id = '{pid}' and ctime between '{stime}' and '{etime}'
                group by cut_time;
                """.format(pid=position_id, stime=start_time, etime=end_time)
        print(sql1)
        row1 = data_conn.query_all(sql1)
        print(row1)
        # 查不到数据
        if len(row1) == 0:
            for row1_one in range(24):
                data_env_indoor_history['data_list'].append({
                    "data_time": str(row1_one),
                    "temperature_high": "0",
                    "temperature_low": "0",
                    "humidity": "0",
                    "voc": "0",
                    "pm2.5": "0"
                })
            print(data_env_indoor_history)

        else:
            for row1_one in row1:
                data_env_indoor_history['data_list'].append({
                    "data_time": row1_one[0][-2:],
                    "temperature_high": row1_one[1],
                    "temperature_low": row1_one[2],
                    "humidity": str(row1_one[3]),
                    "voc": str(row1_one[4]),
                    "pm2.5": str(row1_one[5])
                })
            print(data_env_indoor_history)

    return data_env_indoor_history

def get_energy_overview(check_id):
    '''
    查询用能概况
    :return: dict
    '''
    # 获取查询起止时间 一周
    start_time = start_time = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M")
    print(start_time)
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(end_time)

    data_conn = mysql_utils.Database()

    # 初始化返回数据
    data_energy_overview = {
        "check_name": "{}用能情况".format(check_id),
        "electricity": [],
        "gas": [],
        "water": []
    }

    # 用电情况查询
    if check_id == "":
        # 默认值，取总体数据
        sql_e = """
                SELECT DATE_FORMAT(ctime,'%%Y%%m%%d%%w') cut_time, 
                sum(CASE value_type WHEN 'building' THEN value ELSE 0 END) as '建筑',
                sum(CASE value_type WHEN 'ac' THEN value ELSE 0 END) as '空调',
                sum(CASE value_type WHEN 'device' THEN value ELSE 0 END) as '电器',
                sum(CASE value_type WHEN 'other' THEN value ELSE 0 END) as '其他'
                FROM yf_bim_db.yf_bim_energy_electricity
                where ctime between '{stime}' and '{etime}'
                group by cut_time;
                """.format(stime=start_time, etime=end_time)

    else:
        # 根据位置id取值
        sql_e = """
                SELECT DATE_FORMAT(ctime,'%%Y%%m%%d%%w') cut_time, 
                sum(CASE value_type WHEN 'building' THEN value ELSE 0 END) as '建筑',
                sum(CASE value_type WHEN 'ac' THEN value ELSE 0 END) as '空调',
                sum(CASE value_type WHEN 'device' THEN value ELSE 0 END) as '电器',
                sum(CASE value_type WHEN 'other' THEN value ELSE 0 END) as '其他'
                FROM yf_bim_db.yf_bim_energy_electricity
                where position_id like '%%{pid}%%' and ctime between '{stime}' and '{etime}'
                group by cut_time;
                """.format(pid=check_id, stime=start_time, etime=end_time)

    row_e = data_conn.query_all(sql_e)
    print(row_e)

    # 电能赋值
    for row in row_e:
        data_energy_overview["electricity"].append({
                "time":WEEK_NAMES[int(row[0][-1])],
                "value_list":[{"name":"建筑", "value": str(row[1]),},
                              {"name":"空调", "value": str(row[2]),},
                              {"name":"电器", "value": str(row[3]),},
                              {"name":"其他", "value": str(row[4]),},],
            })

    # 用气情况查询
    sql_g = """
                    SELECT DATE_FORMAT(value_date,'%%Y%%m%%d%%w') cut_time, 
                    sum(CASE value_type WHEN 'boiler' THEN value ELSE 0 END) as '采暖',
                    sum(CASE value_type WHEN 'kitchen' THEN value ELSE 0 END) as '厨房',
                    sum(CASE value_type WHEN 'other' THEN value ELSE 0 END) as '其他'
                    FROM yf_bim_db.yf_bim_energy_gas
                    where ctime between '{stime}' and '{etime}'
                    group by cut_time;
                    """.format(stime=start_time, etime=end_time)

    row_g = data_conn.query_all(sql_g)
    print(row_g)
    # 用气赋值
    for row in row_g:
        data_energy_overview["gas"].append({
            "time": WEEK_NAMES[int(row[0][-1])],
            "value_list": [{"name": "采暖", "value": str(row[1]), },
                           {"name": "厨房", "value": str(row[2]), },
                           {"name": "其他", "value": str(row[3]), }, ],
        })

    # 用水情况查询
    sql_w = """
            SELECT DATE_FORMAT(value_date,'%%Y%%m%%d%%w') cut_time, 
            sum(CASE value_type WHEN 'live' THEN value ELSE 0 END) as '生活',
            sum(CASE value_type WHEN 'ac' THEN value ELSE 0 END) as '空调',
            sum(CASE value_type WHEN 'kitchen' THEN value ELSE 0 END) as '厨房',
            sum(CASE value_type WHEN 'other' THEN value ELSE 0 END) as '其他'
            FROM yf_bim_db.yf_bim_energy_water
            where ctime between '{stime}' and '{etime}'
            group by cut_time;
            """.format(stime=start_time, etime=end_time)

    row_w = data_conn.query_all(sql_w)
    print("row_w", row_w)
    # 用气赋值
    for row in row_w:
        data_energy_overview["water"].append({
            "time": WEEK_NAMES[int(row[0][-1])],
            "value_list": [{"name": "生活", "value": str(row[1]), },
                           {"name": "空调", "value": str(row[2]), },
                           {"name": "厨房", "value": str(row[3]), },
                           {"name": "其他", "value": str(row[4]), }, ],
        })

    # print(data_energy_overview)
    # exit()
    return data_energy_overview


def get_energy_electricity_overview(check_id):
    '''
    用电情况通用查询接口1，使用唯一id进行查询，园区用电、建筑用电返回各建筑、各层用电占比
    :return: dict
    '''
    data_conn = mysql_utils.Database()

    # 初始化返回数据
    data_energy_electricity_overview = {
        "check_name": "{}用能情况".format(check_id),
        "electricity": "",
        "history_year_list": [],
        "history_month_list": [],
        "history_day_list": [],
        "electricity_ratio1": [],
        "electricity_ratio2": [],
    }

    if check_id == "":
        # 默认值，取一层变配电室3三个表最后数值
        sql_total_e = "select * from yf_bim_env_indoor where check_id = '' order by ctime desc limit 1"

    else:
        sql_total_e = "select * from yf_bim_env_indoor where check_id = '{pid}' order by ctime desc limit 1".format(pid=check_id + '_DN')
    row1 = data_conn.query_one(sql_total_e)
    print(row1)
    # todo
    sql_total_e = """
        
    """

    print(data_energy_electricity_overview)

    # 测试数据
    test_data = {
        "check_name":"永丰B5综合服务楼{}".format(check_id),
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
    # return data_energy_electricity_overview


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


def get_device_ac_data(check_id):
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
                    "device_info_name":"风量",
                    "device_info_value":"611m3",
                }
            ],
            "device_status":[
                {
                    "device_status_name":"室内温度",
                    "device_status_value":"23摄氏度",
                },
                {
                    "device_status_name":"冷水阀开关状态",
                    "device_status_value":"on",
                },
                {
                    "device_status_name":"报警信息",
                    "device_status_value":"无故障",
                }
            ]
        }
    else:
        test_data = {
            "device_name":"空调-水泵，{}".format(check_id),
            "device_pic":"ac_water_pump.jpg",
            "device_sn":"ABC123",
            "device_factory":"西门子",
            "device_version":"cv100",
            "device_location":"1号楼2层",
            "device_info":[
                {
                    "device_info_name":"扬程",
                    "device_info_value":"126m",
                },
                {
                    "device_info_name":"流量",
                    "device_info_value":"216m3",
                },
                {
                    "device_info_name":"功率",
                    "device_info_value":"3000w",
                }
            ],
            "device_status":[
                {
                    "device_status_name":"开关状态",
                    "device_status_value":"on",
                },
                {
                    "device_status_name":"报警信息",
                    "device_status_value":"无故障",
                }
            ]
        }
    return test_data

def get_device_ea_data(check_id):
    '''
    设备通用查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    # # 测试数据
    if check_id[0] == 'a':
        test_data = {
            "device_name": "智能插座，{}".format(check_id),
            "device_pic": "switch01.jpg",
            "device_sn": "ABC123{}".format(check_id),
            "device_factory": "小米",
            "device_version": "小米智能插座",
            "device_location": "1号楼2层控制室",
            "device_info": [
                {
                    "device_info_name": "插座类型",
                    "device_info_value": "5孔",
                },
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
    else:
        test_data = {
            "device_name": "其他电器，{}".format(check_id),
            "device_pic": "ea01.jpg",
            "device_sn": "ABC123{}".format(check_id),
            "device_factory": "霍尼韦尔",
            "device_version": "",
            "device_location": "1号楼3层控制室",
            "device_info": [
                {
                    "device_info_name": "类型1",
                    "device_info_value": "设备1",
                },
                {
                    "device_info_name": "类型2",
                    "device_info_value": "设备2",
                },
            ],
            "device_status": [
                {
                    "device_status_name": "开关状态",
                    "device_status_value": "on",
                },
            ]
        }
    return test_data


def get_security_camera_data(check_id):
    '''
    安防摄像头设备查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    # # 测试数据
    test_data = {
        "device_name":"安防摄像头1，{}".format(check_id),
        "device_pic":"cam01.jpg",
        "device_sn":"ABC123",
        "device_factory":"西门子",
        "device_version":"cv100",
        "device_location":"1号楼1层",
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
        }
    }
    return test_data


def get_security_device_data(check_id):
    '''
    安防设备查询接口，使用唯一id 查询设备信息
    :return: dict
    '''
    # # 测试数据
    test_data = {
        "device_name":"红外报警器{}".format(check_id),
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
    # # 测试数据
    test_data = {
        "device_name":"消防报警器 {}".format(check_id),
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

def update_property_data(data_dict):
    '''

    :param data_dict:
    :return:
    '''
    # # 测试数据
    test_data ={
        "date": data_dict.get('date'),
        "gas_boiler": data_dict.get('value1'),
        "gas_kitchen": data_dict.get('value2'),
        "value1": data_dict.get('value3'),
        "value2": data_dict.get('value4'),
    }
    return test_data

if __name__ == '__main__':
    print('---', get_name_by_id('room_a2f228'))
    exit()
    # print(get_area_overview())
    # print(get_building_overview())
    # print(get_env_outdoor())
    # print(env_outdoor_history('year'))
    # print(env_outdoor_history('month'))
    # print(env_outdoor_history('day'))
    # print(get_env_indoor('K1_102_5L_ZZQa'))
    # print(env_indoor_history('111','month'))
    # print(env_indoor_history('K1_102_5L_ZZQ','month'))
    # print(env_indoor_history('K1_102_5L_ZZQ','day'))
    # print(env_indoor_history('11','day'))
    # print(get_energy_overview('b01f03'))
    print(get_energy_electricity_overview('b01f03'))


