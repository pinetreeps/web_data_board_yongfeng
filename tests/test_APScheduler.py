# _*_ coding:utf-8 _*_
# Filename: test_APScheduler.py
# Author: pang song
# python 3.6
# Date: 2019/01/17
'''
测试定时任务 扩展包 APScheduler
'''

from flask import Flask, request
from flask_apscheduler import APScheduler


class Config(object):  # 创建配置，用类
    JOBS = [  # 任务列表
        # {  # 第一个任务
        #     'id': 'job1',
        #     'func': '__main__:job_1',
        #     'args': (1, 2),
        #     'trigger': 'cron',
        #     'hour': 19,
        #     'minute': 27
        # },
        {  # 第二个任务，每隔5秒执行一次
            'id': 'job2',
            'func': '__main__:job_1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 5,
        }
    ]

# 任务函数
def job_1(a, b):
    print('hello',a + b)


app = Flask(__name__)
app.config.from_object(Config())  # 为实例化的flask引入配置


##
@app.route("/hello", methods=["POST", "GET"])
def check():
    return "success", 200


if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=False)
