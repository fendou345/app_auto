# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

import unittest
import time
from ddt import ddt, data, unpack
from common.generateRandom import GenerateRandom as gr
from business.startPatient import StartPatient
from elementutil.personalCenter.register import Register
from common.parseData import getCsvData
from common.variable import GetVariable as gv
from common.operateDB import get_verification_code

@ddt
class TestRegister(unittest.TestCase, Register):
    def setUp(self):
        StartPatient.__init__(self)

    #用户名校验测试
    # @unittest.skip('测试')
    @data(*getCsvData('../testdata/register/username.csv'))
    @unpack
    def test_register1(self, username, expectresult):
        Register.click_jump_button(self)
        Register.click_personnal_button(self)
        Register.click_register_button(self)
        Register.click_usernameregister_button(self)
        Register.type_username(self, username)
        Register.click_next_button(self)
        self.assertEqual(Register.get_username_toast(self), expectresult)

    #密码校验测试
    # @unittest.skip('测试')
    @data(*getCsvData('../testdata/register/password.csv'))
    @unpack
    def test_register2(self, password, confirmpassword, expectresult):
        Register.click_jump_button(self)
        Register.click_personnal_button(self)
        Register.click_register_button(self)
        Register.click_usernameregister_button(self)
        Register.type_username(self, gr.string_random(7, ascii=True))
        Register.click_next_button(self)
        Register.type_password(self, password)
        Register.type_confirm_password(self, confirmpassword)
        Register.click_next_button(self)
        self.assertEqual(Register.get_password_toast(self), expectresult)

    #密保手机校验
    # @unittest.skip('测试')
    @data(*getCsvData('../testdata/register/phone.csv'))
    @unpack
    def test_register3(self, phone, expectresult):
        Register.click_jump_button(self)
        Register.click_personnal_button(self)
        Register.click_register_button(self)
        Register.click_usernameregister_button(self)
        Register.type_username(self, gr.string_random(7, ascii=True))
        Register.click_next_button(self)
        Register.type_password(self, gv.password)
        Register.type_confirm_password(self, gv.password)
        Register.click_next_button(self)
        Register.type_secret_phone(self, phone)
        Register.click_verification_code_button(self)
        self.assertEqual(Register.get_phone_toast(self), expectresult)

    #验证码校验（错误）
    # @unittest.skip('测试')
    def test_register4(self):
        Register.click_jump_button(self)
        Register.click_personnal_button(self)
        Register.click_register_button(self)
        Register.click_usernameregister_button(self)
        Register.type_username(self, gr.string_random(7, ascii=True))
        Register.click_next_button(self)
        Register.type_password(self, gv.password)
        Register.type_confirm_password(self, gv.password)
        Register.click_next_button(self)
        Register.type_secret_phone(self, gv.secretPhone)
        Register.click_verification_code_button(self)
        Register.type_input_code(self, gv.verificationCode)
        Register.click_complete_button(self)
        self.assertEqual(Register.get_password_toast(self), gv.codeErrorText)

    # 验证码校验（过期）
    @unittest.skip('测试')
    def test_register5(self):
        Register.click_jump_button(self)
        Register.click_personnal_button(self)
        Register.click_register_button(self)
        Register.click_usernameregister_button(self)
        Register.type_username(self, gr.string_random(7, ascii=True))
        Register.click_next_button(self)
        Register.type_password(self, gv.password)
        Register.type_confirm_password(self, gv.password)
        Register.click_next_button(self)
        Register.type_secret_phone(self, gv.secretPhone)
        Register.click_verification_code_button(self)
        time.sleep(5)
        Register.type_input_code(self, get_verification_code())
        time.sleep(300)
        Register.click_complete_button(self)
        self.assertEqual(Register.get_password_toast(self), gv.codeOverText)

    # 注册成功
    def test_register6(self):
        Register.click_jump_button(self)
        Register.click_personnal_button(self)
        Register.click_register_button(self)
        Register.click_usernameregister_button(self)
        Register.type_username(self, gr.string_random(7, ascii=True))
        Register.click_next_button(self)
        Register.type_password(self, gv.password)
        Register.type_confirm_password(self, gv.password)
        Register.click_next_button(self)
        Register.type_secret_phone(self, gv.secretPhone)
        Register.click_verification_code_button(self)
        time.sleep(5)
        Register.type_input_code(self, get_verification_code())
        Register.click_complete_button(self)
        time.sleep(2)
        self.assertEqual(Register.get_success_text(self), gv.registerSuccess)


    def tearDown(self):
        self.pat.close()

if __name__ == '__main__':
    unittest.main()
