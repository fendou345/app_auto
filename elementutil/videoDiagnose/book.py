# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

from common.operateElement import OperateElement
from business.startPatient import StartPatient

class Book(StartPatient):
    book = 'android_uiautomator=>text:预约挂号'
    bookOnline = 'android_uiautomator=>text:视频问诊'
    xButton = 'android_uiautomator=>text:X'
    dept = 'android_uiautomator=>text:心血管内科门诊'
    doctor = 'android_uiautomator=>text:李纪鸾'
    orderno = 'android_uiautomator=>text:预约'
    immediateOrder = 'android_uiautomator=>text:立即预约'
    confirmOrder = 'android_uiautomator=>className:android.widget.TextView&&instance:23'
    confirmOrderToast = 'android_uiautomator=>className:android.widget.TextView&&instance:0'
    cardPay = 'android_uiautomator=>className:android.widget.ImageView&&instance:11'
    immediatePay = 'android_uiautomator=>text:立即支付'
    cancelPay = 'android_uiautomator=>text:取消支付'
    confirm_cancel_pay = 'android_uiautomator=>text:确定'
    confirmPay= 'android_uiautomator=>text:确定支付'
    confirmPayToast= 'android_uiautomator=>text:我知道了'
    dai_jiu_zhen_text = 'android_uiautomator=>className:android.widget.TextView&&instance:0'
    cancelOrder = 'android_uiautomator=>text:取消预约'
    dai_fu_kuan_text = 'android_uiautomator=>className:android.widget.TextView&&instance:5'


    def click_book(self):
        self.pat.click(self.book)

    def click_book_online(self):
        self.pat.click(self.bookOnline)

    def click_x(self):
        self.pat.click(self.xButton)

    def click_dept(self):
        self.pat.click(self.dept)

    def click_doctor(self):
        self.pat.click(self.doctor)

    def click_order_no(self):
        self.pat.click(self.orderno, -1)

    def click_immediate_order(self):
        self.pat.click(self.immediateOrder)

    def click_confirm_order(self):
        self.pat.click(self.confirmOrder)

    def get_confirm_order_toast(self):
        return self.pat.get_text(self.confirmOrderToast)

    def click_card_pay(self):
        self.pat.click(self.cardPay)

    def click_immediate_pay(self):
        self.pat.click(self.immediatePay)

    def click_cancel_pay(self):
        self.pat.click(self.cancelPay)

    def click_confirm_cancel_pay(self):
        self.pat.click(self.confirm_cancel_pay)

    def click_confirm_pay(self):
        self.pat.click(self.confirmPay)

    def click_confirm_pay_toast(self):
        self.pat.click(self.confirmPayToast)

    def click_cancel_order(self):
        self.pat.click(self.cancelOrder)

    def get_dai_jiu_zhen_text(self):
        return self.pat.get_text(self.dai_jiu_zhen_text)

    def get_dai_fu_kuan_text(self):
        return self.pat.get_text(self.dai_fu_kuan_text)

    def swip_up_1000(self):
        self.pat.swipe_up(1000)




