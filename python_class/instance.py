# Point 實體物件的設計： 平面座標上的點
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y


# p1 = Point(3,4)
# p2 = Point(5,6)

# print(p1.x,p1.y)
# print(p2.x,p2.y)

# FullName 實體物件的設計：分開紀錄姓、名資料的全名
class FullName:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1 =FullName("Weng","Jung Hung")
print(name1.first,name1.last) 

name2 =FullName("Weng","Jung Jung")
print(name2.first,name2.last) 