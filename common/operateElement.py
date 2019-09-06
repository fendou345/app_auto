# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

import selenium
from appium import webdriver
import appium
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from common.variable import GetVariable as gv
from utils import log
import logging

log.init_log("../../logs/patient_app")

class OperateElement():
    def __init__(self, driver):
        self.driver = driver
    def find_element(self, selector, *args):
        """
        定位元素方法(用=>切割额字符串),args为空，为单元素定位；
        args不为空，为定位元素组，且args[0]的值为index
        :param selector:
        :param args:
        :return:
        """
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if args:
            index = args[0]
            if selector_by == 'android_uiautomator':
                if '&&' in selector_value:
                    selector_child1_by = selector_value.split('&&')[0].split(':')[0]
                    selector_child1_value = selector_value.split('&&')[0].split(':')[1]
                    selector_child2_by = selector_value.split('&&')[1].split(':')[0]
                    selector_child2_value = selector_value.split('&&')[1].split(':')[1]
                    try:
                        element = WebDriverWait(self.driver, gv.WAIT_TIME).until(lambda x:
                            self.driver.find_elements_by_android_uiautomator(
                'new UiSelector().%s(%s).%s(%s)' % (selector_child1_by, selector_child1_value, selector_child2_by, selector_child2_value))[index])
                        return element
                    except selenium.common.exceptions.TimeoutException:
                        return False
                    except selenium.common.exceptions.NoSuchElementException:
                        logging.info("找不到数据")
                        return False

                else:
                    selector_child_by = selector_value.split(':')[0]
                    selector_child_value = selector_value.split(':')[1]
                    try:
                        element = WebDriverWait(self.driver, gv.WAIT_TIME).until(lambda x:
                            self.driver.find_elements_by_android_uiautomator('new UiSelector().%s(\"%s\")' % (selector_child_by, selector_child_value))[index])
                        # element = self.driver.find_element_by_android_uiautomator(
                        #     'new UiSelector().%s(\"%s\")' % (selector_child_by, selector_child_value))
                        return element
                    except selenium.common.exceptions.TimeoutException:
                        return False
                    except selenium.common.exceptions.NoSuchElementException:
                        logging.info("找不到数据")
                        return False
            elif selector_by == 'xpath':
                try:
                    element = WebDriverWait(self.driver, gv.WAIT_TIME).until(lambda x: self.driver.find_elements_by_xpath(selector_value)[index])
                    return element
                except selenium.common.exceptions.TimeoutException:
                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    logging.info("找不到数据")
                    return False

        else:
            if selector_by == 'android_uiautomator':
                if '&&' in selector_value:
                    selector_child1_by = selector_value.split('&&')[0].split(':')[0]
                    selector_child1_value = selector_value.split('&&')[0].split(':')[1]
                    selector_child2_by = selector_value.split('&&')[1].split(':')[0]
                    selector_child2_value = selector_value.split('&&')[1].split(':')[1]
                    try:
                        element = WebDriverWait(self.driver, gv.WAIT_TIME).until(lambda x:
                            self.driver.find_element_by_android_uiautomator(
                'new UiSelector().%s(%s).%s(%s)' % (selector_child1_by, selector_child1_value, selector_child2_by, selector_child2_value)))
                        return element
                    except selenium.common.exceptions.TimeoutException:
                        return False
                    except selenium.common.exceptions.NoSuchElementException:
                        logging.info("找不到数据")
                        return False

                else:
                    selector_child_by = selector_value.split(':')[0]
                    selector_child_value = selector_value.split(':')[1]
                    try:
                        element = WebDriverWait(self.driver, gv.WAIT_TIME).until(lambda x:
                            self.driver.find_element_by_android_uiautomator('new UiSelector().%s(\"%s\")' % (selector_child_by, selector_child_value)))
                        # element = self.driver.find_element_by_android_uiautomator(
                        #     'new UiSelector().%s(\"%s\")' % (selector_child_by, selector_child_value))
                        return element
                    except selenium.common.exceptions.TimeoutException:
                        return False
                    except selenium.common.exceptions.NoSuchElementException:
                        logging.info("找不到数据")
                        return False
            elif selector_by == 'xpath':
                try:
                    element = WebDriverWait(self.driver, gv.WAIT_TIME).until(self.driver.find_element_by_xpath(selector_value))
                    return element
                except selenium.common.exceptions.TimeoutException:
                    return False
                except selenium.common.exceptions.NoSuchElementException:
                    logging.info("找不到数据")
                    return False
    def clear(self, selector, *args):
        """
        清除文本框
        :param self:
        :param selector:
        :param args:
        :return:
        """
        el = self.find_element(selector, *args)
        try:
            el.clear()
        except NameError as e:
            self.get_img()

    def click(self, selector, *args):
        """
        点击元素
        :param selector:
        :return:
        """
        el = self.find_element(selector, *args)
        try:
            el.click()
            logging.info('The element \'%s\' was clicked' % el)
        except NameError as e:
            logging.error('Failed to click the element with %s' % e)

    def type(self, selector, text, *args):
        """
        输入
        :param selector:
        :param text:
        :return:
        """
        el = self.find_element(selector, *args)
        el.clear()
        try:
            el.send_keys(text)
            logging.info('Had type \'%s\' in inputbox' % text)
        except NameError as e:
            logging.error('Failed to type in inputbox with %s' % e)
            self.get_img()

    def get_text(self, selector, *args):
        """
        获取element text
        :return:el.text
        """
        el = self.find_element(selector, *args)
        logging.info('获取\'%s\'的text,text为\'%s\'' % (el, el.text))
        return el.text

    def is_display(self, selector, *args):
        """
        是否展示
        :param selector:
        :return:
        """
        el = self.find_element(selector, *args)
        try:
            el.is_displayed()
            logging.info('The element was displayed')
            return el.is_displayed()
        except NameError as e:
            pass
            logging.error('Failed to displayed the element  %s' % e)

    def camera(self):
        """
        拍照键
        :return:
        """
        self.driver.press_keycode(27)
        logging.info("开始拍照")

    def get_img(self):
        """
        保存图片
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info("Had taken screenshot and save tp folder:/screenshots")
        except NameError as e:
            logging.error("Failed to take screenshot! %s" % e)
            self.get_img()

    def close(self):
        """
        关闭APP
        :return:
        """
        self.driver.close_app()
        logging.info("APP关闭")

    def back(self):
        """
        点击返回键
        :return:
        """
        self.driver.press_keycode(4)
        logging.info("Click back on current page")

    def get_size(self):
        """
        获得机器屏幕大小x,y
        :return:
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_up(self, t):
        """
        屏幕向上滑动,t表示时间，ms
        :param t:
        :return:
        """
        l= self.get_size()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t, *args):
        """
        屏幕向下滑动
        :param t:
        :return:
        """
        l = self.get_size()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    def swip_left(self, t, *args):
        """
        屏幕向左滑动
        :param t:
        :return:
        """
        l = self.get_size()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    def swip_right(self, t, *args):
        """
        屏幕向右滑动
        :param t:
        :return:
        """
        l = self.get_size()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)
