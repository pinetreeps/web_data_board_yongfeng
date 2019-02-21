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


if __name__ == '__main__':

    # 数据表导入 房间、楼层、位置信息表
    df = pd.read_excel('/Users/pinetree_mac/ps_use/start_up_business/web_data_board_yongfeng/文档/数据显示对照表190221.xls',
                       'Sheet3', header = None, names = ['a', 'id', 'name'])
    print(df.head(5))
    print(df['id'].values[139])

    if df['id'].values[0][0:1] == 'b':
        print('--------', df['id'].values[0])

    # exit()

    data_conn = mysql_utils.Database()

    fid = ''
    ptype=''

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

    exit()




