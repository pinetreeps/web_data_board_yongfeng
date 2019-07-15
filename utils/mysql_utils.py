# _*_ coding:utf-8 _*_
# import MySQLdb

# import datetime
import os

# import mysql.connector
import pymysql
import logging
# import ConfigParser
import config

# cf = ConfigParser.ConfigParser()
# filename = 'config.ini'
# curr_dir = os.path.dirname(os.path.abspath(__file__))
# config_file = os.path.join(curr_dir, filename)
# cf.read(config_file)  # 读取配置文件

remoteSSH = config.IS_LOCAL
# 这个参数主要是用于控制远程ssh连接数据库还是本地连接数据库,True为远程，False为本地

server_ip = config.SSH_SERVER_IP
ssh_username = config.SSH_USERNAME
ssh_password = config.SSH_PASSWORD
db_username = config.DB_USERNAME
db_password = config.DB_PASSWORD
db_host = config.DB_HOST
database = config.DB_DATABASE
charset = config.DB_CHARSET

logger = logging.getLogger("main")

def get_server():
    if remoteSSH:
        from sshtunnel import SSHTunnelForwarder
        return SSHTunnelForwarder(
                (server_ip, 22),
                ssh_password=ssh_password,
                ssh_username=ssh_username,
                remote_bind_address=(db_host, 3306)
                )
    return None


class Database:
    server = get_server()

    def __init__(self):
        config = dict(
            user=db_username,
            password=db_password,
            host=db_host,
            database=database,
            charset=charset,
        )
        if remoteSSH:
            self.server.start()
            config = dict(
                user=db_username,
                password=db_password,
                host=db_host,
                port=self.server.local_bind_port,
                database=database,
                charset=charset,
            )

        try:
            self.db_connection = pymysql.connect(**config)

            # self.connection = mysql.connector.connect(**config)
        except Exception as err:
            logger.error(repr(err))
        self.cursor = self.db_connection.cursor()
        # self.cursor = self.connection.cursor(buffered=True, dictionary=True)

    def insert_del_update(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            row_count = self.cursor.rowcount
            self.db_connection.commit()
            return row_count
        except Exception as err:
            logger.error(repr(err))
            self.db_connection.rollback()

    def insert_del_update_query_one(self, query1, query2, params1=(), params2=()):
        try:
            self.cursor.execute(query1, params1)
            self.cursor.execute(query2, params2)
            self.db_connection.commit()
        except Exception as err:
            logger.error(repr(err))
            self.db_connection.rollback()
        return self.cursor.fetchone()

    def query_one(self, query, params=()):
        try:
            self.cursor.execute(query, params)
        except Exception as err:
            logger.error(repr(err))
        return self.cursor.fetchone()

    def query_all(self, query, params=()):
        try:
            self.cursor.execute(query, params)
        except Exception as err:
            logger.error(repr(err))
        return self.cursor.fetchall()

    def query_all_no_params(self, query):
        try:
            self.cursor.execute(query)
            # res = self.cursor.fetchall()
        except Exception as err:
            logger.error(repr(err))
            # res = ()
        return  self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.db_connection.close()
        if remoteSSH:
            self.server.stop()

