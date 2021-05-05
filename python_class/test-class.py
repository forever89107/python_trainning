# 定義類別與類別屬性(封裝在類別中的變數和函式)
class IO:
    supportedSrcs=["console","files"]
    def read(src):
        if src not in IO.supportedSrcs :
            print("not Supported")
        else:
            print("Read form",src)
# 使用類別
print(IO.supportedSrcs)
IO.read("file")