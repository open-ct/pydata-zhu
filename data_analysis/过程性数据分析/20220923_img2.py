import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
'''
画图，生成群体的平均情况图
'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_csv("20220922_name.csv")
data = data[(data["NAME"]!="name")&(data["NAME"]!="ROBINCHEN")]
data2 = pd.read_csv('A卷_转化能力值.csv',converters = {'STU_CODE':str},encoding='gbk')
high_level = data2[data2['IRT_ZHUANHUA'] >= 1]['STU_CODE'].values
middle_level = data2[(data2['IRT_ZHUANHUA'] < 1) & (data2['IRT_ZHUANHUA'] > -1)]['STU_CODE'].values
low_level = data2[data2['IRT_ZHUANHUA'] <= -1]['STU_CODE'].values

high_data_frame = data[data['STU_CODE'].str[:-1].isin(high_level)]
middle_data_frame = data[data['STU_CODE'].str[:-1].isin(middle_level)]
low_data_frame = data[data['STU_CODE'].str[:-1].isin(low_level)]

for i, r in high_data_frame.iteritems():
    if i !="STU_CODE" and i != "NAME":
        high_data_frame = high_data_frame[(high_data_frame[i] > -1)]
for i, r in middle_data_frame.iteritems():
    if i !="STU_CODE" and i != "NAME":
        middle_data_frame = middle_data_frame[(middle_data_frame[i] > -1)]
for i, r in low_data_frame.iteritems():
    if i !="STU_CODE" and i != "NAME":
        low_data_frame = low_data_frame[(low_data_frame[i] > -1)]
high_data_frame = high_data_frame.mean(axis=0)
high_data_frame.drop('Time_Sport_P0', inplace=True)
high_data_frame.drop('Time_Life_P0', inplace=True)
high_value = high_data_frame.values
low_data_frame = low_data_frame.mean(axis=0)
low_data_frame.drop('Time_Sport_P0', inplace=True)
low_data_frame.drop('Time_Life_P0', inplace=True)
low_value = low_data_frame.values
middle_data_frame = middle_data_frame.mean(axis=0)
middle_data_frame.drop('Time_Sport_P0', inplace=True)
middle_data_frame.drop('Time_Life_P0', inplace=True)
middle_value = middle_data_frame.values
index = [[1,14],[14,27],[27,40],[40,53],[53,66],[66,79]]
barWidth = 0.3
r1 = np.arange(13)
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
# data.fillna(0.1,inplace=True)
label = data.index
plt.figure(1,figsize=(20,12))
plt.bar(r1, low_value[index[0][0]:index[0][1]], color='red', width=barWidth, edgecolor='white', label='每题平均作答时间')
plt.bar(r2, low_value[index[3][0]:index[3][1]], color='blue', width=barWidth, edgecolor='white', label='每题平均阅题时间')
plt.bar(r3, low_value[index[4][0]:index[4][1]], color='yellow', width=barWidth, edgecolor='white', label='每题平均检查时间')

for a, b in zip(r1, low_value[index[0][0]:index[0][1]]):
    plt.text(a, b + 0.05, '%.1f' % b, ha='center', va='bottom', fontsize=10)
for a, b in zip(r2, low_value[index[3][0]:index[3][1]]):
    plt.text(a, b + 0.05, '%.1f' % b, ha='center', va='bottom', fontsize=10)
for a, b in zip(r3, low_value[index[4][0]:index[4][1]]):
    plt.text(a, b + 0.05, '%.1f' % b, ha='center', va='bottom', fontsize=10)
plt.xlabel('题目')
plt.ylabel('时间',fontsize=18)
plt.legend(loc=1, bbox_to_anchor=(0.12,0.99),borderaxespad = 0.)
plt.ylim([0,1800])

plt.twinx()
sorts = ['生活水平问题_7','生活水平问题_6','生活水平问题_5','生活水平问题_4','生活水平问题_3','生活水平问题_2',
                                             '生活水平问题_1','运动会问题_6','运动会问题_5','运动会问题_4','运动会问题_3',
                                             '运动会问题_2','运动会问题_1'][::-1]
plt.xticks([r + barWidth for r in range(13)], sorts,rotation=45)

plt.plot(r1, low_value[index[1][0]:index[1][1]],color='green',linewidth=1,linestyle='--',marker='o',markersize=3,label=u'每题平均修改次数')
plt.plot(r1, low_value[index[2][0]:index[2][1]],color='red',linewidth=1,linestyle='--',marker='o',markersize=3,label=u'每题平均停留次数')
plt.plot(r1, low_value[index[5][0]:index[5][1]],color='blue',linewidth=1,linestyle='--',marker='o',markersize=3,label=u'每题平均返回修改次数')
for a, b in zip(r1, low_value[index[1][0]:index[1][1]]):
    plt.text(a, b + 0.05, '%.1f' % b, ha='center', va='bottom', fontsize=10)
for a, b in zip(r2, low_value[index[2][0]:index[2][1]]):
    plt.text(a, b + 0.05, '%.1f' % b, ha='center', va='bottom', fontsize=10)
for a, b in zip(r3, low_value[index[5][0]:index[5][1]]):
    plt.text(a, b + 0.05, '%.1f' % b, ha='center', va='bottom', fontsize=10)

plt.ylabel('次数', fontsize=18)
# 图列
plt.legend(loc=2, bbox_to_anchor=(0.86, 0.99), borderaxespad=0.)
plt.ylim([0, 35])
plt.title('低分学生汇总图')
plt.grid(True)
# plt.show()
plt.savefig(f'img/average_img/低分学生汇总图.jpg')

