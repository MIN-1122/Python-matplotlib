import matplotlib.pyplot as plt
plt.rc("font",family="Microsoft YaHei")

x=[20,10,40]
total=sum(x)    #sum(列表)，計算列表中的數值總和
labels={str(100*data/total)+"%" for data in x}     #產生列表並計算%值

plt.pie(
        x,                               #資料點
        labels=labels,
        labeldistance=0.5,               #參數設定標籤位置
)

plt.title("這是一個圓餅圖")            #圖表標題

plt.legend()      #依標籤產生圖例
plt.show()