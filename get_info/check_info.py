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
    # 查询园区概况
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