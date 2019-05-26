# _*_ coding:utf-8 _*_
# Filename: sqlserver_util.py
# Author: pang song
# python 3.6
# Date: 2019/01/24
'''
sql server 连接工具
'''
import pymssql
import logging

import config

logger = logging.getLogger("main")

db_username = config.DB_SS_USERNAME
db_password = config.DB_SS_PASSWORD
db_host = config.DB_SS_HOST
database = config.DB_SS_DATABASE
port = config.DB_SS_PORT
charset = config.DB_SS_CHARSET

'''
import pymssql
conn = pymssql.connect(host=host, user=user, password=password,
        database=database, charset='utf8', port='1433', as_dict=False)
cursor = conn.cursor()
sql = "select * from payment where id in (59,60)"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)

'''

class Database_sql_server:
    def __init__(self):
        config = dict(
            user=db_username,
            password=db_password,
            host=db_host,
            database=database,
            port=port,
            charset=charset,
        )

        try:
            self.db_connection = pymssql.connect(**config)

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

    def __del__(self):
        self.cursor.close()
        self.db_connection.close()

if __name__ == '__main__':
    sql_server_conn = Database_sql_server()
    # 室外温度
    check_id = 'QXZ_Temperature'

    # UPDATETIME, TAGNAME, TAGVALUE
    sql1 = "SELECT TOP 1 * FROM LASTDAVEDATA WHERE TAGNAME = '{name}' ORDER BY UPDATETIME DESC".format(name=check_id)
    row1 = sql_server_conn.query_one(sql1)
    print(row1)