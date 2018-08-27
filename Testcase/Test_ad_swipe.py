#coding=utf-8
__author__='wg'
import unittest
from PO import DashPage

class XX(unittest.TestCase):

    def setUp(self):
        pass

    def test_Search(self):
        DashPage.Dash.__init__(DashPage.driver)


    def tearDown(self):
        pass

if __name__ == '__main__':
    pass