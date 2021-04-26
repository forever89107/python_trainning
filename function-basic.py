# 定義函式
def multiply(n1 , n2):
    return n1*n2 # 需定義回傳值，否則 value = none
# 呼叫函式
multiply(3,4)
value = multiply(10,8)+multiply(5,4)
print (value)

# 函式可用來做程式的包裝: 同樣的邏輯可以重複利用
def calculate(max):
    sum = 0
    for n in range(1,max+1):
        sum = sum + n
    print(sum)

calculate(10)