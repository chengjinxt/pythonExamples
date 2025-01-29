import time
import os
import sys

# 传统调用方法 这种可以正常打包进去 
from utils import pinyin

#动态调用
import importlib

# 获取相对文件路径方法
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#方法一
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

#方法二
"""
if getattr(sys,'frozen',False):
    BASE_DIR =os.path.dirname(sys.executable)
else:
    BASE_DIR =os.path.dirname(os.path.abspath(__file__))
"""

"""
with open(os.path.join(BASE_DIR, 'data.txt'), mode='r', encoding='utf-8') as f:
    data = f.read().strip()
print(data)
"""

# 调用模块方法一 pyinstaller -F main.py -n main
print(pinyin.get_pinyinCount())

# 动态调用模块方法二
# 打包后报错  ModuleNotFoundError: No module named 'utils.ipa'
"""
修改   main.spec文件 在Analysis里添加如下内容
 hiddenimports=[
        "utils.ipa" 
    ],
再运行如下打包命令
pyinstaller main.spec
注意这里要指定spec文件
"""
ipa = importlib.import_module('utils.ipa')
print(ipa.get_ipaCount())



time.sleep(3)
input("Press any key to exit...")