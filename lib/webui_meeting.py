import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
def enter_meeting(num):
    p = sync_playwright().start()
    # 指定谷歌浏览器
    browser = p.chromium.launch(headless=False, args=["--start-maximized"],
                                          executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
    contex = browser.new_context(no_viewport=True)
    # 打开一个浏览器标签页
    page = contex.new_page()
    page.wait_for_timeout(3000)
    page.goto("https://meet.101.com/?sdp-app-id=52913ac2-ae39-4cb8-b6c9-f093d43d65a8#/")
    page.wait_for_timeout(3000)

    mainframe = page.frame_locator('//*[@id="root"]/div/div/div/div/div[1]/iframe')
    mainframe.locator('//*[@id="conferenceId"]').fill(num)
    page.wait_for_timeout(3000)
    mainframe.locator('//span[text()="加入会议"]').click()
    page.wait_for_timeout(3000)
    browser.close()
    p.stop()
    return num
def user_login(username,password):
    p = sync_playwright().start()
    # 指定谷歌浏览器
    browser = p.chromium.launch(headless=False, args=["--start-maximized"],executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
    contex = browser.new_context(no_viewport=True)
    # 打开一个浏览器标签页
    page = contex.new_page()
    page.wait_for_timeout(3000)
    page.goto("https://meet.101.com/?sdp-app-id=52913ac2-ae39-4cb8-b6c9-f093d43d65a8#/")
    page.wait_for_timeout(3000)
    mainframe = page.frame_locator('//*[@id="root"]/div/div/div/div/div[1]/iframe')
    page.wait_for_timeout(3000)
    mainframe.locator('//*[@id="root"]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]').click()
    page.wait_for_timeout(3000)
    mainframe.locator('//*[@id="loginName"]').fill(username)
    page.wait_for_timeout(3000)
    mainframe.locator('//*[@id="password"]').fill(password)
    page.wait_for_timeout(3000)
    mainframe.get_by_text('登录').click()
    browser.close()
    p.stop()