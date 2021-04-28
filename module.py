# 載入內建的 sys 模組蹦取得資訊，as 別名
# import sys
# import sys as s
# print (s.platform)
# print (s.maxsize)

# 建立 geometry 模組，載入使用
# print(geometry.distance(1, 1, 5, 5))
# print(geometry.slope(1, 2, 5, 6))
# geometry.slope()

# 調整搜尋模組的路徑
from modules import geometry
import sys
print(geometry.distance(1, 1, 5, 5))
sys.path.append("modules")  # 改變預設遍歷的路徑

print(sys.path)  # 印出模組的搜尋路徑，python 會在這些路徑底下找想要引入的模組
