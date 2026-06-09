import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft YaHei")

"""
範例資料:
    日期     價格
    11/01   開盤 95, 收盤 80, 最高 100, 最低 75
    11/02   開盤 82, 收盤 75, 最高 83, 最低 65
    11/03   開盤 73, 收盤 85, 最高 90, 最低 70
"""

plt.bar("11/01",15,bottom=80,width=0.5,color="green")   #陰
plt.bar("11/01",25,bottom=75,width=0.1,color="green")   #影
plt.bar("11/02",7,bottom=75,width=0.5,color="green")    #陰
plt.bar("11/02",18,bottom=65,width=0.1,color="green")   #影
plt.bar("11/03",12,bottom=73,width=0.5,color="red")     #陽
plt.bar("11/03",20,bottom=70,width=0.1,color="red")     #影

plt.show()

#長條圖堆疊出k線圖
#資料點: 日期:10/15 價格: 開盤85 收盤80 最高88 最低78

"""plt.bar(
    "10/15",5,
    bottom=80,width=0.5,color="green"
)

plt.bar(
    "10/15",10,
    bottom=78,width=0.1,color="green"
)

plt.xlabel("x")
plt.ylabel("y")

plt.show()"""