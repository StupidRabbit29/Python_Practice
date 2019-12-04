import numpy as np
import pandas as pd
import time

#1.打开CSV文件
fileNameStr = 'BeijingPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr, encoding='utf-8', usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(df.head())
print(df.describe())
print(df.info())
print("================================")
#2.查看是否有缺失值
print(df.isnull().sum().sort_values(ascending=False))
print("================================")

#方案二，直接使用dataframe的方法
#3.去掉三列PM数据全部为空的行
print(df.info())
df.dropna(axis='index', how='all', subset=['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post'], inplace=True)

print("**************************")
print(df.info())

#4.计算平均值
start = time.time()
df['sum'] = df[['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']].sum(axis=1)
df['count'] = df[['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']].count(axis=1)
df['ave'] = round(df['sum']/df['count'], 2)
end = time.time()
print("---------------duration:", end-start)

#5.输出到文件
#df.to_csv("beijing_ave.csv")
print("****** done ******")

#6.按照年做汇总，查看年的平均值
# print(df.groupby("year").agg({"ave": 'mean'}))
yeargp = df.groupby("year").agg({"ave": 'mean'})
yeardf = pd.DataFrame(yeargp)
yeardf.reset_index(inplace=True)
yeardf.to_csv("beijing_year_mean.csv")
monthgp = df.groupby(["year", "month"]).agg({"ave": 'mean'})
monthdf = pd.DataFrame(monthgp)
monthdf.reset_index(inplace=True)
monthdf.to_csv("beijing_month_mean.csv")
# print(df.groupby(["year", "month"]).agg({"ave": 'mean'}))

