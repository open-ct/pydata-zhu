import pandas as pd
import demjson3
data1 = pd.read_excel("文化A卷整理.xlsx",converters = {'ticket_id' : str})
data3 = pd.read_excel("文化Z卷整理.xlsx",converters = {'ticket_id' : str})
data2 = pd.read_csv("678.csv", encoding="utf-8",converters={'ticket_id' : str})
# mid_data = pd.read_csv("mid_data.csv")
# data2_1 = pd.read_excel("ticket_log_PBL_testing3—过程数据.xlsx",sheet_name="Result 1")
# data2_2 = pd.read_excel("ticket_log_PBL_testing3—过程数据.xlsx",sheet_name="Result 2")
# data2_3 = pd.read_excel("ticket_log_PBL_testing3—过程数据.xlsx",sheet_name="Result 3")
# data2_4 = pd.read_excel("ticket_log_PBL_testing3—过程数据.xlsx",sheet_name="Result 4")
# #
# frames = []
# frames.append(data2_1)
# print(1)
# frames.append(data2_2)
# print(2)
# frames.append(data2_3)
# print(3)
# frames.append(data2_4)
# print(4)
# data2 = pd.concat(frames)
# print(5)
# data2.drop(index = data2[(data2['ticket_id']== '140702141110821')].index.tolist(),inplace=True)
# data2.drop(index = data2[(data2['ticket_id']== '330300211060121')].index.tolist(),inplace=True)
# data2.drop(index = data2[(data2['ticket_id']== '330300181090121')].index.tolist(),inplace=True)
# data2.drop(index = data2[(data2['ticket_id']== '330300141123521')].index.tolist(),inplace=True)

# data2.to_csv("3456.csv",index = None)
# data2.drop(index = data2[(data2['task_name']== '导言')].index.tolist(),inplace=True)
# data2.drop(index = data2[(data2['task_name']== '热身题【本题不计入总分】')].index.tolist(),inplace=True)
# data2.drop(index = data2[(data2['task_name']== '生活水平问题')].index.tolist(),inplace=True)
# data2.drop(index = data2[(data2['task_name']== '运动会问题')].index.tolist(),inplace=True)
# data2.drop(index = data2[(data2['task_name']== '【后测版】刷牙问题')].index.tolist(),inplace=True)
# data2.to_csv("678.csv",columns=["timestamp","ticket_id","task_name","task_answer"],index=None,encoding="utf-8")
# data2['task_answer'] = data2['task_answer'].str.replace(' ','')
global null
null = ""
global false
false = ""
global true
true = ""


def T2(mes):
    print(mes)
    if pd.isnull(mes):
        return 0
    if 'basic' in demjson3.decode(mes):
        return len(demjson3.decode(mes)["basic"][-1])
    else:
        return 0
# mid_data = data2.loc[lambda data2 :(data2["task_name"]=="学习区：神话与民族精神") | (data2["task_name"]=="场景一")|(data2["task_name"]=="创作区：神话与文化创新"),:]
# mid_data['basic'] = mid_data.apply(lambda x: T2(x["task_answer"]), axis=1)
mid_data = pd.read_csv("mid_data.csv",encoding="utf-8",converters={'ticket_id' : str})
for i in range(len(data1)):
    print(i)
    if data1.loc[i]["start_time"] == None or data1.loc[i]["stop_time"] == None:
        row_index = data2[data2['ticket_id'] == data1.loc[i]['ticket_id']].index.tolist()
        data1.loc[i]["start_time"] = pd.to_datetime(data2.loc[row_index[0]]["timestamp"])
        data1.loc[i]["stop_time"] = pd.to_datetime(data2.loc[row_index[-1]]["timestamp"])
        data1.loc[i]["cost_time"] = pd.to_timedelta(data1.loc[i]["stop_time"] - data1.loc[i]["start_time"]).total_seconds()
    row_index1 = data2[(data2['task_name'] == '穿越区：神话与远古先民') & (data2['ticket_id'] == data1.loc[i]['ticket_id'])].index.tolist()
    row_index2 = mid_data[(mid_data['basic'] == 0) & (mid_data['task_name'] == '学习区：神话与民族精神')& (mid_data['ticket_id'] == data1.loc[i]['ticket_id'])].index.tolist()
    row_index3 = mid_data[mid_data['basic'] > 0 & (mid_data['task_name'] == '学习区：神话与民族精神')& (mid_data['ticket_id'] == data1.loc[i]['ticket_id'])].index.tolist()
    row_index4 = data2[(data2['task_name'] == '辩论区：神话与当代传承') & (data2['ticket_id'] == data1.loc[i]['ticket_id'])].index.tolist()
    row_index5 = mid_data[(mid_data['task_name'] == '创作区：神话与文化创新')& (mid_data['ticket_id'] == data1.loc[i]['ticket_id'])].index.tolist()
    row_index6 = mid_data[(mid_data['basic'] > 0) & (mid_data['task_name'] == '创作区：神话与文化创新')& (mid_data['ticket_id'] == data1.loc[i]['ticket_id'])].index.tolist()
    if len(row_index1) > 0:
        data1.at[i,"T1_strat_time"] = pd.to_datetime(data2.loc[row_index1[0]]["timestamp"])
        data1.at[i,"T1_stop_time"] = pd.to_datetime(data2.loc[row_index1[-1]]["timestamp"])
        data1.at[i,"T1_cost_time"] = pd.to_timedelta(data1.loc[i]["T1_stop_time"] - data1.loc[i]["T1_strat_time"]).total_seconds()
    if len(row_index2) >0 :
        data1.at[i,"T2_strat_time"] = pd.to_datetime(mid_data.loc[row_index2[0]]["timestamp"])
        data1.at[i,"T2_stop_time"] = pd.to_datetime(mid_data.loc[row_index2[-1]]["timestamp"])
        data1.at[i,"T2_cost_time"] = pd.to_timedelta(data1.loc[i]["T2_stop_time"] - data1.loc[i]["T2_strat_time"]).total_seconds()
    if len(row_index3) >0 :
        data1.at[i,"T3_strat_time"] = pd.to_datetime(mid_data.loc[row_index3[0]]["timestamp"])
        data1.at[i,"T3_stop_time"] = pd.to_datetime(mid_data.loc[row_index3[-1]]["timestamp"])
        data1.at[i,"T3_cost_time"] = pd.to_timedelta(data1.loc[i]["T3_stop_time"] - data1.loc[i]["T3_strat_time"]).total_seconds()
    if len(row_index4) >0 :
        data1.at[i, "T4_strat_time"] = pd.to_datetime(data2.loc[row_index4[0]]["timestamp"])
        data1.at[i, "T4_stop_time"] = pd.to_datetime(data2.loc[row_index4[-1]]["timestamp"])
        data1.at[i, "T4_cost_time"] = pd.to_timedelta(
            data1.loc[i]["T4_stop_time"] - data1.loc[i]["T4_strat_time"]).total_seconds()
    if len(row_index5) > 0 and len(row_index6) > 0 :
        data1.at[i, "T5_strat_time"] = pd.to_datetime(data2.loc[row_index5[0]]["timestamp"])
        data1.at[i, "T5_stop_time"] = pd.to_datetime(data2.loc[row_index6[0]]["timestamp"])
        data1.at[i, "T5_cost_time"] = pd.to_timedelta(
            data1.loc[i]["T5_stop_time"] - data1.loc[i]["T5_strat_time"]).total_seconds()
        data1.at[i, "T6_strat_time"] = pd.to_datetime(data2.loc[row_index6[0]]["timestamp"])
        data1.at[i, "T6_stop_time"] = pd.to_datetime(data2.loc[row_index6[-1]]["timestamp"])
        data1.at[i, "T6_cost_time"] = pd.to_timedelta(
            data1.loc[i]["T6_stop_time"] - data1.loc[i]["T6_strat_time"]).total_seconds()
