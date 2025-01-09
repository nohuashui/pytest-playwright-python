#读取文件
import yaml
from playwright.sync_api import Page
import pytest
import common.action as action
from playwright.sync_api import sync_playwright



class Test_Web:
    def setup_class(self):
        #初始化
        self.playwright = sync_playwright().start()
        #指定谷歌浏览器
        self.browser=self.playwright.chromium.launch(headless=False,args=["--start-maximized"],executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe',)
        contex=self.browser.new_context(no_viewport=True)
        #打开一个浏览器标签页
        self.page=contex.new_page()
        self.page.wait_for_timeout(3000)
        self.page.goto("https://meeting-web.beta.101.com/")
        self.page.wait_for_timeout(3000)
    def test_huiyihaocuowu(self):
        #调用这个方法
        #action.get_frame_ele(page,'//*[@id="root"]/div/div/div/div/div[1]/iframe','//*[@id="conferenceId"]','217430700')
        mainframe= self.page.frame_locator('//*[@id="root"]/div/div/div/div/div[1]/iframe')
        mainframe.locator('//*[@id="conferenceId"]').fill('123456')
        mainframe.locator('//*[@id="smart-meeting-button"]').click()
        self.page.wait_for_timeout(3000)
    def test_fangkeruhui(self):
        #调用这个方法
        #action.get_frame_ele(page,'//*[@id="root"]/div/div/div/div/div[1]/iframe','//*[@id="conferenceId"]','217430700')
        mainframe= self.page.frame_locator('//*[@id="root"]/div/div/div/div/div[1]/iframe')
        mainframe.locator('//*[@id="conferenceId"]').fill('217430700')
        mainframe.locator('//*[@id="smart-meeting-button"]').click()
        self.page.wait_for_timeout(3000)


    def teardows(self):
        self.browser.close()
        self.playwright.stop()
