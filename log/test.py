# _*_ coding:utf-8 _*_
# Filename: .py
# Author: pang song
# python 3.6
# Date: 2019/

import random


VOC_LEVEL = {'0':'良好', '1':'轻污染', '2':'中污染', '3':'重污染'}


print(str(random.randint(0, 3)))
print(VOC_LEVEL.get(str(random.randint(0, 3))))


