# 抓取 PTT股票版的網頁原始碼(HTML)
import bs4
import urllib.request as req
ptt_stock_url = "https://www.ptt.cc/bbs/Stock/index.html"
# 建立一個 Request 附加 headers
request = req.Request(ptt_stock_url, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
})
with req.urlopen(request) as res:
    data = res.read().decode("utf-8")
# print(data)
# 解析原始碼，取得每篇文章的標題
root = bs4.BeautifulSoup(data, "html.parser")
# title = root.find("div" , class_="title")  # root.find 找到一個
# <div class="title">
# <a href="/bbs/Stock/M.1620202844.A.DF8.html">[新聞] 《電腦設備》宅經濟助陣 曜越Q1飽賺</a>
# </div>
# print(title)
# print(title.a.string)  # [新聞] 《電腦設備》宅經濟助陣 曜越Q1飽賺

titles = root.find_all("div", class_="title")  # root.find_all 找到所有符合的，並返回列表
for row in titles:
    print(row.a.string)
