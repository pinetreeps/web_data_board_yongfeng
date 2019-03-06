# _*_ coding:utf-8 _*_
# Filename: data_loader.py
# Author: pang song
# python 3.6
# Date: 2019/02/21
'''
数据导入
'''
import pandas as pd
from utils import mysql_utils

def loader_position_info():
    # 数据表导入 房间、楼层、位置信息表
    df = pd.read_excel('/Users/pinetree_mac/ps_use/start_up_business/web_data_board_yongfeng/文档/数据显示对照表190221.xls',
                       'Sheet3', header=None, names=['a', 'id', 'name'])
    print(df.head(5))
    print(df['id'].values[139])

    if df['id'].values[0][0:1] == 'b':
        print('--------', df['id'].values[0])

    # exit()

    data_conn = mysql_utils.Database()

    fid = ''
    ptype = ''

    for i in range(0, 140):

        if df['id'].values[i][0:1] == 'b':
            # print('--------', df['id'].values[0])
            fid = 'area'
        elif df['id'].values[i][0:1] == 'f':
            fid = 'building_a'
        elif df['id'].values[i][0:1] == 'r':
            fid = 'floor_' + df['id'].values[i][5:8]
        else:
            print(' -------- error --------')

        print(df['id'].values[i], fid)

        sql = """
                    INSERT INTO `yf_bim_db`.`yf_bim_position_info`
                    (`position_id`,
                    `position_name`,
                    `position_type`,
                    `position_father_id`,
                    `ctime`,
                    `utime`)
                    VALUES
                    ('{pid}','{pname}','{ptype}','{pfid}', now(), now());
                """.format(pid=df['id'].values[i], pname=df['name'].values[i], ptype='position', pfid=fid)

        data_conn.insert_del_update(sql)

def loader_device_info():
    # 数据表导入 设备信息表
    df = pd.read_excel('/Users/pinetree_mac/ps_use/start_up_business/web_data_board_yongfeng/文档/数据显示对照表190305.xlsx',
                       '接口设备名称对照表', header=None, names=['a', 'id', 'name', 'code', 'zjcode'])
    print(df.head(5))
    print(len(df))
    print(df.iloc[652:, :])
    # exit()
    print(df[pd.isnull(df['code'])==True])
    df['code'] = df['code'].fillna('unknow')
    print('---------------')
    print(df[pd.isnull(df['code']) == True])

    # exit()

    data_conn = mysql_utils.Database()

    dpid = ''
    dtype = ''

    for i in range(511, 653):

        did = df['id'].values[i].split('_')
        dtype = did[0]
        dpid = did[1]

        print(df['id'].values[i], dpid, dtype)

        sql = """
                INSERT INTO `yf_bim_db`.`yf_bim_device_info`
                (
                `device_id`,
                `device_name`,
                `device_code`,
                `device_type`,
                `device_position_id`,
                `ctime`,
                `utime`)
                VALUES
                ( '{did}', '{dname}', '{dcode}', '{dtype}', '{dpid}', now(), now());
        """.format(did=df['id'].values[i], dname=df['name'].values[i], dcode=df['code'].values[i], dtype=dtype, dpid=dpid)

        data_conn.insert_del_update(sql)

if __name__ == '__main__':
    # loader_position_info()
    loader_device_info()

    exit()




