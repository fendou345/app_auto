# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

from common.operateElement import OperateElement
from business.startPatient import StartPatient

class Login(StartPatient):
    jump = 'android_uiautomator=>text:跳过'
    personnalButton = 'android_uiautomator=>text:个人中心'
    username = 'android_uiautomator=>className:android.widget.EditText&&instance:0'
    password = 'android_uiautomator=>className:android.widget.EditText&&instance:1'
    loginButton = 'android_uiautomator=>text:立即登录'
    loginToast = 'android_uiautomator=>className:android.widget.TextView&&instance:12'

    def click_jump_button(self):
        self.pat.click(self.jump)

    def click_personnal_button(self):
        self.pat.click(self.personnalButton)

    def type_username(self, username):
        self.pat.type(self.username, username)

    def type_password(self, password):
        self.pat.type(self.password, password)

    def click_login_button(self):
        self.pat.click(self.loginButton)

    def get_login_toast(self):
        return self.pat.get_text(self.loginToast)