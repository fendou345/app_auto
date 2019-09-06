# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

import unittest
from ddt import ddt, data, unpack
from business.startPatient import StartPatient
from elementutil.personalCenter.login import Login
from common.parseData import getCsvData

@ddt
class TestLogin(unittest.TestCase, Login):
    def setUp(self):
        StartPatient.__init__(self)

    #登录校验测试
    # @unittest.skip('测试')
    @data(*getCsvData('../../testdata/login/login.csv'))
    @unpack
    def test_login1(self, username, password, expectresult):
        Login.click_jump_button(self)
        Login.click_personnal_button(self)
        Login.type_username(self, username)
        Login.type_password(self, password)
        Login.click_login_button(self)
        self.assertEqual(Login.get_login_toast(self), expectresult)

    def tearDown(self):
        self.pat.close()

if __name__ == '__main__':
    unittest.main()