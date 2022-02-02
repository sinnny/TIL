import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("", encoding='cp949')
data
pd.options.display.float_format = '{:.2f}'.format

data
data.columns
data.describe()
data.value_counts()
df=data.groupby(by=['crym', 'tco_btc_nm']).sum()
df
data['tco_btc_nm'].unique()
df_menu = df.groupby(level=1).sum()
df_menu
total_krw = df['tco_btc_u_am'].sum()
total_krw
total_counts = df['tco_btc_u_ct'].sum()
total_counts
df_pmenu = DataFrame(df_menu['tco_btc_u_am'] / total_krw * 100)
df_pmenu = df_pmenu.rename(columns={'tco_btc_u_am':'ratio_krw'})
df_pmenu
import matplotlib
from matplotlib import font_manager, rc
import platform

try : 
    if platform.system() == 'Windows':
    # 윈도우인 경우
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else:    
    # Mac 인 경우
        rc('font', family='AppleGothic')
except : 
    pass
matplotlib.rcParams['axes.unicode_minus'] = False  
df_menu = df.groupby(level=1).sum()
df_menu = df_menu.reset_index()
df_menu
data1 = pd.concat([df_menu, df_pmenu], axis=1)
data1
data1 = data1.rename(columns={'tco_btc_nm':'카테고리', 'tco_btc_u_ct':'결제건수', 'tco_btc_u_am':'결제금액', 'ratio_krw':'결제금액비율'})
data1
data1 = data1.drop(['ma_fem_dc', 'agegrp_dc'], axis=1)
data1



fm_data = data['ma_fem_dc'].astype(str)
fm_data = pd.DataFrame(fm_data.replace("1","남성").replace("2","여성"))
fm_data = fm_data.rename(columns= {'ma_fem_dc':'성별'})
fm_data
fm_data = pd.concat([data,fm_data], axis=1)
fm_data.head()
data_1 = data['agegrp_dc'].astype(str)
data_1 = pd.DataFrame(data_1.replace("1","10대미만").replace("10","10대").replace("20","20대").replace("30","30대").replace("40","40대").replace("50","50대").replace("60","60대").replace("70","70대").replace("80","80대").replace("90","90대"))
data_1 = data_1.rename(columns= {'agegrp_dc':'연령별'})
data_1 


data_1 = pd.concat([fm_data, data_1], axis=1)
data_1
data_1 = data_1.groupby(by=['tco_btc_nm', '성별']).count()
data_1
data2 = data_1.iloc[:,[1]]
data2.rename = ({'tco_btc_nm'})
sns.barplot(data=df_menu, x="tco_btc_nm", y="tco_btc_u_ct", hue="tco_btc_nm")

plt.figure(figsize=(7,7))
plt.pie(data_c['ratio_krw'], 
       labels=data_c['tco_btc_nm'],
       autopct='%.2f%%',
       colors=sns.color_palette('hls'),
       textprops={'fontsize':8})
plt.title("업종별 매출 비율", fontsize=10)
plt.subplots(data_c['ratio_krw'], 
       labels=data_c['tco_btc_nm'],
       autopct='%.2f%%',
       colors=sns.color_palette('hls'),
       textprops={'fontsize':8})





df_menu.to_excel("/Users/shinhee/Desktop/df_menu.xlsx")



