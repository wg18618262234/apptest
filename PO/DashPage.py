#coding=utf-8
__author__='wg'
from PO import BasePage
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
import time
'''
京东首页涉及的所有页面元素 - 操作方法 -> 封装

element find_element(self, type, loc)
type:xpath,id,name,link_text

swipe(self,x,x1,y,y1)
'''

driver = webdriver.Remote("http://localhost:4723/wd/hub",BasePage.Base.capabilities)

ad_swipe = BasePage.Base.swipe

class Dash(BasePage.Base):

    height = driver.get_window_size()['height']
    width = driver.get_window_size()['width']

    # 初始化登录（广告-立即体验-版本更新-下次再说-登录）
    def __init__(self):
        time.sleep(5)
        if BasePage.Base.find_element(driver,'id','android:id/button1'):
            BasePage.Base.find_element(driver,'id','android:id/button1').click()
        #获取屏幕高度
        height = driver.get_window_size()['height']
        width = driver.get_window_size()['width']
        print("手机分辨率为：" + str(height) + " * " + str(width))

        # 广告滑动3次
        time.sleep(2)
        for page in range(2):
            time.sleep(1)
            ad_swipe(driver,width/5*4,width/5*1,height/2,height/2)
            time.sleep(1)

        #点击立即体验
        TouchAction(driver).tap(x=width*0.48148, y=height*0.833).perform()

        #进入登录页面
        # TouchAction(driver).tap(x=width * 0.81792, y=height * 0.17864).perform()    #坐标点击
        time.sleep(3)
        BasePage.Base.find_element(driver, 'id', 'com.unicom.wopay:id/wopay_wallet_main_login_btn').click() #id元素点击
        driver.find_element_by_id('com.unicom.wopay:id/wopay_account_center_login_mobile_edt').send_keys('18618262234\n')   #账号
        time.sleep(1)
        # driver.find_element_by_id('com.unicom.wopay:id/wopay_account_center_login_pass_edt').send_keys('11111111q\n')   #密码

        #沃钱包安全键盘输入密码
        TouchAction(driver).tap(x=width*0.12778, y=height*0.95052).perform()
        time.sleep(0.5)
        for i in range(8):
            time.sleep(0.5)
            TouchAction(driver).tap(x=55, y=1424).perform()  #64 1422 55 1424
        time.sleep(0.2)
        TouchAction(driver).tap(x=width*0.12778, y=height*0.95052).perform()
        time.sleep(0.5)
        TouchAction(driver).tap(x=width*0.05, y=height*0.73489).perform()
        time.sleep(1)

        # 点击登录
        BasePage.Base.find_element(driver,'id','com.unicom.wopay:id/wopay_login_submit_btn').click()
        time.sleep(3)
        WebDriverWait(driver,15).until(BasePage.Base.find_element(driver,'name','更多应用'))
        #更多应用
        # BasePage.Base.find_element(driver,'id','com.unicom.wopay:id/wopay_wallet_main_griditem_cv')[7].click()
        BasePage.Base.find_element(driver,'name','更多应用').click()
        #进入京东
        time.sleep(3)
        print(BasePage.Base.find_element(driver,'name','京东商城'))

if __name__ == '__main__':
    Dash.__init__(driver)