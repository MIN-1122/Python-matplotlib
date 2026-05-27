import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft YaHei")

plt.pie([20,30,40],
        labels=["第一塊","第二塊","第三塊"],
        labeldistance=0.5)   #資料點

plt.title("這是一個圓餅圖")

plt.legend()
plt.show()