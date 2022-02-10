from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
ser = Service('../chromdriver/chromedriver')
driver = webdriver.Chrome(service = ser)
url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
driver.get(url)
html = driver.page_source

soup= BeautifulSoup(html, 'html.parser')
soup
# [음악/댄스], 가수명, 구독자수, view수. 동영상수
songs = soup.select('form > table > tbody > tr')
len(songs)
songs[0]
song = songs[0]
song
category = song.select('p.category')[0].text.strip()
singer = song.select('h1 > a')[0].text.strip()
subscriber = song.select('td.subscriber_cnt')[0].text.strip()
view = song.select('td.view_cnt')[0].text.strip()
video = song.select('td.video_cnt')[0].text.strip()
songs = soup.select('form > table > tbody > tr')
songs_list = []
rank = 1

for song in songs:
    category = song.select('p.category')[0].text.strip()
    singer = song.select('h1 > a')[0].text.strip()
    subscriber = song.select('td.subscriber_cnt')[0].text.strip()
    view = song.select('td.view_cnt')[0].text.strip()
    video = song.select('td.video_cnt')[0].text.strip()
    
    mylist = [rank, category, singer, subscriber, view, video]
    
    songs_list.append(mylist)
    rank += 1
    
songs_list
df_songs_list = pd.DataFrame(songs_list,
                            columns = ['rank', 'category', 'singer', 'subscriber', 'view', 'video'])

df_songs_list.to_excel("./files/youtube_rank_prac.xlsx",
                       index=False)
from matplotlib import rc, font_manager
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
df = pd.read_excel('./files/youtube_rank_prac.xlsx')
df.head()
df['category'].value_counts()
df['replaced_subscriber'] = df['subscriber'].str.replace('만','0000')
df.head()
df.info()
df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
df.info()
df.head()
pivot_df = df.pivot_table(values = 'replaced_subscriber',
              index = 'category',
              aggfunc = ['sum', 'count'])
pivot_df
pivot_df.columns = ['subscriber_sum', 'subscriber_count']
pivot_df = pivot_df.reset_index()
pivot_df.head()
pivot_df = pivot_df.sort_values(by = 'subscriber_sum',
                               ascending = False)
pivot_df = pivot_df.reset_index(drop = True)
pivot_df.head()
pivot_df.head(6)
# plt.rcParamas['fontsize'] = 10
plt.figure(figsize = (6,6))
plt.pie(pivot_df['subscriber_sum'],
       labels = pivot_df.head(6)['category'],
       autopct = '%.1f%%')

plt.show()



import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 20
ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

explodes = [0,0.1, 0, 0]
colors = ['#e042f5', '#3a24c9', '#4fed37', '#de3207']

plt.figure(figsize = (6,6))
plt.pie(ratio, labels = labels, 
       autopct = '%.1f%%', counterclock = False,
       startangle = 90, explode = explodes, shadow = True,
       colors = colors)
plt.show()





