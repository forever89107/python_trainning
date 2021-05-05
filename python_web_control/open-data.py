# 網路連線
# import urllib.request as req
# src = "https://www.ntu.edu.tw/"
# with req.urlopen(src) as response:
#     data = response.read().decode("utf-8") #取得台灣大學網站的原始碼(HTML、CSS、JS)
# print(data)

# 串接、擷取公開資料
import urllib.request as req
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with req.urlopen(src) as response:
    data = json.load(response) #內湖科技園區廠商資料
# 取得公司名稱
clist=data["result"]["results"]
with open("data.txt", "w" , encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")