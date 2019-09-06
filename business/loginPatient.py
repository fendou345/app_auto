# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

from business.startPatient import StartPatient
from elementutil.personalCenter.login import Login
from common.variable import GetVariable as gv

class LoginPatient(Login):

    def login_patient(self):
        Login.click_jump_button(self)
        Login.click_personnal_button(self)
        Login.type_username(self, gv.username)
        Login.type_password(self, gv.password)
        Login.click_login_button(self)


# if __name__ == '__main__':
#     LoginPatient.login_patient(self=LoginPatient)
