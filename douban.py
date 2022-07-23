from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    # Fill input[name="wd"]
    page.fill("input[name=\"wd\"]", "douban")

    # Click text=豆瓣删除
    # with page2.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%B1%86%E7%93%A3&fenlei=256&rsv_pq=aed946c20001a95d&rsv_t=2eb3wTYiLmNyijvV89MQPjIfBP%2FeKsh0lYPaI5wJFIxE6Iib9QUtbTSVXEiU&rqlang=en&rsv_enter=1&rsv_dl=ts_0&rsv_sug3=7&rsv_sug1=6&rsv_sug7=101&rsv_sug2=1&rsv_btype=i&prefixsug=douban&rsp=0&inputT=3105&rsv_sug4=4514&rsv_sug=1&rsv_jmp=fail"):
    with page.expect_navigation():
        page.click("text=豆瓣")
    # assert page2.url == "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%B1%86%E7%93%A3&fenlei=256&rsv_pq=aed946c20001a95d&rsv_t=2eb3wTYiLmNyijvV89MQPjIfBP%2FeKsh0lYPaI5wJFIxE6Iib9QUtbTSVXEiU&rqlang=en&rsv_enter=1&rsv_dl=ts_0&rsv_sug3=7&rsv_sug1=6&rsv_sug7=101&rsv_sug2=1&rsv_btype=i&prefixsug=douban&rsp=0&inputT=3105&rsv_sug4=4514&rsv_sug=1"

    # Click text=豆瓣
    # with page2.expect_navigation(url="https://www.douban.com/"):
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("text=豆瓣")
        page3 = popup_info.value

    # Click [placeholder="书籍、电影、音乐、小组、小站、成员"]
    page3.click("[placeholder=\"书籍、电影、音乐、小组、小站、成员\"]")

    # Fill [placeholder="书籍、电影、音乐、小组、小站、成员"]
    page3.fill("[placeholder=\"书籍、电影、音乐、小组、小站、成员\"]", "cc")

    # Press Enter
    page3.press("[placeholder=\"书籍、电影、音乐、小组、小站、成员\"]", "Enter")
    # assert page3.url == "https://www.douban.com/search?q=cc"

    # Click text=photoshop cc 2019中文版(adobe PS最新版) v20. 官方...
    # with page3.expect_navigation(url="https://www.douban.com/note/694269932/?_i=8591252XUAZXH6"):
    with page3.expect_navigation():
        page3.click("text=photoshop cc 2019中文版(adobe PS最新版) v20. 官方...")
    # assert page3.url == "https://www.douban.com/note/694269932/"

    # Click :nth-match(:text("×"), 2)
    page3.click(":nth-match(:text(\"×\"), 2)")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
