
# coding: utf-8

# In[2]:


print('Hello world')


# In[12]:


from __future__ import print_function
student_data = [
    {'name': 'Bob', 'id':0, 'scores':[68,75,56,81]},
    {'name': 'Yui', 'id':1, 'scores':[68,75,56,81]}, 
    {'name': 'Mike', 'id':2, 'scores':[68,75,56,81]},
]


# In[14]:


student_data


# In[20]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('pylab', 'inline --no-import-all')
x = np.arange(-3, 3, 0.1)
y = np.sin(x)
plt.plot(x, y)


# In[22]:


x = np.random.randn(30)
y = np.sin(x) + np.random.randn(30)
plt.plot(x, y, "o")  # "o"は小さい円(circle marker)


# In[25]:


pip install pandas
pip install folium


# In[32]:


# -*- coding:utf-8 -*-
# pythonでfoliumを利用する際のサンプル
import folium
# 地図の基準として兵庫県明石市を設定
japan_location = [35, 135]
# 基準地点と初期の倍率を指定し、地図を作成する
map = folium.Map(location=japan_location, zoom_start=5)
# 基準地点にマーカーを設置するs
marker = folium.Marker(japan_location, popup='Akashi')
map.add_children(marker)


# In[33]:


japan_location


# In[38]:


import folium
# 地図の基準として兵庫県明石市を設定
japan_location = [35, 135]
# 基準地点と初期の倍率を指定し、地図を作成する
map = folium.Map(location=japan_location, zoom_start=5)
# 基準地点にマーカーを設置するs
marker = folium.Marker(japan_location, popup='Akashi')
map.add_child(marker)
map.save(outfile="map.html")


# In[40]:


import numpy as np
import pandas as pd
from sklearn import datasets

import matplotlib.pyplot as plt
import matplotlib.cm as cm
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

sns.set(style="darkgrid", palette="muted", color_codes=True) 


# In[42]:


# irisデータのロード
iris = datasets.load_iris()


# In[44]:


# 散布図の表示（色が白黒になってしまう・・・）
plt.figure(figsize=(10,7))
plt.scatter(iris.data[:,0], iris.data[:,1], linewidths=0, alpha=1,
            c=iris.target   # iris.targetには種別を表す[0, 1, 2]が入っているのでそれで色分け
           )
plt.show()


# In[46]:


# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
 
#対象ページへアクセス
res = requests.get('http://gigazine.net/')
content = res.content
 
#スクレイピングしたページデータを整形する
soup = BeautifulSoup(content, 'html.parser')
 
# タイトル要素を取得する
title_tag = soup.title
 
# 要素の文字列を取得する
title = title_tag.string
 
# タイトル要素を出力
print(title_tag)
 
# タイトルを文字列を出力
print(title)


# In[49]:


soup

