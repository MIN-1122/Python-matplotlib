from email import header

import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft YaHei")

#資料點(x,height):("T",4) ("A",6) ("O",2)

plt.bar(
    ["T","A","O"],
    [4,6,2],
    width=0.5,         #width設定參數寬度
    color="red"
)

plt.legend()
plt.show()