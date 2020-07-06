import unittest
from com import NingBo
import HTMLTestRunner
import os

me = NingBo.NingBo('chenyuwen', 'wen960803')

class NingBoTestCase(unittest.TestCase):


    def setUp(self) -> None:
        print('用例开始执行')
        #me.login()

    def tearDown(self) -> None:
        print('用例结束')
        #me.logout()
        #me.quitDriver()
    #登录并到位登记
    def test_01(self):
        me.login()
        me.startX()
        me.daoW1()
        print('第一条用例')

    #提交缺陷
    def test_02(self):
        me.sM()
        print('第二条用例')

    #危险点处理
    def test_03(self):
        me.danger()
        me.endX()
        print('第三条用例')

    #开启保电
    def test_04(self):
        me.startProPlan()
        me.sM()
        me.danger()
        me.tongD()
        me.endPro()
        print('第四条用例')

    #开启检修计划
    def test_05(self):
        me.startJianX()
        me.sM()
        me.danger()
        me.endJianX()
        print('第五条用例')

    #其他到位
    def test_06(self):
        me.daoW()
        print('第六条用例')






if __name__ == '__main__':
    unittest.main()
