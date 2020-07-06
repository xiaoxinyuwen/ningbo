from appium import webdriver
import time
from com.getDeviceInfo import getInfo
'''
1、登录
2、状态到位登记
3、提交缺陷
4、提交交跨
5、提交接地电阻
6、提交零值检测
7、提交覆冰检测
8、红外测温
9、特殊到位登记
10、故障到位登记
11、检测到位登记
12、消缺到位登记
13、工单消缺
14、保电安排：危险点巡视（布控措施例巡（正常、异常）、特巡（正常、异常）、经纬度变更、危险点处理、异常消缺、通道特巡、提交缺陷）
'''
info = getInfo()
class NingBo:
    def __init__(self,user,password):
        self.user = user
        self.password = password
        desired_caps = {
            'platformName': 'Android',
            'deviceName': info[0],
            'platformVersion': info[1],
            'appPackage': 'com.uflycn.uoperation',
            'appActivity': 'com.uflycn.uoperation.ui.splash.widget.SplashActivity'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        print('连接appium，初始化，启动app！')

    #获取屏幕大小
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print('获取屏幕大小并返回！')
        return (x,y)

    #向上滑动屏幕
    def swipUp(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1,y1,x1,y2,t)
        print('向上划动一下！')

    #向下滑动屏幕
    def swipDown(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1,y1,x1,y2,t)
        print('向下划动一下！')

    #弹出框确定
    def confirm(self):
        self.driver.find_element_by_id("android:id/button1").click()

    #登录
    def login(self):
        self.driver.implicitly_wait(120)
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_username").send_keys(self.user)
        try:
            self.driver.hide_keyboard()
        except:
            print('passL-1')
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_password").send_keys(self.password)
        try:
            self.driver.hide_keyboard()
        except:
            print('passL-2')
        self.driver.find_element_by_id('com.uflycn.uoperation:id/btn_server_setting').click()
        self.driver.find_element_by_id('com.uflycn.uoperation:id/et_server_ip').clear().send_keys('product.uflycn.com')
        self.driver.find_element_by_id('com.uflycn.uoperation:id/et_server_port').clear().send_keys('7056')
        try:
            self.driver.hide_keyboard()
        except:
            print('passL-3')
        self.driver.find_element_by_id('com.uflycn.uoperation:id/et_push_port').clear().send_keys('7063')
        try:
            self.driver.hide_keyboard()
        except:
            print('passL-4')
        self.driver.find_element_by_id('com.uflycn.uoperation:id/btn_submit').click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_login").click()
        print('登录成功！')

    #开启巡视
    def startX(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_open_close_drawer").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_plan_task").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_search_line").send_keys('0512')
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_search_line").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_start_tour").click()
        print('开启巡视成功！')

    #提交缺陷
    def sMQ(self):
        #提交缺陷
        #self.daoWei()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_tour_result").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        self.swipUp(3000)
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_defect_remark").send_keys("test")
        try:
            self.driver.hide_keyboard()
        except:
            print('passQ-1')
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_addImage").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        print('提交缺陷成功！')

    #提交交跨
    def sMJ(self):
        #提交交跨
        #self.daoWei()
        #self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_tour_result").click()
        self.driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/linearLayout").click()
        #	com.uflycn.uoperation:id/btn_submit
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_get_distance").send_keys("5")
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_absolute_height").send_keys("6")
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_cross_angle").send_keys("7")
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_cross_description").send_keys("test")
        try:
            self.driver.hide_keyboard()
        except:
            print('passJ-1')
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_addImage").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        print('提交交跨成功！')

    #提交接地电阻
    def sMT1(self):
        #接地电阻
        #self.daoWei()
        #self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_tour_result").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_resistance_a").send_keys("7")
        try:
            self.driver.hide_keyboard()
        except:
            print('passT1-1')
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        print('提交接地电阻成功！')

    #提交红外测温
    def sMT2(self):
        #红外测温
        #self.daoWei()
        #self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_tour_result").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_infrared_temperature").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_guide_line").send_keys("5")
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_environment_temperature").send_keys("6")
        try:
            self.driver.hide_keyboard()
        except:
            print('passT2-1')
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_big_size_slide_a").send_keys("7")
        try:
            self.driver.hide_keyboard()
        except:
            print('passT2-2')
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        print('提交红外测温成功！')

    #提交零值检测
    def sMT3(self):
        #零值检测
        #self.daoWei()
        #self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_tour_result").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_zero_check").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_jueyuan_count").send_keys("3")
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_select_tower1").click()
        print('提交零值成功！')

    #提交覆冰厚度
    def sMT4(self):
        #覆冰检测
        #self.daoWei()
        #self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_tour_result").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_ice_cover").click()
        self.driver.find_element_by_id("android:id/text1").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_ice_cover").send_keys("10")
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_ice_temp").send_keys("10")
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_ice_humidity").send_keys("10")
        try:
            self.driver.hide_keyboard()
        except:
            print('passT4-1')
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        print('提交覆冰厚度成功！')

    #提交缺陷、交跨、接地、红外、覆冰
    def sM(self):
        '''

        try:
            self.login()
        except:
            print('登录失败')


        try:
            self.startX()
        except:
            print('开启巡视失败')
        try:
            self.daoW1()
        except:
            print('状态到位失败')
            '''
        try:
            self.sMQ()
        except:
            print('提交缺陷失败')
        try:
            self.sMJ()
        except:
            print('提交交跨失败')
        try:
            self.sMT1()
        except:
            print('提交接地失败')
        try:
            self.sMT2()
        except:
            print('提交红外测温失败')
        try:
            self.sMT4()
        except:
            print('提交覆冰厚度失败')
        try:
            self.back()
        except:
            print('返回失败！')

    #状态到位
    def daoW1(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_register_loaction").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath(
            " /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath(
            " /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img_confirm").click()
        self.driver.find_element_by_id("android:id/button1").click()
        print('状态到位成功！')

    #特殊到位
    def daoW2(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_register_loaction").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/sp_tour_nature").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img_confirm").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_register_loaction").click()
        print('特殊到位成功！')

    #故障到位
    def daoW3(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_register_loaction").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/sp_tour_nature").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img_confirm").click()
        self.driver.find_element_by_id("android:id/button1").click()
        print('故障到位成功！')

    #检测到位
    def daoW4(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_register_loaction").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/sp_tour_nature").click()
        self.driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img_confirm").click()
        self.driver.find_element_by_id("android:id/button1").click()
        print('检测到位成功！')

    #消缺到位
    def daoW5(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_register_loaction").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/sp_tour_nature").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[5]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img").click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.widget.GridView/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add_img_confirm").click()
        self.driver.find_element_by_id("android:id/button1").click()
        print('消缺到位成功！')

    #全部到位
    def daoW(self):
        # try:
        #     self.login()
        # except:
        #     print('登陆失败')
        # try:
        #     self.startX()
        # except:
        #     print('开启巡视失败')
        try:
            self.daoW1()
        except:
            print('状态到位失败')
        try:
            self.daoW2()
        except:
            print('特殊到位失败')
        try:
            self.daoW3()
        except:
            print('故障到位失败')
        try:
            self.daoW4()
        except:
            print('检测到位失败')
        try:
            self.daoW5()
        except:
            print('消缺到位失败')

    #返回
    def back(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_back").click()
        print('返回上一页！')

    #添加图片
    def addPicture(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_addImage").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_gallery").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_right_lh").click()
        # try:
        #     self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        # except:
        #     print('no this button!')
        # print('添加图片成功！')


#14、保电安排：危险点巡视（布控措施例巡（正常、异常）、特巡（正常、异常）、经纬度变更、危险点处理、异常消缺、通道特巡、提交缺陷）
    '''
    危险点：com.uflycn.uoperation:id/ll_dangerous_point
    巡视：/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[1]/android.widget.Button
    处理：/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[2]/android.widget.Button
    异常记录：/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[3]/android.widget.Button
    
    +：com.uflycn.uoperation:id/iv_add
    经度：	com.uflycn.uoperation:id/et_longitude
    纬度：com.uflycn.uoperation:id/et_latitude
    提交：com.uflycn.uoperation:id/btn_commit
    
    例巡：com.uflycn.uoperation:id/btn_dispost
    缺陷描述：com.uflycn.uoperation:id/et_defect_remark
    正常按钮：android:id/text1
    异常：/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]
    提交：com.uflycn.uoperation:id/btn_submit
    
    现场情况描述：com.uflycn.uoperation:id/et_dp_remark
    提交：com.uflycn.uoperation:id/btn_dp_commit
    正常按钮：	com.uflycn.uoperation:id/sp_dp_state
    异常：/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]
    机械类型：com.uflycn.uoperation:id/sp_dp_type
    人工作业：	/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[6]
    
    现场情况描述：	com.uflycn.uoperation:id/et_dp_remark
    提交：com.uflycn.uoperation:id/btn_commit
    
    异常记录消缺：com.uflycn.uoperation:id/btn_error_dispose
    异常描述：	com.uflycn.uoperation:id/et_defect_remark
    提交：	com.uflycn.uoperation:id/btn_submit
    
    '''
    #例巡正常
    def danger1(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_dangerous_point").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[1]/android.widget.Button").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_dispost").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_defect_remark").send_keys("test for automation")
        try:
            self.driver.hide_keyboard()
        except:
            print("danger-1")
        self.addPicture()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        self.confirm()
        self.back()
        self.back()
        print('危险点-例巡-正常-提交成功')

    #例巡异常
    def danger2(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_dangerous_point").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[1]/android.widget.Button").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_dispost").click()
        self.driver.find_element_by_id("android:id/text1").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_defect_remark").send_keys("test for automation")
        try:
            self.driver.hide_keyboard()
        except:
            print("danger-2")
        self.addPicture()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        self.confirm()
        self.back()
        self.back()
        print("危险点-例巡-异常-提交成功")


    #特巡正常
    def danger3(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_dangerous_point").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[1]/android.widget.Button").click()
        self.swipUp(3000)
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_dp_remark").send_keys("test for automation")
        try:
            self.driver.hide_keyboard()
        except:
            print("danger-3")
        self.addPicture()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_dp_commit").click()
        self.confirm()
        self.back()
        print('危险点-例巡-正常-提交成功')

    #特巡异常
    def danger4(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_dangerous_point").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[1]/android.widget.Button").click()
        self.swipUp(3000)
        self.driver.find_element_by_id("com.uflycn.uoperation:id/sp_dp_state").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/sp_dp_type").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[6]").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_dp_remark").send_keys("test for automation")
        try:
            self.driver.hide_keyboard()
        except:
            print("danger-4")
        self.addPicture()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_dp_commit").click()
        self.confirm()
        print('危险点特巡异常提交成功！')
        self.back()


    #经纬度修改
    def danger5(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_dangerous_point").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[1]/android.widget.Button").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_add").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_longitude").send_keys("123.321")
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_latitude").send_keys("12.21")
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_commit").click()
        print('危险点经纬度变更成功！')
        self.back()
        self.back()

    #处理提交
    def danger6(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_dangerous_point").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[2]/android.widget.Button").click()
        self.swipUp(1500)
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_dp_remark").send_keys("test for automation")
        try:
            self.driver.hide_keyboard()
        except:
            print("danger-6")
        self.addPicture()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_commit").click()
        self.confirm()
        print('危险点处理提交成功！')
        self.back()
    #异常记录消缺
    def danger7(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/ll_dangerous_point").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[9]/android.widget.LinearLayout[3]/android.widget.Button").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_error_dispose").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_defect_remark").send_keys("test for automation")
        try:
            self.driver.hide_keyboard()
        except:
            print("danger-7")
        self.addPicture()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        self.confirm()
        print('异常消缺成功！')
        self.back()
        self.back()


    def danger(self):
        self.danger1()
        self.danger2()
        self.danger3()
        self.danger4()
        self.danger5()
        self.danger6()
        self.danger7()

    #开启保电安排
    def  startProPlan(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_open_close_drawer").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_protect_electricity").click()
        self.driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[6]/android.widget.Button[1]").click()
        print('开启保电计划成功！')

    #通道巡视
    def tongD(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_channel_tour").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_add").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/et_description").send_keys("tset for automation")
        try:
            self.driver.hide_keyboard()
        except:
            print('tongD-1')
        self.addPicture()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit").click()
        self.back()
        print('通道特巡提交成功！')

    #开启检修计划
    def startJianX(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_open_close_drawer").click()
        self.swipUp(700)
        self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_maintenance_plan").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_execute").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_start_line").click()
        print('成功开启检修计划!')

    #关闭检修计划
    def endJianX(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_open_close_drawer").click()
        self.swipUp(700)
        self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_maintenance_plan").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_execute").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_start_line").click()
        print('成功关闭检修计划！')
        self.back()
        self.backX()

    #检修备注
    def jianXiuBeiZ(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_start_line").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_start_line").click()
        self.addPicture()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_start_line").send_keys("test for automation")
        try:
            self.driver.hide_keyboard()
        except:
            print('检修备注')
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_submit")
        print('检修备注提交成功！')
        self.back()

    #结束我的巡视
    def endX(self):
        #com.uflycn.uoperation: id / rb_tour
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_open_close_drawer").click()
        self.swipUp(2000)
        self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_tour").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/btn_all_stop").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/dlg_btn_right").click()
        # self.driver.find_element_by_id("com.uflycn.uoperation:id/tv_channel_tour").click()
        # self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_my_tour").click()
        self.backX()
        print('结束巡视成功！')

    #回到巡视页面
    def backX(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_open_close_drawer").click()
        try:
            self.swipDown(1000)
        except:
            self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_my_tour").click()
        print('回到巡视页面！')

    #关闭保电
    def endPro(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_open_close_drawer").click()
        self.driver.find_element_by_id("com.uflycn.uoperation:id/rb_protect_electricity").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[6]/android.widget.Button[1]").click()
        print('关闭保电成功@！')
        self.backX()

    def test(self):
        self.driver.find_element_by_id("com.uflycn.uoperation:id/iv_open_close_drawer").click()
        while 1:
            self.swipUp(3000)
            time.sleep(3)
            self.swipDown(3000)
            time.sleep(3)







'''
巡视页面：com.uflycn.uoperation:id/rb_my_tour

检修计划、保电安排（危险点、通道巡视）、事务管理
检修计划：	com.uflycn.uoperation:id/rb_maintenance_plan
开启踏勘：	com.uflycn.uoperation:id/btn_execute
开启线路：	com.uflycn.uoperation:id/btn_start_line
踏勘备注：com.uflycn.uoperation:id/btn_remark
已完成：com.uflycn.uoperation:id/rb_has_finish
未完成：com.uflycn.uoperation:id/rb_no_finish
工作备注：	com.uflycn.uoperation:id/et_work_remark
提交：	com.uflycn.uoperation:id/btn_submit


事务管理：com.uflycn.uoperation:id/rb_transaction
+：com.uflycn.uoperation:id/iv_add_tran
事务主题：	com.uflycn.uoperation:id/et_transaction_topic
事务要求：	com.uflycn.uoperation:id/ed_transaction_request
事务内容：	com.uflycn.uoperation:id/ed_transaction_content
负责人：com.uflycn.uoperation:id/tv_transaction_principal
确定：com.uflycn.uoperation:id/btnSubmit
计划完成时间：com.uflycn.uoperation:id/tv_transaction_start_time
确定：	com.uflycn.uoperation:id/btnSubmit
配合人：/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.CheckBox
提交：com.uflycn.uoperation:id/btn_submit

工单任务：com.uflycn.uoperation:id/rb_work_order

月计划：com.uflycn.uoperation:id/rb_mouth_plan

检修设备：com.uflycn.uoperation:id/rb_overhaul_equipment

在线监控：com.uflycn.uoperation:id/rb_online_monitor

机巡监控：com.uflycn.uoperation:id/rb_flight_monitor

临时通知：com.uflycn.uoperation:id/rb_temp_task

我的巡视：com.uflycn.uoperation:id/rb_tour
全部停止：	com.uflycn.uoperation:id/btn_all_stop
确定：	com.uflycn.uoperation:id/dlg_btn_right

输电手册：	com.uflycn.uoperation:id/rb_document

离线数据：com.uflycn.uoperation:id/rb_offlinedata

'''







