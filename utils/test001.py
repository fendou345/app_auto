# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

# import xlrd
#
# data = xlrd.open_workbook('e:\data\\test.xlsx')
# sheets = data.sheet_names()
# all_case = []
# for i in range(len(sheets)):
#     sheet = sheets[i]
#     table = data.sheet_by_name(sheet)
#     nrows = table.nrows
#     for j in range(1, nrows):
#         all_case.append({"id":table.cell_value(j, 0), "casename":table.cell_value(j, 1)})
# print(all_case)
# import os
# def get_excel():
#     filenames = os.listdir("E:\\06.需求\\01.患者端测试用例")
#     for filename in filenames:
#         print(filename)
# get_excel()
# import os
# path = os.path.join(os.path.dirname(os.getcwd()), 'test_case_data')
# path1 = os.getcwd()
# print(path)
# print(path1)

import requests
import json
# url = 'http://192.168.1.131:9101/pat/v1/personalcenter/patientuser/login-by-password'
# header = '{"Content-Type": "application/json"}'
# para = '{"loginType": 2, "password": "123456xy", "usernameOrPhone": "lxx345"}'
#
# headers = json.loads(header)
#
# reponse = requests.post(url=url, data=para, headers=headers)
# print(reponse.text)
# paylod = {"wd": "Python接口测试"}
# r = requests.get('http://www.baidu.com')
# # print(r.status_code)
# # # print(r.url)
# # print(r.text)
# print(r)
# payload = {'key': 'value1', 'key2': 'value2'}
# r = requests.post('http://httpbin.org/post', data=json.dumps(payload))
# print(r.status_code)
# print(r.text)
# print(r.json())

# r = requests.get('https://www.zhihu.com/', verify=False)
# print(r.status_code)
# print(r.text)


# import unittest
# print(help(unittest))

# f = open('f:\\burpsuite\\sql.txt', 'r')
# print(f.read(10))
# f.close()

# with open('f:\\burpsuite\\sql.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# import os
# print(os.environ.get('PATH'))

# import os
# # 查看当前目录的绝对路径
# print(os.path.abspath('.'))
# # 把两个路径合成一个
# print(os.path.join('f:\\Python_work\\app_auto\\utils', 'test'))
# #拆分路径时
# print(os.path.split('f:\\Python_work\\app_auto\\utils\\test001.py'))
# #得到文件扩展名
# print(os.path.splitext('f:\\Python_work\\app_auto\\utils\\test001.py'))
# #列出当前目录下的所有目录
# print([x for x in os.listdir('.') if os.path.isdir(x)])


# import os
# print('Process (%s) start...' % os.getppid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


from multiprocessing import Process
import os


# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# from multiprocessing import Process,Queue
# import os,time,random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()



