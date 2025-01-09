import pytest
from playwright.sync_api import sync_playwright
import conftest
from playwright.sync_api import Page
def user_login(username,password,page:Page):
    page.goto("https://release.a.callie.cc/")
    page.wait_for_timeout(5000)
    #点击登录按钮
    #根据文本信息定位，不适合多语言的系统
    #page.get_by_text("Anmelden").click()
    page.locator(".top-user").wait_for()
    page.locator('.top-user').click()
    #等待登录按钮出现
    page.wait_for_timeout(3000)
    page.locator(".head-user-login").wait_for()
    #点击登录按钮
    page.locator('.head-user-login').click()
    page.wait_for_timeout(3000)
    # 定位到登录iframe
    loginframe = page.frame_locator('#headLgoinIframe')
    page.wait_for_timeout(3000)
    #等待账号输入框出现
    #.form-input , .form-index email-input 会匹配到多个元素
    loginframe.locator('[param-key="index.email"]').wait_for()
    #在账号输入框输入账号
    loginframe.locator('[param-key="index.email"]').fill(username)
    #点击继续按钮
    loginframe.locator('#continue-btn').click()
    #等待输入密码框出现
    #组合定位法loginframe.locator('.form-text > .login-password').wait_for()
    #通过属性定位loginframe.locator('[param-key="password"]').wait_for()
    #通过标签的文本定位
    page.wait_for_timeout(3000)
    print("----------------mima-----------------------")
    loginframe.locator('[param-key="password"]').wait_for()
    #点击密码输入框
    loginframe.locator('[param-key="password"]').fill(password)
    #点击登录按钮
    loginframe.locator('#login-btn').click()
    page.wait_for_timeout(5000)
    page.screenshot(path='right_login_prc.png', full_page=True)
    #判断登录按钮有没有存在
    alertText=loginframe.locator('#login-btn').is_visible()
    return alertText

