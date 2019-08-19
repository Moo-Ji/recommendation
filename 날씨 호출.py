def weather(date, time):

    from urllib.request import Request, urlopen
    from urllib.parse import urlencode, quote_plus
    import json
    import pandas as pd


    url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib'
    queryParams = '?' + urlencode({quote_plus(
        'ServiceKey'): 'vNTq1lksHC5gAxJtE2JHfHXFsESjQxUWA7TJyvVUvX3wHAmgc9UDnLIPz94tPZRfidRUEd9Mm8fCOl4rHoakUw==',
                                   quote_plus('base_date'): date,
                                   quote_plus('base_time'): time,
                                   quote_plus('nx'): '60',
                                   quote_plus('ny'): '127',  # 60-127 서울시
                                   quote_plus('numOfRows'): '10',
                                   quote_plus('pageNo'): '1',
                                   quote_plus('_type'): 'json'})

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    my_json = response_body.decode('utf8').replace("'", '"')
    Weather = json.loads(my_json)

    # 카테고리 확인용 PYT = 강수 여부
    C = Weather["response"]["body"]["items"]["item"][0]["category"]
    # 날씨 값 #pyt = 강수 형태 0=맑음, 1 비, 2 눈비, 3 눈
    R = Weather["response"]["body"]["items"]["item"][0]["obsrValue"]

    if R == 3:
        R = 0  # 눈-> 비가 안온 날 0
    if R == 2:
        R = 1  # 진눈깨비 -> 비온날 1

    return R


weather('20190514', '1400')
## 'yyyymmdd', 'hhmm'




