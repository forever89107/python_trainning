# break 的簡易範例
# n = 0
# while n<=5:
#     print(n)
#     if(n==3):
#         break
#     n+=1
# print("n最後是: ",n)

# continue 的簡易範例
# for x in [0,1,2,3]:
#     if x % 2 == 0: # x 是偶數
#         continue
#     print(x)

# else 的簡易範例
# sum = 0
# for x in range(11):
#     sum+=x
# else:
#     print(sum) # 印出0+1+2+....+10的結果

#綜合範例：找出整數平方根
#輸入9, 得到3
#輸入11, 得到【沒有】 整數的平方根
n = int(input("請輸入正整數:"))
if n**0.5 % 1 == 0 :
    print (n**0.5)
else:
    print("【沒有】 整數的平方根")

