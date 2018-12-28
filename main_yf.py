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

# -------------------------3.1、项目概况模块----------------------------
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

# 建筑概况接口
# http://.../building_overview
@app.route('/building_overview', methods=['GET', 'POST'])
def building_overview():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'building_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_building_overview())
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# -------------------------3.2、环境信息模块----------------------------
# 3.2.1室外环境 实时（物联网）
# http://.../env_outdoor
@app.route('/env_outdoor', methods=['GET', 'POST'])
def env_outdoor():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_env_outdoor())
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 3.2.2室外环境 历史数据（物联网）
# http://.../env_outdoor_history
@app.route('/env_outdoor_history', methods=['GET', 'POST'])
def env_outdoor_history():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'data_type' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.env_outdoor_history(data.get('data_type')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 3.2.3室内环境 实时（物联网）
# http://.../env_indoor
@app.route('/env_indoor', methods=['GET', 'POST'])
def env_indoor():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'position_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_env_indoor(data.get('position_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 3.2.4室内环境 历史（物联网）
# http://.../env_indoor_history
@app.route('/env_indoor_history', methods=['GET', 'POST'])
def env_indoor_history():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'position_id' in data.keys() and 'data_type' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.env_indoor_history(data.get('position_id'), data.get('data_type')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# -------------------------3.3、用能信息模块----------------------------
# 3.3.1用能总览
# http://.../energy_overview
@app.route('/energy_overview', methods=['GET', 'POST'])
def energy_overview():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_energy_overview(check_id))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')


# 3.3.2园区、建筑用电情况（物联网）
# http://.../energy_electricity_overview
@app.route('/energy_electricity_overview', methods=['GET', 'POST'])
def energy_electricity_overview():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_energy_electricity_overview(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 3.3.3设备用电情况（物联网）
# http://.../energy_electricity
@app.route('/energy_electricity', methods=['GET', 'POST'])
def energy_electricity():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_energy_electricity(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 3.3.4用气情况（燃气公司或手动输入）
# http://.../energy_gas
@app.route('/energy_gas', methods=['GET', 'POST'])
def energy_gas():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_energy_gas(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 3.3.5用水情况（物联网）
# http://.../energy_water_overview
@app.route('/energy_water_overview', methods=['GET', 'POST'])
def energy_water_overview():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_energy_water_overview(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')


# 3.3.6用热情况（物联网）
# http://.../energy_check_hot
@app.route('/energy_check_hot', methods=['GET', 'POST'])
def energy_check_hot():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return '输入参数不完整或者不正确'
        else:
            return '输入参数不完整或者不正确'
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_energy_check_hot(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8290, debug=True)
    # app.run(debug=True)