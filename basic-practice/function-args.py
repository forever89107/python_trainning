# 參數的預設資料
def power(base , exp = 0):
    print(base ** exp)
power(3,2)
power(4)

# 使用參數名稱對應 
def divide(n1,n2):
    print (n2/n1)

divide(2,4)
divide(n2 = 4, n1 = 1)

# 無限 / 不定 參數資料: *變數名
def avg(*numbers):
    sum = 0
    for x in numbers:
        sum+= x
    sum=sum/len(numbers)
    print(numbers,"平均值為: ",sum)

avg(3,4)
avg(5,6,7)
    