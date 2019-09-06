# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

import unittest
from ddt import ddt, data, unpack
from business.startPatient import StartPatient
from elementutil.videoDiagnose.book import Book
from common.variable import GetVariable as gv
from business.loginPatient import LoginPatient


class TestBook(unittest.TestCase, Book, LoginPatient):
    def setUp(self):
        StartPatient.__init__(self)
        LoginPatient.login_patient(self)

    #待付款
    def test_book(self):
        Book.click_book(self)
        Book.click_book_online(self)
        Book.click_x(self)
        Book.click_dept(self)
        Book.click_doctor(self)
        Book.swip_up_1000(self)
        Book.click_order_no(self)
        Book.click_immediate_order(self)
        Book.click_confirm_order(self)
        Book.click_cancel_pay(self)
        Book.click_confirm_cancel_pay(self)
        self.assertIn(gv.dai_fu_kuan, Book.get_dai_fu_kuan_text(self))

    def tearDown(self):
        self.pat.close()

if __name__ == '__main__':
    unittest.main()


