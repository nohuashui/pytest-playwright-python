from playwright.sync_api import sync_playwright
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"], channel="chrome")
        contex = browser.new_context(no_viewport=True)
        # 打开一个浏览器标签页
        page = contex.new_page()
        page.wait_for_timeout(5000)
        page.goto("https://release.a.callie.cc/")
        page.wait_for_timeout(5000)
        yield browser
        browser.close()
        p.stop()