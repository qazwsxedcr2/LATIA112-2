import csv
import requests
from bs4 import BeautifulSoup

# 定義自定義的 User-Agent 標頭
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 使用 requests 套件發送 GET 請求，並加入 headers
response = requests.get("https://www.kingstone.com.tw/newproduct/book/", headers=headers)

# 確認請求成功
if response.status_code == 200:
    # 解析 HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 找到書籍名稱的元素
    book_names = soup.find_all('h3', class_='pdnamebox height2')
    
    # 建立書籍清單
    books = [book.text.strip() for book in book_names]
    
    # 儲存成 CSV 檔案
    with open('booksrequests.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['書籍名稱'])
        
        # 寫入書籍名稱
        for book in books:
            writer.writerow([book])
        
    print("書籍清單已儲存至 booksrequests.csv 檔案。")