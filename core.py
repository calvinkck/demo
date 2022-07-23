#coding==utf-8

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    print(page.title())
    # browser.close()




