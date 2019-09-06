# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

from common.operateElement import OperateElement
from business.startPatient import StartPatient

class Register(StartPatient):

    jump = 'android_uiautomator=>text:跳过'
    personnalButton = 'android_uiautomator=>text:个人中心'
    registerButton = 'android_uiautomator=>text:注册账号'
    usernameRegister = 'android_uiautomator=>text:用户名注册'
    setUsername = 'android_uiautomator=>className:android.widget.EditText&&instance:0'
    nextButton = 'android_uiautomator=>text:下一步'
    setPassword = 'android_uiautomator=>className:android.widget.EditText&&instance:0'
    confirmPassword = 'android_uiautomator=>className:android.widget.EditText&&instance:1'
    secretPhone = 'android_uiautomator=>className:android.widget.EditText&&instance:0'
    verificationCode = 'android_uiautomator=>text:获取验证码'
    inputCode = 'android_uiautomator=>text:请输入验证码'
    completeBotton = 'android_uiautomator=>text:完成'
    usernameTosat = 'android_uiautomator=>className:android.widget.TextView&&instance:7'
    #验证码提示一样
    passwordTosat = 'android_uiautomator=>className:android.widget.TextView&&instance:6'
    phoneTosat = 'android_uiautomator=>className:android.widget.TextView&&instance:5'
    registerSuccess = 'android_uiautomator=>className:android.widget.TextView&&instance:0'

    def click_jump_button(self):
        self.pat.click(self.jump)

    def click_personnal_button(self):
        self.pat.click(self.personnalButton)

    def click_register_button(self):
        self.pat.click(self.registerButton)

    def click_usernameregister_button(self):
        self.pat.click(self.usernameRegister)

    def type_username(self, username):
        self.pat.type(self.setUsername, username)

    def type_password(self, password):
        self.pat.type(self.setPassword, password)

    def click_next_button(self):
        self.pat.click(self.nextButton)

    def type_confirm_password(self, password):
        self.pat.type(self.confirmPassword, password)

    def type_secret_phone(self, phone):
        self.pat.type(self.secretPhone, phone)

    def click_verification_code_button(self):
        self.pat.click(self.verificationCode)

    def type_input_code(self, code):
        self.pat.type(self.inputCode, code)

    def click_complete_button(self):
        self.pat.click(self.completeBotton)

    def get_username_toast(self):
        return self.pat.get_text(self.usernameTosat)

    def get_password_toast(self):
        return self.pat.get_text(self.passwordTosat)

    def get_phone_toast(self):
        return self.pat.get_text(self.phoneTosat)

    def get_success_text(self):
        return self.pat.get_text(self.registerSuccess)



