# _*_ coding:utf-8 _*_
# Filename: user_dal.py
# Author: pang song
# python 3.6
# Date: 2018/11/05

from yongfeng.utils import mysql_utils
from . import hash

from flask_login import UserMixin


# define profile.json constant, the file is used to
# save user name and password_hash
# 用户类
class User(UserMixin):
    def __init__(self, uid=None, uname=None, usergroup=None, nickname=None, mail=None, phone=None):
        self.uid = uid
        self.uname = uname
        self.usergroup = usergroup
        self.nickname = nickname
        self.mail = mail
        self.phone = phone

    def to_dict(self):
        return self.__dict__

    def get_id(self):
        return self.uid


#用户类操作类
class UserDal:
    def __init__(self):
        pass
    persist = None

    @classmethod #检查uid
    def check_uid(cls, params):
        sql = "select * from yf_bim_user_info where uid = %s"
        row = mysql_utils.Database().query_one(sql, (params['uid'],))
        if row is not None:
            # user = User(uid=row['uid'], uname=row['uname'], usergroup=row['user_group'],
            #                        nickname=row['nickname'], mail=row['mail'], phone=row['phone'])
            user = User(uid=row[1], uname=row[2], usergroup=row[4], nickname=row[5], mail=row[6], phone=row[7])

            # 实例化一个对象，将查询结果逐一添加给对象的属性
        else:
            return None
        return user

    # 通过用户名及密码查询用户对象
    @classmethod
    def login_auth(cls, params):
        # passwd = hash.salted_password(params['password'])
        passwd = params['password']

        sql = "select * from yf_bim_user_info where uname = %s and passwd = %s"
        row = mysql_utils.Database().query_one(sql, (params['uname'], passwd))
        print(row)
        if row is not None:
            # user = User(uid=row['uid'], uname=row['uname'], usergroup=row['user_group'],
            #                        nickname=row['nickname'], mail=row['mail'], phone=row['phone'])
            user = User(uid=row[1], uname=row[2], usergroup=row[4], nickname=row[5], mail=row[6], phone=row[7])
            # user = User(row)
            # 实例化一个对象，将查询结果逐一添加给对象的属性
        else:
            return None

        return user

    # 通过用户名及密码注册对象
    @classmethod
    def register(cls, params):
        if cls.register_name_check(params):
            # passwd = hash.salted_password(params['password'])
            passwd = params['password']
            if 'user_group' in params.keys():
                user_group = params['user_group']
            else:
                user_group = 'default'
            if 'phone' in params.keys():
                phone = params['phone']
            else:
                phone = None
            if 'mail' in params.keys():
                mail = params['mail']
            else:
                mail = None
            sql = "insert into yf_bim_user_info (uid, uname, passwd, user_group, nickname, mail, phone, ctime, utime) " \
                  "values (UUID(), %s, %s, %s, %s, %s, %s, now(), now())"
            rowcount = mysql_utils.Database().insert_del_update(sql, (params['uname'], passwd, user_group, params['nickname'],
                                                           mail, phone,))
            if rowcount > 0:
                return True
        else:
            return False

    # 通过用户名及密码注册对象
    @classmethod
    def register_name_check(cls, params):
        sql = "select * from yf_bim_user_info where uname = %s "
        row = mysql_utils.Database().query_one(sql, (params['uname'],))
        if row is not None:
            return False
        else:
            return True

if __name__ == '__main__':
    row = (11, '123', 'abc', '123', 'admin', 'Tom', None, None)
    user = User(uid=row[1], uname=row[2], usergroup=row[3], nickname=row[4], mail=row[5], phone=row[6])

