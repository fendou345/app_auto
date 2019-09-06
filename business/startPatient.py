# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

from appium import webdriver
from utils import conf_args
from common.operateElement import OperateElement
import time

class StartPatient():
    def __init__(self):
        """
        类初始化函数
        """
        plantform_dict = self.init_platform_args()
        self.pat_driver = self.init_driver(plantform_dict)
        self.pat = OperateElement(self.pat_driver)

    @staticmethod
    def init_platform_args():
        """
        初始化: 获取 测试平台 参数
        :return: 参数字典 plantform_config
        """
        platform_sec_ops = {
            'testplatform1':
                [
                    'platform_name',
                    'platform_version',
                    'device_name',
                    'app_package',
                    'app_activity'
                ]
        }
        platform_config = conf_args.ConfigArgs('../conf/plantforms_conf.ini', platform_sec_ops)
        platform_config.initialize()
        return platform_config.config_dict

    @staticmethod
    def init_driver(plantform_dict):
        """
        初始化 webdriver
        :return: driver
        """
        desired_caps = dict()
        #desired_caps['automationName'] = 'uiautomator2'
        desired_caps['platformName'] = plantform_dict.get('platform_name')
        desired_caps['platformVersion'] = plantform_dict.get('platform_version')
        desired_caps['deviceName'] = plantform_dict.get('device_name')
        desired_caps['appPackage'] = plantform_dict.get('app_package')
        desired_caps['appActivity'] = plantform_dict.get('app_activity')
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['newCommandTimeout'] = 600
        desired_caps['automationName'] = 'uiautomator2'
        print(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(3)
        return driver


# if __name__ == '__main__':
#     StartPatient.__init__()