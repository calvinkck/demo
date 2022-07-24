#coding==utf-8

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context= browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    print(page.title())
    page.fill("input[name=\"wd\"]", "豆瓣")
    page.click("input[name=\"wd\"]")
    # Fill input[name="wd"]

    page.close()
