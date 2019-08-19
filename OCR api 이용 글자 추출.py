# ocr계정생성 후 실행


import os
import io
import re
import numpy as np
import pandas as pd
from google.cloud import vision
from google.cloud.vision import types

# cmd 창에 setx GOOGLE_APPLICATION_CREDENTIALS "파일경로/파일명.json"
# 혹은 cmd 창에 set GOOGLE_APPLICATION_CREDENTIALS = "파일경로/파일명.json"
# 해서 성공 뜨면 연결된 것.


# google과 사용자를 연결하는 코드
client = vision.ImageAnnotatorClient()

# 분석하려는 이미지 파일 경로를 잡는 코드
# (os.path.dirname('파일경로'), '이미지파일명')
file_name = os.path.join(
    os.path.dirname('C:'),
    '/example/example2.jpg')

# 이미지 로드
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
image = types.Image(content=content)

# 이미지 파일에서 text를 감지
response = client.text_detection(image=image)
texts = response.text_annotations

my_list = list()

# 이미지에서 추출한 texts들 중 description만 뽑아내기
for text in texts:
    result = text.description
    my_list.append(result)

data = my_list[0]
data1 = data.replace('\n', ' ')
data2 = data1.replace('(', ' ')
data3 = data2.replace(')', ' ')
data4 = data3.replace('/', ' ')
data5 = data4.split(' ')

df = pd.DataFrame(data5, columns=["총리스트"])
df1 = pd.DataFrame(columns=["0", "1", "2", "3"])
df2 = pd.DataFrame(columns=["0", "1", "2", "3"])

df1.loc[0, '3'] = "아메리카노"
df1.loc[1, '2'] = "아이스"
df1.loc[1, '3'] = "아메리카노"
...
df1.loc[2, '2'] = "아이스"
df1.loc[2, '3'] = "카페라떼"
df1.loc[3, '3'] = "카페라떼"

# df1에 있는 파스쿠찌 모든 메뉴 한 단어로 만드는 과정 => Allmenu에 담음
menu = df1[['0', '1', '2', '3']].astype(str).sum(axis=1)
menu = menu.str.replace('nan', '')
m2 = menu.unique()
Allmenu = pd.DataFrame(m2, columns=["AllMenu"])
display(Allmenu)

for i in range(0, len(df.index)):
    for i2 in range(0, len(df1.index)):
        if df1.loc[i2, '0'] == df.loc[i, "총리스트"]:
            df2.loc[i2, '0'] = df.loc[i, "총리스트"]
        elif df1.loc[i2, '1'] == df.loc[i, "총리스트"]:
            df2.loc[i2, '1'] = df.loc[i, "총리스트"]
        elif df1.loc[i2, '2'] == df.loc[i, "총리스트"]:
            df2.loc[i2, '2'] = df.loc[i, "총리스트"]
        elif df1.loc[i2, '3'] == df.loc[i, "총리스트"]:
            df2.loc[i2, '3'] = df.loc[i, "총리스트"]

# 사진에서 추출한 텍스트 메뉴랑 비교해서 한 단어로 만들기
df3 = df2.sort_index()
match = df3[['0', '1', '2', '3']].astype(str).sum(axis=1)  # match -> array 형식 astype -> 문자로 변환
match = match.str.replace('nan', '')  # 난값을 공백
match = match.unique()  # 중복메뉴 (아이스 4개행 중복 걸러줌)
imgtxt = pd.DataFrame(match, columns=["imgtxt"])