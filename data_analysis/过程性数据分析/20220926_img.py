import pandas as pd
import os
import glob
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
'''
画图，生成热力图
'''
data2 = pd.read_csv('A卷_转化能力值.csv',converters = {'STU_CODE':str},encoding='gbk')
high_level = data2[data2['IRT_ZHUANHUA'] >= 1]['STU_CODE'].values
middle_level = data2[(data2['IRT_ZHUANHUA'] < 1) & (data2['IRT_ZHUANHUA'] > -1)]['STU_CODE'].values
low_level = data2[data2['IRT_ZHUANHUA'] <= -1]['STU_CODE'].values
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
all_csv = glob.glob(os.path.join('img_data', '*.csv'))
high_data_frames = []
middle_data_frames = []
low_data_frames = []
for csv in all_csv:
    code_name = str(csv.split('\\')[1].split('.')[0])[:-1]
    data_frame = pd.read_csv(csv,encoding='gbk')  # 添加列标题
    data_frame1 = data_frame.drop(data_frame[(data_frame['page']=='生活水平问题_8') | (data_frame['page']=='运动会问题_7')].index)
    if code_name in high_level:
        high_data_frames.append(data_frame1)
    if code_name in middle_level:
        middle_data_frames.append(data_frame1)
    if code_name in low_level:
        low_data_frames.append(data_frame1)
high_frame_concat = pd.concat(high_data_frames, axis=0, ignore_index=True)
print(high_frame_concat)
middle_frame_concat = pd.concat(middle_data_frames, axis=0, ignore_index=True)
low_frame_concat = pd.concat(low_data_frames, axis=0, ignore_index=True)# axis = 0 表示数据垂直合并,等于1表示
print('合并完成!')
# je_cut = [0, 360, 720, 1080, 1440, 1800]
je_cut = np.arange(0,1800,60)
je_label = ['0-360', '360-720', '720-1080', '1080-1440', '1440-1800']  #
high_frame_concat['时间区间'] = pd.cut(high_frame_concat['current_time'], bins=je_cut)
middle_frame_concat['时间区间'] = pd.cut(middle_frame_concat['current_time'], bins=je_cut)
low_frame_concat['时间区间'] = pd.cut(low_frame_concat['current_time'], bins=je_cut)


sorts = ['生活水平问题_7','生活水平问题_6','生活水平问题_5','生活水平问题_4','生活水平问题_3','生活水平问题_2',
                                             '生活水平问题_1','生活水平问题_0','运动会问题_6','运动会问题_5','运动会问题_4','运动会问题_3',
                                             '运动会问题_2','运动会问题_1','运动会问题_0']
high_Summary = high_frame_concat.pivot_table(index = 'page',columns = '时间区间', values = 'time', aggfunc = np.sum,fill_value = 0)
high_Summary = high_Summary.reindex(index = sorts)
print(high_Summary)

middle_Summary = middle_frame_concat.pivot_table(index = 'page',columns = '时间区间', values = 'time', aggfunc = np.sum,fill_value = 0)
middle_Summary = middle_Summary.reindex(index = sorts)
low_Summary = low_frame_concat.pivot_table(index = 'page',columns = '时间区间', values = 'time', aggfunc = np.sum,fill_value = 0)
low_Summary = low_Summary.reindex(index = sorts)
lables = ['高分','中段','低分']
im = [high_Summary,middle_Summary,low_Summary]
for i in range(len(im)):
    fig = plt.figure(figsize=(18, 12))
    sns.heatmap(data = im[i], # 指定绘图数据 # 指定填充色
                linewidths = 0,cmap="hot_r"# 设置每个单元格边框的宽度 # 显示数值 # 以科学计算法显示数据
                )
   #添加标题
    plt.title(f'{lables[i]}学生停留时间热力图')
    # 显示图形
    plt.savefig('img/' + f'{lables[i]}' + '热力图.jpg')