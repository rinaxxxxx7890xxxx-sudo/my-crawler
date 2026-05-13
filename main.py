from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        # ブラウザを起動
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        try:
            url = "https://catalog.data.metro.tokyo.lg.jp/dataset"
            print(f"Playwrightでアクセス中: {url}")
            
            # ページを開く
            page.goto(url, wait_until="networkidle")
            
            print("--- 接続成功 ---")
            print(f"ページタイトル: {page.title()}")
            
            # せっかくなので、データセットの数も数えてみる
            count = page.locator(".dataset-heading").count()
            print(f"見つかったデータセット数: {count}")

        except Exception as e:
            print(f"エラーが発生しました: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    main()