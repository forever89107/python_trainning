# 抓取 PTT八掛版的網頁原始碼(HTML)
import bs4
import urllib.request as req
def getData(ptt_url):
    # 建立一個 Request 附加 headers，因為八卦版需要年滿18確認，所以需要cookie裡的over18=1，讓我們可直接進入
    request = req.Request(ptt_url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "cookie":"__cfduid=de48b9173eeeaa177b57867218fc4bd2f1620206631; __cf_bm=7f912ef4d0be2887dd3104ba957464b4dac9a6eb-1620206631-1800-AS2lv9FOPV4iRX+0PY7c33YbpBdySxbJZj/4KY/JQ/JlyS3jKqGE1YxvXhKO6G3NtRN9qFQyGtP4L3UFhMZgHRs=; over18=1",
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
    ptt_domian="https://www.ptt.cc"

    nextLink = root.find("a", string ="‹ 上頁")  # root.find a標籤裡符合的string
    # print(nextLink) # <a class="btn wide" href="/bbs/Gossiping/index39165.html">‹ 上頁</a>
    # print(nextLink["href"]) # /bbs/Gossiping/index39165.html
    return (ptt_domian+nextLink["href"]) # 

# 八卦版的首頁
ptt_url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 取得八卦版的上一頁
page = 0
while page <=3 :
    previous_page = getData(ptt_url)
    print("上", page , "頁 ",previous_page)
    ptt_url = previous_page
    page+=1