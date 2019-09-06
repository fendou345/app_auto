# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

import os
import unittest
import time
import HTMLTestRunner
from testcase.testVideo.testBook import TestBook
from common.sendEmail import SendEmail

#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.'))+'/report/'

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

#设置报告名称格式
html_file = report_path+now+'HTMLtemplate.html'
fp = open(html_file, 'wb')


#每次加载一个测试用例到测试套件中
# suite=unittest.TestSuite()
# suite.addTest(TestRegister('test_register'))

#一次性加载一个类文件下所有测试用例到suite中去
suite = unittest.TestSuite(unittest.makeSuite(TestBook))

#加载一个路径下所有的测试用例
# listcasedir = os.path.dirname(os.path.abspath('.'))+'/manage_web/'
# suite=unittest.TestLoader().discover(listcasedir, pattern ='test*.py', top_level_dir = None)

if __name__=='__main__':
    #初始化一个HTMLTestRunnner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='患者端 测试报告', description='用例测试情况')
    runner.run(suite)
    fp.close()
    SendEmail(report_path).send_email()
