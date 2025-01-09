import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="session")
def context(browser_type,browser_type_launch_args,browser_context_args):
    browser_context_args = {
        "headless": False,
        "o_viewport":True
        #"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    browser_type_launch_args={
        'args':["--start-maximized"]
    }
    context = browser_type.launch_persistent_context('chrome',browser_type_launch_args,browser_context_args)
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    #page = context.new_page()
    yield context
    # context.tracing.stop(path='./trace.zip')
    context.close()
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()