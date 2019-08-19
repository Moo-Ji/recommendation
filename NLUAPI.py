import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions
import pandas as pd

# 1에서 저장한 Data.csv 파일 불러오기
Data = pd.read_csv("./data/cafe/Data.csv")
R = Data["Review"]

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='키값',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)

_list = list()
for txt in R:
    response = natural_language_understanding.analyze(text=txt, \
                                                      features=Features(sentiment=SentimentOptions())).get_result()
    _keys = response["sentiment"]["document"]["score"]
    _list.append(_keys)

Data["Review"] = _list

# NLU 수치 정규화
Data["Review"] = MinMaxScaler().fit_transform(Data[["Review"]].values)
# Data.to_csv("./data/cafe/Data.csv", header = True, index = True)

# 메뉴별로 groupby해서 평균 구하기
Data01 = Data.groupby(['Menu']).mean()
Data01["NoRain"] = 1 - Data01["Rain"]
# Data01.to_csv("./data/cafe/Data02.csv", header = True, index = True)

