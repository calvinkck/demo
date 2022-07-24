from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Open new page
    page1 = context.new_page()

    # Go to about:blank
    page.goto("about:blank")

    # Close page
    page.close()

    # Click body
    page1.click("body")

    # Open new page
    page2 = context.new_page()

    # Go to https://www.baidu.com/
    page2.goto("https://www.baidu.com/")

    # Close page
    page1.close()

    # Click input[name="wd"]
    page2.click("input[name=\"wd\"]")

    # Fill input[name="wd"]
    page2.fill("input[name=\"wd\"]", "douban")

    # Click text=豆瓣
    # with page2.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%B1%86%E7%93%A3&fenlei=256&rsv_pq=fad9704100008c66&rsv_t=2385IwHKMj30mrbC6hpbHYow%2B98kZJAtbzXto1js0MfcbdVxpv1KB3DLT5M&rqlang=cn&rsv_enter=1&rsv_dl=ts_0&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&rsv_sug2=1&rsv_btype=i&prefixsug=douban&rsp=0&inputT=2782&rsv_sug4=3552&rsv_jmp=fail"):
    with page2.expect_navigation():
        page2.click("text=豆瓣")
    # assert page2.url == "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%B1%86%E7%93%A3&fenlei=256&rsv_pq=fad9704100008c66&rsv_t=2385IwHKMj30mrbC6hpbHYow%2B98kZJAtbzXto1js0MfcbdVxpv1KB3DLT5M&rqlang=cn&rsv_enter=1&rsv_dl=ts_0&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&rsv_sug2=1&rsv_btype=i&prefixsug=douban&rsp=0&inputT=2782&rsv_sug4=3552"

    # Click text=豆瓣
    # with page2.expect_navigation(url="https://www.douban.com/"):
    with page2.expect_navigation():
        with page2.expect_popup() as popup_info:
            page2.click("text=豆瓣")
        page3 = popup_info.value

    # Click [placeholder="书籍、电影、音乐、小组、小站、成员"]
    page3.click("[placeholder=\"书籍、电影、音乐、小组、小站、成员\"]")

    # Fill [placeholder="书籍、电影、音乐、小组、小站、成员"]
    page3.fill("[placeholder=\"书籍、电影、音乐、小组、小站、成员\"]", "cc")

    # Press Enter
    page3.press("[placeholder=\"书籍、电影、音乐、小组、小站、成员\"]", "Enter")
    # assert page3.url == "https://www.douban.com/search?q=cc"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