data1.to_csv('1-1.csv',index = None)
for i in range(len(data3)):
    print(i)
    if pd.isnull(data3.loc[i]["start_time"]) or pd.isnull(data3.loc[i]["stop_time"]):
        row_index = data2[data2['ticket_id'] == data3.loc[i]['ticket_id']].index.tolist()
        if len(row_index)>0:
            data3.at[i,"start_time"] = pd.to_datetime(data2.loc[row_index[0]]["timestamp"])
            data3.at[i,"stop_time"] = pd.to_datetime(data2.loc[row_index[-1]]["timestamp"])
    data3.at[i,"cost_time"] = pd.to_timedelta(pd.to_datetime(data3.loc[i]["stop_time"]) - pd.to_datetime(data3.loc[i]["start_time"])).total_seconds()
    row_index1 = mid_data[(mid_data['basic'] > 0) & (mid_data['task_name'] == '场景一') & (mid_data['ticket_id'] == data3.loc[i]['ticket_id'])].index.tolist()
    row_index0 = data2[(data2['task_name'] == '场景一') & (data2['ticket_id'] == data3.loc[i]['ticket_id'])].index.tolist()
    row_index2 = data2[(data2['task_name'] == '场景二') & (data2['ticket_id'] == data3.loc[i]['ticket_id'])].index.tolist()
    if len(row_index1) > 0:
        data3.at[i,"T1_strat_time"] = pd.to_datetime(data2.loc[row_index0[0]]["timestamp"])
        data3.at[i,"T1_stop_time"] = pd.to_datetime(mid_data.loc[row_index1[0]]["timestamp"])
        data3.at[i,"T1_cost_time"] = pd.to_timedelta(data3.loc[i]["T1_stop_time"] - data3.loc[i]["T1_strat_time"]).total_seconds()
        data3.at[i,"T2_strat_time"] = pd.to_datetime(mid_data.loc[row_index1[0]]["timestamp"])
        data3.at[i,"T2_stop_time"] = pd.to_datetime(mid_data.loc[row_index1[-1]]["timestamp"])
        data3.at[i,"T2_cost_time"] = pd.to_timedelta(data3.loc[i]["T2_stop_time"] - data3.loc[i]["T2_strat_time"]).total_seconds()
    if len(row_index2) > 0:
        data3.at[i,"T3_strat_time"] = pd.to_datetime(data2.loc[row_index2[0]]["timestamp"])
        data3.at[i,"T3_stop_time"] = pd.to_datetime(data2.loc[row_index2[-1]]["timestamp"])
        data3.at[i,"T3_cost_time"] = pd.to_timedelta(data3.loc[i]["T3_stop_time"] - data3.loc[i]["T3_strat_time"]).total_seconds()

data3.to_csv('2-1.csv',index = None)


