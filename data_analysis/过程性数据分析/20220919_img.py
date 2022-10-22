import matplotlib.pyplot as plt
import pandas as pd
import os
from matplotlib import rcParams
'''
画图，生成每个学生在1800秒内的行为图
'''
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
j = 0
for data_path in os.listdir("./img_data"):
    j += 1
    print(j)
    data = pd.read_csv(os.path.join("./img_data",data_path),encoding="gbk")
    task = ['运动会问题','生活水平问题']
    task_page = [8,9]
    taks_name = [i for i in task]
    label = []
    for i in taks_name:
        for k in range(task_page[task.index(i)]):
            label.append(i +"_" + str(k))
    for i in label:
        locals()[f'{i}_y_true']= data[(data['page']==i) & (data['is_change']==True)]['time']
        locals()[f'{i}_z_true'] = data[(data['page']==i) & (data['is_change']==True)]['current_time']
        locals()[f'{i}_y_false']= data[(data['page']==i) & (data['is_change']==False)]['time']
        locals()[f'{i}_z_false'] = data[(data['page']==i) & (data['is_change']==False)]['current_time']
    fig = plt.figure(figsize=(10, 6))  # 调整画布大小
    ax = plt.gca()
    ax.set_facecolor('oldlace')
    width = 0.5
    plt.xlim(0,1800)
    for i in label:
        if i != '运动会问题_7' and i != '生活水平问题_8':
            locals()[f'p{label.index(i)}'] = plt.barh([i],locals()[f'{i}_y_false'],width, left=locals()[f'{i}_z_false'], color='blue',linewidth=2)
            locals()[f'p{label.index(i)}'] = plt.barh([i],locals()[f'{i}_y_true'],width, left=locals()[f'{i}_z_true'], color='red',linewidth=2)
    plt.grid(True)
    plt.xlabel("时间（秒）")
    plt.title(f'{data_path.split(".csv")[0]}')
    plt.xticks()


    plt.savefig("./img/time_img/{}.jpg".format(data_path.split(".csv")[0]))