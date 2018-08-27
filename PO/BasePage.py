#coding=utf-8
__author__='wg'
from appium import webdriver
import time

class Base:
    driver = None
    # # 一加五
    # capabilities = {"platformName": "Android",
    #                 "platformVersion": "8.1.0",
    #                 "deviceName": "f015db0b",
    #                 "appPackage": "com.unicom.wopay",
    #                 "appActivity": "modules.main.ui.WelcomeActivity",
    #                 "app": "C:\\Users\\Administrator\\Desktop\\新建文件夹\\沃钱包\\wopay-4.1.1-jgjc-07311454.apk",
    #                 # "unicodeKeyboard":True,
    #                 # "resetKeyboard":True}
    #                 }



    # 小米5
    capabilities = {"platformName": "Android",
                    "platformVersion": "8.0",
                    "deviceName": "d81ef4be",
                    "appPackage": "com.unicom.wopay",
                    "appActivity": "modules.main.ui.WelcomeActivity",
                    "app": "C:\\Users\\Administrator\\Desktop\\新建文件夹\\沃钱包\\wopay-4.1.1-jgjc-07311454.apk",
                    # "unicodeKeyboard":True,
                    # "resetKeyboard":True}
                    }

    def __init__(self,appium_driver):
        self.driver = appium_driver

    # 重新封装查找元素定为方法
    def find_element(self, type, loc):
        time.sleep(1)
        flag = None
        try:
            if type == 'xpath':
                element = self.find_element_by_xpath(loc)
                # element_exist(element)
                return element
            elif type == 'id':
                element = self.find_element_by_id(loc)
                # element_exist( element )
                return element
            elif type == 'name':
                element = self.find_element_by_name(loc)
                # element_exist( element )
                return element
            elif type == 'link_text':
                element = self.find_element_by_link_text(loc)
                # element_exist( element )
                return element
        except Exception:
            print('定位%s元素失败'%loc)
        else:
            print('定位%loc元素成功'%loc)
        finally:
            print('定位方法执行完成')
    # 重新封装滑动定为方法
    def swipe(self,x,x1,y,y1):
        self.swipe(start_x=x, end_x=x1, start_y=y, end_y=y1, duration=300)

# '''
#
# try:
#
# # 确保元素是可见的。
#
# # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
#
# WebDriverWait(self.driver,10).until(lambda driver: element.is_displayed())
#
# # 注意：以下入参本身是元组，不需要加*
#
# #WebDriverWait( self.driver, 10 ).until( EC.visibility_of_element_located( loc ) )
#
# return element
#
# except:
#
# print("元素没有出现，等待超时")
#
# '''