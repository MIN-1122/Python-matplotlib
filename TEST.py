import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft YaHei")

import csv
file=open("data.csv",encoding="cp950")
reader=csv.reader(file)
header=next(reader)
print("標頭",header) #讀取第一列
x=[]    #預期年度資料
y=[]    #預期薪資資料
for row in reader:
    print("每列的資料",row)
    x.append(int(row[0]))
    y.append([int(row[1]),int(row[2])])

plt.plot(x,y,label=header[1:3])   #標籤
plt.legend()

plt.xlabel(header[0])
plt.ylabel("薪資")

plt.show()

#折線圖
#plt.plot([1,2,3],[1,5,3])
#plt.show()

#兩條折線圖
#兩組資料點:
# (1,1),(2,2),(3,5)
# (1,2),(2,3),(3,6)
"""plt.plot([1,2,3],[[1,2],[2,3],[5,6]]
         ,label=["第一組","第二組"])

#設定軸線標題
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()  #標籤呼叫(label)
plt.show()"""