import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 設置 Chrome 選項
options = Options()
options.add_argument('--headless')  # 隱藏瀏覽器視窗

# 啟動 Chrome 瀏覽器
service = Service("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
service.start()
driver = webdriver.Remote(service.service_url, options=options)

# 前往指定的網頁
url = "https://www.kingstone.com.tw/newproduct/book/"
driver.get(url)

# 加入延遲
time.sleep(0.5)

# 解析 HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 找到書籍名稱的元素
book_names = soup.find_all('h3', class_='pdnamebox height2')

# 建立書籍清單
books = [book.text.strip() for book in book_names]

# 關閉瀏覽器
driver.quit()

# 儲存成 CSV 檔案
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['書籍名稱'])  # 寫入表頭

    # 寫入書籍名稱
    for book in books:
        writer.writerow([book])

print("書籍清單已儲存至 books.csv 檔案。")