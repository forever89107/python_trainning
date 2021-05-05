# 集合的運算
s1 = {3,4,5}
# 利用 in or not in 來確認是否包含在此集合當中
(3 in s1)
(3 not in s1)
s2 = {4,5,6,7}
# s3 = s1 & s2 # 交集: 取兩個集合中，相同的資料
# s3 = s1 | s2 # 聯集: 取兩個集合中的所有資料，但不重複
# s3 = s1 - s2 # 差集: 從 s1 中 減去和 s2 相同的部分，誰減誰有先後順序
# s3 = s1 ^ s2 # 反交集: 取兩個集合中，不重疊的部分
s= set("Hello") # set 字串，字串拆解為集合，重複的不加入、不排序，結果為{'l', 'e', 'o', 'H'}
# 字點的運算 {key:value}配對
dic = {"apple" : "蘋果" , "book": "書"}
# dic["apple"] # 取得dic中 key為"apple"的資料
# 利用 in or not in 來確認是否包含在此字典當中
# print("test" in dic)
#If the key doesn't exist, it's added and points to that value. If it exists, the current value it points to is overwritten.
dic["cat"] = "貓"
print (dic)
# del dic["apple"] #刪除字典中的鍵值對(key - value pair)
# 從列表資料產生字典
dic={x:x*2 for x in [3,4,5,6,7]} # {3: 6, 4: 8, 5: 10, 6: 12, 7: 14}
print(dic)

