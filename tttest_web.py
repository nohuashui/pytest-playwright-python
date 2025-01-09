#读取文件
import yaml
import pytest
from playwright.sync_api import sync_playwright
f = open('testcase.yaml',mode='r')
# cases_dict = yaml.safe_load(f)
with open('testcase.yaml', mode='r', encoding='utf-8') as f:
    cases_dict = yaml.safe_load(f)


class TestWeb:
    def run_step(self,func,value):
        # 所有用例的初始化操作
        """
        显示每个步骤执行 什么关键字
        :param func:
        :param value:
        :return:
        """
        self.page.wait_for_timeout(3000)
        func(*value)
    def run_cases(self,POCases):
        #执行用例的方法,也是重点和难点环节
        #获取所有测试用例步骤
        cases=POCases['cases']
        try:
            for case in cases:
                func=self.page.__getattribute__(case['method'])
                #获取参数
                caselist=list(case.values())
                print ("---------------caselist-----------------")
                print (caselist)
                print("---------------caselist[2:]-----------------")
                print(caselist[2:])
                self.page.wait_for_timeout(3000)
                self.run_step(func,caselist[2:])
        except Exception:
            pytest.fail('用例执行失败')

    def setup_class(self):
        #初始化
        #同步方法
        self.playwright = sync_playwright().start()
        #指定谷歌浏览器
        self.browser=self.playwright.chromium.launch(headless=False,args=["--start-maximized"],executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
        contex=self.browser.new_context(no_viewport=True)
        #打开一个浏览器标签页
        self.page=contex.new_page()


    @pytest.mark.parametrize('POCases', cases_dict['fangkeruhui'])
    def test_fangkeruhui(self,POCases):
        #调用这个方法
        self.run_cases(POCases)
        self.page.wait_for_timeout(3000)

    def teardows(self):
        self.browser.close()
        self.playwright.stop()
