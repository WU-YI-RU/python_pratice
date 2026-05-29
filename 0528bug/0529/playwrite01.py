from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Browser：啟動新的 Chromium 瀏覽器（headless 模式，不顯示視窗）
    browser = p.chromium.launch()

    # Context：建立一個隔離的瀏覽環境
    context = browser.new_context()

    # Page：開一個新分頁
    page = context.new_page()

    page.goto("https://24h.pchome.com.tw")
    print(page.title())
    button

    browser.close()