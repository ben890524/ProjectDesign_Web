from bs4 import BeautifulSoup
import requests

# Google 爬蟲
class Google():
    def __init__(self, search):
        self.search = search  # 查詢的消息
        self.headers = {"user-agent" : "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36"}

    def scrape(self):
        # Google 搜尋 URL
        google_url = 'http://www.google.com.tw/search'

        # 查詢參數
        my_params = {'q': self.search}

        # 下載 Google 搜尋結果
        r = requests.get(google_url, params = my_params, headers = self.headers)
        content = []
        # 確認是否下載成功
        if r.status_code == requests.codes.ok:
            # 以 BeautifulSoup 解析 HTML 原始碼
            soup = BeautifulSoup(r.text, 'html.parser')
            for g in soup.find_all('div', class_='xpd', limit = 7):
                anchors = g.find('a')

                if anchors is not None and "國家/地區" not in anchors.getText():
                    href = anchors.get('href')
                    # if anchors is None:
                    #     print(77777777777,anchors)

                    if anchors.find("h3"):
                        h3 = anchors.find("h3").find('div').getText()
                        # print(anchors, "\n")
                        href = href.replace('/url?q=', '')
                        end_index = href.find('&sa=')
                        href = href[:end_index]
                        # print(href, "\n")
                        # print(h3, "\n")
                        content.append([h3, href])
        return content