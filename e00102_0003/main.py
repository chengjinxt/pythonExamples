import time
import os
import sys
# 获取相对文件路径方法
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

with open(os.path.join(BASE_DIR, 'data.txt'), mode='r', encoding='utf-8') as f:
    data = f.read().strip()
print(data)

time.sleep(3)
input("Press any key to exit...")