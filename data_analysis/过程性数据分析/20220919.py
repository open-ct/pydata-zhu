import pandas as pd
import demjson3
import csv
'''
根据生成的数据表生成每个学生每个时间节点所在的题目位置
input：数据表
output：每个学生的时间表，img_data
'''
data1 = pd.read_excel("20220822.xlsx",converters = {'ticket_id' : str,'task_answer' : str})
tickid_data = pd.read_csv("20220922_name.csv")
tickid = tickid_data['STU_CODE'].unique()

task = ['运动会问题','生活水平问题']
task_page = [8,9]
second = []
k = 0
for tick_id in tickid:
    print(k)
    k +=1
    writer = csv.writer(open('./img_data/{}.csv'.format(tick_id), 'w', newline=''))
    writer = csv.writer(open('./img_data/{}.csv'.format(tick_id), 'a', newline=''))
    writer.writerow(['page', 'time', 'current_time', 'is_change'])
    current_second = 0
    for task_name in task:
        i = 0
        h = False
        is_change = ['False' for i in range(task_page[task.index(task_name)])]
        for index, row in data1[(data1['ticket_id'] == tick_id) & (data1['task_name'] == task_name)].iterrows():
            values = demjson3.decode(
                row["task_answer"].replace("null", "{'data':{'page':0,'answer':[]},'isAnswered': false}"))
            if "null" in row["task_answer"] and h==True:
                continue
            if "null" in row["task_answer"]:
                print(row["task_answer"])
                h = True
            if i == 0:
                last_time =pd.to_datetime(row["timestamp"])
                i += 1
                last_page = values['frame']['data']['page']
                continue
            now_time = pd.to_datetime(row["timestamp"])
            cost_time = pd.to_timedelta(now_time - last_time).total_seconds()
            if i == 1:
                writer.writerow([task_name + "_" + "0", cost_time, 0, is_change[values['frame']['data']['page']]])
                current_second += cost_time
                i += 1
            else:
                if values['frame']['data']['page'] < task_page[task.index(task_name)] and cost_time < 1000 and cost_time > 0:
                    writer.writerow([task_name + "_" + str(values['frame']['data']['page']), cost_time, current_second, is_change[values['frame']['data']['page']]])
                    current_second += cost_time
            last_time = now_time
            if values['frame']['data']['page'] != last_page and values['frame']['data']['page'] < task_page[task.index(task_name)]  and last_page< task_page[task.index(task_name)] :
                is_change[last_page] = 'True'
            last_page = values['frame']['data']['page']
        last_page = 0
