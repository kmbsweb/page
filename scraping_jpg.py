from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.booking.com/searchresults.ja.html?aid=397594;label=gog235jc-index-ja-XX-XX-unspec-jp-com-L%3Aja-O%3AosSx-B%3Afirefox-N%3AXX-S%3Abo-U%3Ac-H%3As;sid=adab453741ee3ee0dc162e922eb32ebf;city=-246227;from_idr=1&;ilp=1;d_dcp=1")
bs0bj = BeautifulSoup(html.read())
print(bs0bj.title)

import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート
 
URL = 'http://su-gi-rx.com' # URL入力
images = [] # 画像リストの配列
 
soup = BeautifulSoup(requests.get(URL).content,'lxml') # bsでURL内を解析

import os
os.getcwd() 
os.chdir("/Users/ksk/Desktop")

for link in soup.find_all("img"): # imgタグを取得しlinkに格納
    if link.get("src").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
        images.append(link.get("src")) # imagesリストに格納
    elif link.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
    	images.append(link.get("src")) # imagesリストに格納
 
for target in images: # imagesからtargetに入れる
    re = requests.get(target)
    with open('img/' + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
        f.write(re.content) # .contentにて画像データとして書き込む
 
print("ok") # 確認

# Rstudioで日本語がかきにくいという指摘は正しいのか？
