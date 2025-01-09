#读取文件
from playwright.sync_api import Page
import pytest
from playwright.sync_api import sync_playwright
from lib.webui_meeting import enter_meeting
from lib.webui_callie import user_login
def setup_module():
    print('\n *** 初始化-模块（清除所有类） ***')

def teardown_module(p):
    print('\n ***   清除-模块（清除所有类） ***')
#p = sync_playwright().start()
# 指定谷歌浏览器
class TestCallie:
    #在类中定义类方法需要加装饰器
    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')
    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')

    def setup_method(cls):
        print('\n --- 初始化-方法  ---')
        cls.p = sync_playwright().start()
        # 指定谷歌浏览器
        cls.browser = cls.p.chromium.launch(headless=False, args=["--start-maximized"], channel="chrome")
        cls.contex = cls.browser.new_context(no_viewport=True)
        # 打开一个浏览器标签页
        cls.page = cls.contex.new_page()
        cls.page.wait_for_timeout(5000)

    def teardown_method(cls):
        print('\n --- 清除  -方法 ---')
        cls.contex.close()
        cls.browser.close()
        cls.p.stop()
    def test_right_login(cls):
        # 调用这个方法
        alertText=user_login('991289327@qq.com','123456',cls.page)
        assert alertText == False
    def test_error_paswcord(cls):
        # 调用这个方法
        alertText=user_login('991289327@qq.com','123786',cls.page)
        assert alertText ==True


    # @pytest.mark.parametrize("createUser", [("zhangsan", "111111"), ("lisi", "111")],indirect=True)
    # def test_A00100X(self,createUser):
    #     print('\nusername is', createUser['username'])
    #     print('测试行为')
    # #使用DBB把步骤相同，参数值不同的用例参数独立出来
    # @pytest.mark.parametrize('username, password', [('111', '88888888'),('10009606@nd','Ysp2019..')])
    # def test_login(self,username,password):
    #     user_login(username,password)
    #     assert 2 == 2
# class Test_casetwo:
#

#     def test_C001021(self):
#         print('\n用例C001021')
#         assert 1 == 1
#
#     def test_C001022(self):
#         print('\n用例C001022')
#         assert 2 == 2