# 判斷式
# x=int(input("請輸入數字: ")) # 取得字串行式的使用者輸入 -> 將字串型態轉換成數字型態
# y=int(input("請輸入數字: ")) # 取得字串行式的使用者輸入 -> 將字串型態轉換成數字型態
# if x>=200: # True 跑這個
#     print (x , "，大於200")
# elif x>=100: # True 跑這個
#     print (x , "，小於200，大於100")
# else: # False 跑這個
#     print (x , "，小於100")
op=input("請輸入運算子(ex: +, -, *, /) -> ")
# if op=="+":
#     print(x+y)
# elif op=="-":
#     print(x-y)
# elif op=="*":
#     print(x*y)
# elif op=="/":
#     print(x/y)
# else:
#     print("不支援此運算符!!")

# python 不支援 switch，取代方式如下
op=int(op)
switch={1:"+", 2:"-", 3:"*", 4:"/"}
print("選擇符號為: ",switch[op])
