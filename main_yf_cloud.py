# _*_ coding:utf-8 _*_
# Filename: main_yf.py
# Author: pang song
# python 3.6
# Date: 2018/11/05
'''
适用于阿里云部署版本，未连接物联网数据库
'''

import sys
try:
    reload(sys)  # Python2.5 初始化后删除了 sys.setdefaultencoding 方法，我们需要重新载入
    sys.setdefaultencoding('utf-8')
except:
    pass

from flask import Flask, request, render_template
import json
from auth import user_dal
# from auth import user_dal
from utils.is_json import is_json
from utils.post_json import post_json
import config
from get_info import check_info, check_info_wlw, check_security

from flask_bootstrap import Bootstrap
from flask_cors import CORS

app = Flask(__name__)
bootstrap = Bootstrap(app)
# 解决跨域问题
CORS(app, supports_credentials=True)

import logging
# -----------日志配置------------
# 格式化日志配置，输出日志到文件
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("main")
hdr = logging.FileHandler(config.LOGGING_FILE)

# 日志格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(name)s %(funcName)s: %(message)s','%Y-%m-%d %H:%M:%S')
hdr.setFormatter(formatter)
logger.addHandler(hdr)

# 输出到终端
hdr_s = logging.StreamHandler()
hdr_s.setFormatter(formatter)
logger.addHandler(hdr_s)


# -------------------------测试接口----------------------------
@app.route('/')
def hello_world():
    return '<h1>Hello World! yong feng!</h1>'


# -------------------------登录注册接口----------------------------
# 登陆接口
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uname' in data.keys() and 'password' in data.keys():
                user = user_dal.UserDal().login_auth(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys() and 'uname' in data.keys():
                success = True
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uname' in data.keys() and 'password' in data.keys() and 'nickname' in data.keys() \
                    and 'apply_code' in data.keys():
                if data.get('apply_code') == config.APPLY_CODE:
                    success = user_dal.UserDal().register(data)
                else:
                    return post_json(2, 'success', data='邀请码不正确')
            else:
                return post_json(1, 'failed', data='输入参数不完整或者不正确')
        else:
            return post_json(1, 'failed', data='输入参数不完整或者不正确')
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
            logger.debug(data)
            if 'uname' in data.keys():
                success = user_dal.UserDal().register_name_check(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')

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
            logger.debug(data)
            if 'uid' in data.keys():
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys() and 'building_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            # 查询物联网接口数据
            # logger.debug(post_json(0, 'success', check_info.get_env_outdoor()))
            # return check_info_wlw.get_info_wlw(config.URL_WLW + '/env_outdoor', request.get_data())

            # 查询虚拟数据
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
            logger.debug(data)
            if 'uid' in data.keys() and 'data_type' in data.keys() and data.get('data_type') in ("year", "month", "day"):
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys() and 'position_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys() and 'position_id' in data.keys() and 'data_type' in data.keys()  and data.get('data_type') in ("year", "month", "day"):
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_energy_overview(data.get('check_id')))
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
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
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
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_energy_check_hot(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')


# -------------------------4.监控通用接口----------------------------
# 4.1监控通用接口_空调（物联网）
# http://.../monitor_check_ac

@app.route('/monitor_check_ac', methods=['GET', 'POST'])
def monitor_check_ac():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_device_ac_data(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')


# 4.2监控通用接口_电器（物联网）
# http://.../monitor_check_ea

@app.route('/monitor_check_ea', methods=['GET', 'POST'])
def monitor_check_ea():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_device_ea_data(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')


# 4.3.1安防摄像头（摄像头供应商）
# http://.../security_camera

@app.route('/security_camera', methods=['GET', 'POST'])
def security_camera():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_security_camera_data(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 4.3.2安防设备（物联网）
# 例如红外报警器、门禁等
# http://.../security_device

@app.route('/security_device', methods=['GET', 'POST'])
def security_device():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_security_device_data(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')


# 4.4 消防设备信息（物联网）
# http://.../fire_equipment

@app.route('/fire_equipment', methods=['GET', 'POST'])
def fire_equipment():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.get_fire_equipment_data(data.get('check_id')))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')


# -------------------------5.管理接口----------------------------
# 5.1 用户管理
# http://.../config_user

@app.route('/config_user', methods=['GET', 'POST'])
def config_user():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.update_user_data(data))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 5.2.1园区信息配置
# http://.../config_area

@app.route('/config_area', methods=['GET', 'POST'])
def config_area():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.update_area_data(data))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 5.2.2建筑信息配置
# http://.../config_building

@app.route('/config_building', methods=['GET', 'POST'])
def config_building():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.update_building_data(data))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 5.2.3房间信息配置
# http://.../config_room

@app.route('/config_room', methods=['GET', 'POST'])
def config_room():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.update_room_data(data))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 5.2.4物业信息管理
# http://.../config_property

@app.route('/config_property', methods=['GET', 'POST'])
def config_property():
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'check_id' in data.keys():
                # 检查uid
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
        # 获取数据
        if user is not None:
            return post_json(0, 'success', check_info.update_property_data(data))
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# -------------------------6.安防信息接口----------------------------
# 6.1 接收物联网安防信息接口，保存到数据库
# http://.../security_bim

@app.route('/security_bim', methods=['GET', 'POST'])
def security_bim():
    logger.info('/security_bim')
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            # 检测规定参数是否存在
            if 'security_time' in data.keys() and 'device_id' in data.keys():
                # 存入数据库
                check_security.save_security_msg(data)
                return post_json(0, 'success')
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
    else:
        return render_template('404.html')

# 6.2 从数据库读取安防信息
# http://.../security_msg

@app.route('/security_msg', methods=['GET', 'POST'])
def security_msg():
    logger.info('/security_msg')
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys():
                # 检测规定参数是否存在
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
            # 获取数据
        if user is not None:
            return post_json(0, 'success', check_security.get_security_msg())
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')

# 6.3 更新数据库安防信息状态
# http://.../security_msg_update

@app.route('/security_msg_update', methods=['GET', 'POST'])
def security_msg_update():
    logger.info('/security_msg_update')
    if request.method == 'GET':
        return '<h1>请使用post方法</h1>'
    elif request.method == 'POST':
        # 参数校验
        if is_json(request.get_data()):
            data = json.loads(request.get_data())
            logger.debug(data)
            if 'uid' in data.keys() and 'security_id' in data.keys() and 'security_update_code' in data.keys():
                # 检测规定参数是否存在
                user = user_dal.UserDal().check_uid(data)
            else:
                return post_json(data='输入参数不完整或者不正确')
        else:
            return post_json(data='json校验失败')
            # 获取数据
        if user is not None:
            success_label = check_security.update_security_msg(data)
            if success_label:
                return post_json(0, 'success')
            else:
                return post_json(data='update failed')
        else:
            return post_json(data='uid校验失败')
    else:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8290, debug=True)
    # app.run(debug=True)