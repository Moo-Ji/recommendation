import numpy as np
import pandas as pd
import datetime

#1. 크롤링한 결과 csv 파일로 불러오기
df = pd.read_csv("./data/cafe/clawringexample_06_True.csv")

#2. 메뉴 결측값 제거
df = df.dropna(axis=0)  # 값이 없는 행 모두 제거

#3. 메뉴 별 리뷰 분리(메뉴 3개 시켰다면 메뉴 하나씩으로 행 구분)
df = \
    (df.set_index(df.columns.drop('Menu', 1).tolist())
         .Menu.str.split(',', expand=True)
         .stack()
         .reset_index()
         .rename(columns={0: 'Menu'})
         .loc[:, df.columns]
         )

#4. 메뉴 이름 외 값 제거
df[['Menu', 'Option']] = df.Menu.str.split("/", expand=True)
del df['Option']
df[['Menu', 'Option']] = df.Menu.str.split("（", expand=True)
del df['Option']

#5. 정리된 데이터프레임(df)에서 우리가 필요한 컬럼만 불러오기
df = df[["Restaurant", "Menu", "Review", "Total", "Taste", "Quantity", "Date"]]
# Date가 문자열로 되어있는데 날짜 데이터로 변환하기
df["Date"] = pd.to_datetime(df["Date"])

#6. 기상청에서 다운받은 날짜별 날씨 데이터로 비여부 판단
# AvgTemp : 평균기온 / RainDuration : 강수지속시간(일)
# RainMaxHour : 1시간 최대 강수량 / RainAday : 일강수량
w = pd.read_csv("./data/cafe/weather.csv")

# 문자로 되어있는 Date의 데이터를 날짜 형식으로 바꾸기
w["Date"] = pd.to_datetime(w["Date"])
w = pd.DataFrame(w, columns=["Date", "AvgTemp", "RainDuration", "RainMaxHour", "RainAday", "Rain"])

# 비오는 기준(임의로 정함)
# 강수지속시간(일)>3(시간) or 1시간 최대 강수량>=5(mm) or 일강수량>=5(mm) -> 비온날 True
w["Rain"] = (w["RainDuration"]) > 3 | (w["RainDuration"] >= 5) | (w["RainAday"] >= 5)

#7. 크롤링 데이터와 날씨 데이터를 Date 컬럼을 기준으로 합침
data = pd.merge(df, w, on="Date", how="inner")
data2 = data[["Date", "Restaurant", "Menu", "Review", "Taste", "Quantity", "Rain"]]
data3 = data2.sort_values(by="Date", axis=0, ascending=False, inplace=False)

#8. 크롤링 + 비여부 판단 데이터 최종 (띄어쓰기 제거 모든 메뉴 한 단어로 만들기)
menu_list = []
for i in (data3["Menu"]):
    menu_list.append(i.replace(' ', ''))

data3["Menu"] = menu_list

# 9. 메뉴별 빈도수 구해보기
data4 = data3.groupby(["Menu"]).count()['Total']
Menu_in_Rv = pd.DataFrame(data4)
Menu_in_Rv.reset_index(level=['Menu'], inplace=True)
# Menu_in_Rv.to_csv("./data/cafe/Menu_in_Rv.csv", header = True, index = False)