# _*_ coding:utf-8 _*_
# Filename: config.py
# Author: pang song
# python 3.6
# Date: 2018/05/08

# --------------开关控制  --------------
# 这个参数主要是用于控制远程ssh连接数据库还是本地连接数据库 False为部署线上，True为本地(需要远程访问数据库)
# IS_LOCAL = True
IS_LOCAL = False

# --------------文件目录  --------------
# 阿里云服务器
WORK_PATH = "/root/data1/web_data_board_yongfeng/"
# 本机
# WORK_PATH = "/Users/pinetree_mac/ps_use/py_works/web_data_board_yongfeng/"

# --------------日志文件配置--------------
LOGGING_FILE = WORK_PATH + "log/main.log"

# --------------mysql数据库配置--------------

DB_USERNAME = 'root'
# 永丰数据库密码
# DB_PASSWORD = 'yongfeng2018'
DB_PASSWORD = 'pangsongpangsong'
DB_HOST = '127.0.0.1'
DB_PORT = '3307'
DB_DATABASE = 'yf_bim_db'
DB_CHARSET = 'utf8mb4'

# SSH
SSH_SERVER_IP = '39.105.61.38'
SSH_USERNAME = 'pangsong'
SSH_PASSWORD = 'pangsongpangsong'

# --------------sql-server数据库配置--------------

DB_SS_USERNAME = 'sa'
DB_SS_PASSWORD = 'qw@123'
DB_SS_HOST = '192.168.1.54'
DB_SS_PORT = '1433'
DB_SS_DATABASE = 'RealInfo'
DB_SS_CHARSET = 'utf8'

# --------------用户注册邀请码--------------
APPLY_CODE = 'yongfeng2018'




