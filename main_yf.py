# _*_ coding:utf-8 _*_
# Filename: main_yf.py
# Author: pang song
# python 3.6
# Date: 2018/11/05

from flask import Flask,request, render_template
import json
from auth import user_dal
# from auth import user_dal
from utils.is_json import is_json
from utils.post_json import post_json
import config
from get_info import check_info

from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return '<h1>Hello World! yong feng!</h1>'


# 登陆接口
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uname' in data.keys() and 'password' in data.keys():
                user = user_dal.UserDal().login_auth(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        if user is not None:
            return post_json(0, 'success', user.to_dict())
        else:
            return post_json(data='用户名或密码错误')
    else:
        return render_template('404.html')

# 登出接口
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'uname' in data.keys():
                success = True
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        data = json.loads(request.get_data())
        if success:
            return post_json(0, 'success', data='用户登出成功')
        else:
            return post_json(data='用户登出失败')
    else:
        return render_template('404.html')

# 注册接口
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uname' in data.keys() and 'password' in data.keys() and 'nickname' in data.keys() \
                    and 'apply_code' in data.keys():
                if data.get('apply_code') == config.APPLY_CODE:
                    success = user_dal.UserDal().register(data)
                else:
                    return '邀请码不正确'
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        if success:
            return post_json(0, 'success', data='注册成功')
        else:
            return post_json(data='注册失败')
    else:
        return render_template('404.html')

# 注册用户名重复检查接口
@app.route('/register_name_check', methods=['GET', 'POST'])
def register_name_check():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uname' in data.keys():
                success = user_dal.UserDal().register_name_check(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'

        if success:
            return post_json(0, 'success', data='注册用户名不存在，可以注册')
        else:
            return post_json(data='注册用户名已经存在，换一个用户名试试')
    else:
        return render_template('404.html')

# -------------------------信息查询接口----------------------------
# 园区概况接口
@app.route('/area_overview', methods=['GET', 'POST'])
def area_overview():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys():
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        if user is not None:
            return post_json(0, 'success', check_info.get_area_overview())
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8290, debug=True)
    app.run(debug=True)