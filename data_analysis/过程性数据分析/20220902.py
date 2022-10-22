
import pandas as pd
'''
给生成的数据表加上名字
'''
data1 = pd.read_csv("20220922.csv",converters = {'STU_CODE' : str},encoding='gbk')
data2 = pd.read_csv('A卷_转化能力值.csv',converters = {'STU_CODE' : str},encoding='gbk')
print(data2['STU_CODE'])
print(data1['STU_CODE'])
def T2(mes):
    name = data2[data2['STU_CODE'] == str(mes)[:-1]]['STU_NAME'].tolist()
    if name == []:
        return 'name'
    else:
        print(name[0])
        return name[0]
data1['NAME'] = data1.apply(lambda x: T2(x["STU_CODE"]), axis=1)
data1.to_csv("20220922_name.csv",index=None)