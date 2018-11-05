# _*_ coding:utf-8 _*_
# Filename: config.py
# Author: pang song
# python 3.6
# Date: 2018/05/08

# --------------开关控制  --------------
# 这个参数主要是用于控制远程ssh连接数据库还是本地连接数据库 False为部署线上，True为本地
IS_LOCAL_DB = True

# --------------文件目录  --------------
# file_dir = "/Users/pinetree_mac/ps_use/py_works/document_tools/app/"

# --------------数据库配置--------------

DB_USERNAME = 'root'
DB_PASSWORD = 'pangsongpangsong'
DB_HOST = '127.0.0.1'
DB_PORT = '3307'
DB_DATABASE = 'yf_bim_db'
DB_CHARSET = 'utf8mb4'

# SSH
SSH_SERVER_IP = '39.105.61.38'
SSH_USERNAME = 'pangsong'
SSH_PASSWORD = 'pangsongpangsong'

# --------------用户注册邀请码--------------
APPLY_CODE = 'yongfeng2018'



