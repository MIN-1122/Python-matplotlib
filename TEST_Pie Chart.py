import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft YaHei")

plt.pie([20,30,40],
        labels=["第一塊","第二塊","第三塊"])   #資料點

plt.legend()
plt.show()