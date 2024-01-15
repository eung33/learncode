# World Economic Outlook Data Analysis
Data Source : IMF
import pandas as pd
df = pd.read_csv('WEOApr2020all.csv')
df.head(3)
df.describe()
df.columns
type(df)
df['Country'].nunique()
df.iloc[:,::3]
df['Subject Descriptor'].head(7)
df[['Country','Subject Descriptor','2020']]
# Inflation
idx_inf = df['Subject Descriptor'].str.contains('Inflation, end of')
print(idx_inf)
df.loc[idx_inf]
df_inf = df[idx_inf]
df_inf.head(3)
df_inf_2021 = df_inf[['Country','2021']]
df_inf_2021
df_inf_2021.reset_index(drop=True, inplace=True)
df_inf_2021

df_inf_2021.dtypes
df_inf_2021.info()
# get only non-null data type
df_inf_2021 = df_inf_2021.loc[df_inf_2021['2021'].notnull()]
df_inf_2021
df_inf_2021.info()
df_inf_2021 = df_inf_2021.replace(',','',regex=True)
df_inf_2021
# change to numeric
df_inf_2021['2021'] = pd.to_numeric(df_inf_2021['2021'])
df_inf_2021
df_inf_2021.info()
# plot bar graph
df_inf_2021.sort_values('2021').plot.bar(x='Country')
df_inf_2021.sort_values('2021').iloc[0:20,:].plot.bar(x='Country')
# Unemployment Rate
df_ur = df[ df['Subject Descriptor'].str.contains('Unemployment')][['Country','2021']]
df_ur
df_ur.info()
df_ur = df_ur.loc[df_ur['2021'].notnull()]
df_ur.info()
df_ur.reset_index(drop=True, inplace=True)
df_ur
df_ur.info()
df_ur['2021'] = pd.to_numeric(df_ur['2021'])
df_ur
df_ur.info()
df_ur.plot.bar(x='Country')
df_ur.sort_values('2021', ascending=False).plot.bar(
    x='Country', 
    title='Unemployment Rate', 
    figsize=(15,5)
    )
df_ur_numpy = df_ur.sort_values('2021', ascending=False).to_numpy()
print(df_ur_numpy)
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['figure.figsize'] =(20,3)
plt.xticks(rotation='vertical')
plt.bar(df_ur_numpy[:,0], df_ur_numpy[:,1])
plt.title("2021 Unemployment Rate - IMF World Eonomic Outlook Database, April 2020")
# color on Korea
idx = np.where(df_ur_numpy == 'Korea')
plt.bar(df_ur_numpy[idx[0],0], df_ur_numpy[idx[0], 1], label = 'Korea')
# color on United States
idx = np.where(df_ur_numpy == 'United States')
plt.bar(df_ur_numpy[idx[0],0], df_ur_numpy[idx[0], 1], label = 'United States')
# color on China
idx = np.where(df_ur_numpy == 'China')
plt.bar(df_ur_numpy[idx[0],0], df_ur_numpy[idx[0], 1], label = 'China')
plt.legend()
df.head(3)
len(df.columns)
idx = list(range(0,52))
print(idx)
idx[3]=0
idx[0]=3
print(idx) 
df.iloc[:,idx] # 순서가 바뀐 idx 값을 인자로 받음
# Add new column and group analysis
df_ur
df_ur['Criteria'] = 'NONE'
df_ur
df_ur.loc[df_ur['2021'] < 5, 'Criteria'] = 'Low'
df_ur.loc[(df_ur['2021'] >= 5) & (df_ur['2021'] < 10), 'Criteria'] = 'Medium'
df_ur.loc[df_ur['2021'] >= 10, 'Criteria'] = 'High'
df_ur
df_ur.groupby(['Criteria']).mean()
df_ur.groupby(['Criteria']).mean().sort_values('2021')
df_ur.groupby(['Criteria']).count()
for df_chunk in pd.read_csv('WEOApr2020all.csv', chunksize=5):
    print(df_chunk)

df_new = pd.DataFrame(columns=df.columns)
df_new
for df_chunk in pd.read_csv('WEOApr2020all.csv', chunksize=5):
    temp = df_chunk.loc[ df_chunk['Subject Descriptor'] == 'Unemployment rate']
    df_new = pd.concat([df_new, temp])
df_new






df_sang = df[df['StartPoint'] == 'GYEONGSANG']['Gyeonggi']
from scipy import stats
ans2_1 = stats.ttest_ind(df_gi, df_sang)
ans2_2 = "YES" if ans2_1.pvalue <= 0.05 else "NO"
print( {round(ans2_1.pvalue, 4)}, {ans2_2})


import matplotlib.pyplot as plt 
plt.plot(df[1])


import matplotlib.pyplot as plt 
df2[['일자', '종가']].plot()
plt.show()


Don't you care about your background
when you start a video conference outside of the office?
Now, with Knox Meeting's "virtual background" feature,
you can be more immersed in your conference while keeping your privacy.

1. Before joining
   Click "Turn on virtual background" at the top right of the settings pop-up
2. After joining
   Click "Settings" at the bottom left > check "Using virtual background"
※ Virtual background in VDI/RBS will be supported in the future.

013938 02 192121

202-01-035342



eksctl create cluster --name team5 --version 1.21 --nodegroup-name standard-workers --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 3
 
aws eks --region ap-southeast-2 update-kubeconfig --name cluster-team5
kubectl get all
# 클러스터 설정확인
kubectl config current-context


kubectl autoscale deployment reservation --cpu-percent=20 --min=1 --max=3
kubectl autoscale deployment rentcarmanage --cpu-percent=20 --min=1 --max=3
kubectl autoscale deployment payment --cpu-percent=20 --min=1 --max=3
kubectl autoscale deployment viewpage --cpu-percent=20 --min=1 --max=3

siege -c20 -t40S -v http://reservation:8080/reserves

siege -c20 -t40S -v http://reservation:8080/reserves


viewpage


pks1411

구글 
카카오








