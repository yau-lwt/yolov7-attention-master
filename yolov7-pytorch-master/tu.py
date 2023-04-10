import numpy as np
import matplotlib.pyplot as plt

# 读取txt文件，存储为一维数组
with open('C:/Users/taotao/Desktop/log/loss_2023_03_31_22_25_46/epoch_loss.txt', 'r') as f:
    data_str = f.read().split('\n')
    data_str = [i.strip() for i in data_str if i.strip()]
    data = np.array([float(i) * 1000 for i in data_str])  # 给每个数字乘1000

# 将数据分成每十个一组
group_size = 10
group_num = len(data) // group_size
data_group = [data[i*group_size:(i+1)*group_size] for i in range(group_num)]

# 绘制折线图
x = np.arange(group_size)
for i in range(group_num):
    y = data_group[i]
    plt.plot(x, y)
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()
