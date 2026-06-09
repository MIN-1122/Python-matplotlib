import matplotlib.pyplot as plt
import csv
plt.rc("font",family="Microsoft YaHei")

file=open("data_scatter.csv",encoding="cp950")

reader=csv.reader(file)
next(reader)      #讀取第一列

data={
    "男":{"x":[],"y":[]},
    "女":{"x":[],"y":[]}
}

for row in reader:
    gender=row[0]
    data[gender]["x"].append(int(row[1])),
    data[gender]["y"].append(int(row[2])),

plt.scatter(data["男"]["x"],data["男"]["y"],label="男生")
plt.scatter(data["女"]["x"],data["女"]["y"],label="女生")

plt.xlabel("身高")
plt.ylabel("體重")

plt.legend()
plt.show()

#    print(row)  輸出csv檔裡的值




#第一組資料(2,4)(4,3)(3,6)
#第二組資料(1,2)(3,5)(4,4)

"""plt.scatter(
    [2,4,3],[4,3,6],
    c="green",s=50,               # c設定顏色，s設定大小
    label="第一組"
)

plt.scatter(
    [1,3,4],[2,5,4],
    c="#880000",s=100,
    label="第二組"
)

plt.legend()
plt.show()"""