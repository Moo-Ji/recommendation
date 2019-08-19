from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
import cx_Oracle
import os
import io
import re
import pandas as pd
from google.cloud import vision
from google.cloud.vision import types



def index(request):
	candidates = Candidate.objects.all() #Candidate에 있는 모든 객체를 불러옵니다
	str01 ="" #마지막에 return해 줄 문자열입니다.
	for candidate in candidates:
		str01 += candidate.name #<P>는 html에서 단락을 바꾸기 위해 쓰입니다.
		str01 += str(candidate.party_number)
		str01 += str(candidate.image_file)
	return HttpResponse(str01)


def index01(request):
	candidate = Candidate.objects.all()

	no1 = Candidate.objects.filter(party_number = 1)
	no1[0].party_number 
	image_db01=no1[0].image_file

	image_db=str(image_db01)
	client = vision.ImageAnnotatorClient()
	    
	file_name = os.path.join(
	        os.path.dirname('C:'), 
	                            '/Users/student/mysite02/media/'+image_db)

	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)


	response = client.text_detection(image=image)
	texts = response.text_annotations
	    
	my_list = list()

	for text in texts:
	    result = text.description
	    my_list.append(result)
	    
	data = my_list[0]

	data1 = data.replace('\n',' ')
	data2 = data1.replace('(',' ')
	data3 = data2.replace(')',' ')
	data4 = data3.replace('/',' ')
	data5 = data4.split(' ')

	df = pd.DataFrame(data5, columns=["총리스트"])
	df1 = pd.DataFrame(columns=["1","2","3","4"])
	df2 = pd.DataFrame(columns=["1","2","3","4"])

	df1.loc[0, '3'] ="아메리카노"
	df1.loc[1, '2'] ="아이스"
	df1.loc[1, '3'] ="아메리카노"
	df1.loc[2, '2'] ="아이스"
	df1.loc[2, '3'] ="카페라떼"
	df1.loc[3, '3'] ="카페라떼"
	df1.loc[4, '1'] ="아이스"
	df1.loc[4, '2'] ="바닐라라떼"
	df1.loc[4, '3'] ="마끼아또"
	df1.loc[5, '1'] ="아이스"
	df1.loc[5, '2'] ="카라멜라떼"
	df1.loc[5, '3'] ="마끼아또"
	df1.loc[6, '2'] ="카라멜라떼"
	df1.loc[6, '3'] ="마끼아또"
	df1.loc[7, '3'] ="마끼아또"
	df1.loc[7, '2'] ="라떼"
	df1.loc[7, '1'] ="카라멜"
	df1.loc[8, '2'] ="바닐라라떼"
	df1.loc[8, '3'] ="마끼아또"
	df1.loc[9, '1'] ="바닐라"
	df1.loc[9, '2'] ="라떼"
	df1.loc[9, '3'] ="마끼아또"
	df1.loc[10, '1'] ="화이트초콜릿"
	df1.loc[10, '2'] ="라떼"
	df1.loc[10, '3'] ="마끼아또"
	df1.loc[11, '3'] ="카푸치노"
	df1.loc[12, '2'] ="헤이즐넛"
	df1.loc[12, '3'] ="카푸치노"
	df1.loc[13, '2'] ="오리지널"
	df1.loc[13, '3'] ="드립커피"
	df1.loc[14, '1'] ="아이스"
	df1.loc[14, '2'] ="오리지널"
	df1.loc[14, '3'] ="드립커피"
	df1.loc[15, '2'] ="카페"
	df1.loc[15, '3'] ="모카"
	df1.loc[16, '3'] ="카페모카"
	df1.loc[17, '2'] ="아이스"
	df1.loc[17, '3'] ="카페모카"
	df1.loc[18, '2'] ="화이트초콜릿라떼"
	df1.loc[18, '3'] ="마끼아또"
	df1.loc[19, '1'] ="아이스"
	df1.loc[19, '2'] ="화이트초콜릿라떼"
	df1.loc[19, '3'] ="마끼아또"
	df1.loc[20, '2'] ="콜드브루"
	df1.loc[20, '3'] ="아메리카노"
	df1.loc[21, '2'] ="콜드브루"
	df1.loc[21, '3'] ="원액"
	df1.loc[22, '2'] ="니트로"
	df1.loc[22, '3'] ="콜드브루"
	df1.loc[23, '2'] ="콜드브루"
	df1.loc[23, '3'] ="라떼"
	df1.loc[24, '3'] ="그라니따"
	df1.loc[24, '2'] ="콘파나"
	df1.loc[24, '1'] ="모카"
	df1.loc[25, '1'] ="카라멜"
	df1.loc[25, '2'] ="콘파나"
	df1.loc[25, '3'] ="그라니따"
	df1.loc[26, '3'] ="그라니따"
	df1.loc[26, '2'] ="망고요거트"
	df1.loc[27, '3'] ="그라니따"
	df1.loc[27, '2'] ="요거트"
	df1.loc[27, '1'] ="망고"
	df1.loc[28, '3'] ="그라니따"
	df1.loc[28, '2'] ="플레인요거트"
	df1.loc[29, '3'] ="그라니따"
	df1.loc[29, '1'] ="플레인"
	df1.loc[29, '2'] ="요거트"
	df1.loc[30, '3'] ="그라니따"
	df1.loc[30, '2'] ="자바칩민트"
	df1.loc[31, '3'] ="그라니따"
	df1.loc[31, '2'] ="에스프레소콘파나"
	df1.loc[32, '3'] ="그라니따"
	df1.loc[32, '2'] ="콘파나"
	df1.loc[32, '1'] ="에스프레소"
	df1.loc[33, '3'] ="그라니따"
	df1.loc[33, '2'] ="스트로베리요거트"
	df1.loc[34, '3'] ="그라니따"
	df1.loc[34, '2'] ="요거트"
	df1.loc[34, '1'] ="스트로베리"
	df1.loc[35, '3'] ="그라니따"
	df1.loc[35, '2'] ="스트로베리"
	df1.loc[36, '3'] ="그라니따"
	df1.loc[36, '2'] ="블루베리요거트"
	df1.loc[37, '3'] ="그라니따"
	df1.loc[37, '2'] ="요거트"
	df1.loc[37, '1'] ="블루베리"
	df1.loc[38, '3'] ="그라니따"
	df1.loc[38, '2'] ="복숭아"
	df1.loc[39, '3'] ="그라니따"
	df1.loc[39, '2'] ="그린티"
	df1.loc[40, '3'] ="그라니따"
	df1.loc[40, '2'] ="찰인절미"
	df1.loc[40, '1'] ="레드빈"
	df1.loc[41, '3'] ="그라니따"
	df1.loc[41, '2'] ="흑임자"
	df1.loc[41, '1'] ="레드빈"
	df1.loc[42, '3'] ="레드빈흑임자그라니따"
	df1.loc[43, '3'] ="그라니따"
	df1.loc[43, '2'] ="쑥"
	df1.loc[43, '1'] ="레드빈"
	df1.loc[44, '3'] ="레드빈쑥그라니따"
	df1.loc[45, '3'] ="그라니따"
	df1.loc[45, '2'] ="민트"
	df1.loc[45, '1'] ="레몬"
	df1.loc[46, '3'] ="그라니따"
	df1.loc[46, '2'] ="민트"
	df1.loc[46, '1'] ="자바칩"
	df1.loc[47, '3'] ="아이스티"
	df1.loc[48, '3'] ="아이스티"
	df1.loc[48, '2'] ="라즈베리"
	df1.loc[49, '3'] ="아이스티"
	df1.loc[49, '2'] ="복숭아"
	df1.loc[50, '3'] ="그린티라떼"
	df1.loc[50, '2'] ="아이스"
	df1.loc[51,'1']="아이스"
	df1.loc[51,'2']="그린티"
	df1.loc[51,'3']="라떼"
	df1.loc[52,'3']="그린티라떼"
	df1.loc[53,'2']="그린티"
	df1.loc[53,'3']="라떼"
	df1.loc[54,'2']="아이스x"
	df1.loc[54,'3']="초콜릿x"
	df1.loc[55,'2']="콜드브루"
	df1.loc[55,'3']="밀크티"
	df1.loc[56,'2']="핫"
	df1.loc[56,'3']="초콜릿"
	df1.loc[57,'2']="아이스"
	df1.loc[57,'3']="초콜릿"
	df1.loc[58,'2']="레몬"
	df1.loc[58,'3']="스파클링"
	df1.loc[59,'2']="자몽"
	df1.loc[59,'3']="스파클링"
	df1.loc[60,'2']="베리"
	df1.loc[60,'3']="스파클링"
	df1.loc[61,'2']="청포도"
	df1.loc[61,'3']="스파클링"
	df1.loc[62,'3']="딸기플라워밀크쉐이크"
	df1.loc[63,'3']="딸기프룻티펀치"
	df1.loc[64,'3']="딸기치즈큐브쉐이크"
	df1.loc[65,'3']="딸기요거트그래놀라"
	df1.loc[66,'3']="딸기라떼"
	df1.loc[67,'3']="딸기주스"
	df1.loc[68,'2']="딸기"
	df1.loc[68,'3']="주스"
	df1.loc[69,'2']="키위"
	df1.loc[69,'3']="주스"
	df1.loc[70,'2']="토마토"
	df1.loc[70,'3']="주스"
	df1.loc[71,'2']="루비자몽"
	df1.loc[71,'3']="주스"
	df1.loc[72,'2']="루비자몽"
	df1.loc[72,'3']="핫주스"
	df1.loc[73,'2']="오렌지"
	df1.loc[73,'3']="주스"
	df1.loc[74,'2']="프루티"
	df1.loc[74,'3']="하동"
	df1.loc[75,'2']="머스캣"
	df1.loc[75,'3']="그린티"
	df1.loc[76,'3']="민트크루"
	df1.loc[77,'2']="오렌지"
	df1.loc[77,'3']="보스"
	df1.loc[78,'2']="루이보스"
	df1.loc[78,'3']="오렌지"
	df1.loc[79,'3']="커즈마인"
	df1.loc[80,'2']="시트러스"
	df1.loc[80,'3']="캐모마일"
	df1.loc[81,'2']="퍼스트"
	df1.loc[81,'3']="브레이크"
	df1.loc[82,'3']="영그레이"
	df1.loc[83,'1']="아이스"
	df1.loc[83,'2']="루이보스"
	df1.loc[83,'3']="크림티"
	df1.loc[84,'2']="루이보스"
	df1.loc[84,'3']="크림티"
	df1.loc[85,'1']="아이스"
	df1.loc[85,'2']="캐모마일"
	df1.loc[85,'3']="프루티"
	df1.loc[86,'2']="캐모마일"
	df1.loc[86,'3']="프루티"
	df1.loc[87,'2']="파니니"
	df1.loc[87,'3']="클래식"
	df1.loc[88,'2']="파니니"
	df1.loc[88,'3']="불고기"
	df1.loc[89,'3']="허니브레드"
	df1.loc[90,'2']="수플레"
	df1.loc[90,'3']="치즈케익"
	df1.loc[91,'3']="흑당이달고나빙산"
	df1.loc[92,'3']="피치얼그레이빙산"
	df1.loc[93,'3']="요거딸기빙산"
	df1.loc[94,'3']="망고딸기동산"
	df1.loc[95,'3']="인절미팥동산"
	df1.loc[96,'3']="찹찹딸기라떼보틀"
	df1.loc[97,'1']="홀)"
	df1.loc[97,'2']="수플레"
	df1.loc[97,'3']="치즈케익"
	df1.loc[98,'2']="애플시나몬"
	df1.loc[98,'3']="허니브레드"
	df1.loc[99,'1']="까사링고"
	df1.loc[99,'2']="베리"
	df1.loc[99,'3']="케익"

	for i in range(0,len(df.index)):
		for i2 in range(0,len(df1.index)):
			if df1.loc[i2,'1'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'1'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'2'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'2'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'3'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'3'] = df.loc[i,"총리스트"]


	str02=""
	str02+=df2.loc[0,"3"]

	#for i3 in range(1,len(df2.index)):
	#	str02 +=","
	#	str02+=df2.loc[i,"3"]
	# df3=df2.sort_index()
	
	# str02=""
	# for i in range(0,len(df3.index)):
	# 	str02 +=","
	# 	str02 += df3.loc[i,"3"]
    

	# str02=""
	# for i in range(0,len(df.index)):
	# 	str02 +=","
	# 	str02 += df.loc[i,"총리스트"]
                 
	#print(df.loc[0,"총리스트"])
	return HttpResponse(str02)

def index02(request):
	candidate = Candidate.objects.all()

	no1 = Candidate.objects.filter(party_number = 3)
	no1[0].party_number 
	image_db01=no1[0].image_file

	image_db=str(image_db01)
	client = vision.ImageAnnotatorClient()
	    
	file_name = os.path.join(
	        os.path.dirname('C:'), 
	                            '/Users/student/mysite02/media/'+image_db)

	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)


	response = client.text_detection(image=image)
	texts = response.text_annotations
	       
	my_list = list()

	for text in texts:
		result = text.description
		my_list.append(result)
	    
	data = my_list[0]

	data1 = data.replace('\n',' ')
	data2 = data1.replace('(',' ')
	data3 = data2.replace(')',' ')
	data4 = data3.replace('/',' ')
	data5 = data4.split(' ')

	df = pd.DataFrame(data5, columns=["총리스트"])

	df1 = pd.DataFrame(columns=["0","1","2","3"])
	df2 = pd.DataFrame(columns=["0","1","2","3"])

	df1.loc[0, '3'] ="아메리카노"
	df1.loc[1, '2'] ="아이스"
	df1.loc[1, '3'] ="아메리카노"
	df1.loc[2, '2'] ="아이스"
	df1.loc[2, '3'] ="카페라떼"
	df1.loc[3, '3'] ="카페라떼"
	df1.loc[4, '1'] ="아이스"
	df1.loc[4, '2'] ="바닐라라떼"
	df1.loc[4, '3'] ="마끼아또"
	df1.loc[5, '1'] ="아이스"
	df1.loc[5, '2'] ="카라멜라떼"
	df1.loc[5, '3'] ="마끼아또"
	df1.loc[6, '2'] ="카라멜라떼"
	df1.loc[6, '3'] ="마끼아또"
	df1.loc[7, '3'] ="마끼아또"
	df1.loc[7, '2'] ="라떼"
	df1.loc[7, '1'] ="카라멜"
	df1.loc[8, '2'] ="바닐라라떼"
	df1.loc[8, '3'] ="마끼아또"
	df1.loc[9, '1'] ="바닐라"
	df1.loc[9, '2'] ="라떼"
	df1.loc[9, '3'] ="마끼아또"
	df1.loc[10, '1'] ="화이트초콜릿"
	df1.loc[10, '2'] ="라떼"
	df1.loc[10, '3'] ="마끼아또"
	df1.loc[11, '3'] ="카푸치노"
	df1.loc[12, '2'] ="헤이즐넛"
	df1.loc[12, '3'] ="카푸치노"
	df1.loc[13, '2'] ="오리지널"
	df1.loc[13, '3'] ="드립커피"
	df1.loc[14, '1'] ="아이스"
	df1.loc[14, '2'] ="오리지널"
	df1.loc[14, '3'] ="드립커피"
	df1.loc[15, '2'] ="카페"
	df1.loc[15, '3'] ="모카"
	df1.loc[16, '3'] ="카페모카"
	df1.loc[17, '2'] ="아이스"
	df1.loc[17, '3'] ="카페모카"
	df1.loc[18, '2'] ="화이트초콜릿라떼"
	df1.loc[18, '3'] ="마끼아또"
	df1.loc[19, '1'] ="아이스"
	df1.loc[19, '2'] ="화이트초콜릿라떼"
	df1.loc[19, '3'] ="마끼아또"
	df1.loc[20, '2'] ="콜드브루"
	df1.loc[20, '3'] ="아메리카노"
	df1.loc[21, '2'] ="콜드브루"
	df1.loc[21, '3'] ="원액"
	df1.loc[22, '2'] ="니트로"
	df1.loc[22, '3'] ="콜드브루"
	df1.loc[23, '2'] ="콜드브루"
	df1.loc[23, '3'] ="라떼"
	df1.loc[24, '3'] ="그라니때"
	df1.loc[24, '2'] ="콘파나"
	df1.loc[24, '1'] ="모카"
	df1.loc[25, '1'] ="카라멜"
	df1.loc[25, '2'] ="콘파나"
	df1.loc[25, '3'] ="그라니때"
	df1.loc[26, '3'] ="그라니때"
	df1.loc[26, '2'] ="망고요거트"
	df1.loc[27, '3'] ="그라니때"
	df1.loc[27, '2'] ="요거트"
	df1.loc[27, '1'] ="망고"
	df1.loc[28, '3'] ="그라니때"
	df1.loc[28, '2'] ="플레인요거트"
	df1.loc[29, '3'] ="그라니때"
	df1.loc[29, '1'] ="플레인"
	df1.loc[29, '2'] ="요거트"
	df1.loc[30, '3'] ="그라니때"
	df1.loc[30, '2'] ="자바칩민트"
	df1.loc[31, '3'] ="그라니때"
	df1.loc[31, '2'] ="에스프레소콘파나"
	df1.loc[32, '3'] ="그라니때"
	df1.loc[32, '2'] ="콘파나"
	df1.loc[32, '1'] ="에스프레소"
	df1.loc[33, '3'] ="그라니때"
	df1.loc[33, '2'] ="스트로베리요거트"
	df1.loc[34, '3'] ="그라니때"
	df1.loc[34, '2'] ="요거트"
	df1.loc[34, '1'] ="스트로베리"
	df1.loc[35, '3'] ="그라니때"
	df1.loc[35, '2'] ="스트로베리"
	df1.loc[36, '3'] ="그라니때"
	df1.loc[36, '2'] ="블루베리요거트"
	df1.loc[37, '3'] ="그라니때"
	df1.loc[37, '2'] ="요거트"
	df1.loc[37, '1'] ="블루베리"
	df1.loc[38, '3'] ="그라니때"
	df1.loc[38, '2'] ="복숭아"
	df1.loc[39, '3'] ="그라니때"
	df1.loc[39, '2'] ="그린티"
	df1.loc[40, '3'] ="그라니때"
	df1.loc[40, '2'] ="찰인절미"
	df1.loc[40, '1'] ="레드빈"
	df1.loc[41, '3'] ="그라니때"
	df1.loc[41, '2'] ="흑임자"
	df1.loc[41, '1'] ="레드빈"
	df1.loc[42, '3'] ="레드빈흑임자그라니때"
	df1.loc[43, '3'] ="그라니때"
	df1.loc[43, '2'] ="쑥"
	df1.loc[43, '1'] ="레드빈"
	df1.loc[44, '3'] ="레드빈쑥그라니때"
	df1.loc[45, '3'] ="그라니때"
	df1.loc[45, '2'] ="민트"
	df1.loc[45, '1'] ="레몬"
	df1.loc[46, '3'] ="그라니때"
	df1.loc[46, '2'] ="민트"
	df1.loc[46, '1'] ="자바칩"
	df1.loc[47, '3'] ="아이스티"
	df1.loc[48, '3'] ="아이스티"
	df1.loc[48, '2'] ="라즈베리"
	df1.loc[49, '3'] ="아이스티"
	df1.loc[49, '2'] ="복숭아"
	df1.loc[50, '3'] ="그린티라떼"
	df1.loc[50, '2'] ="아이스"
	df1.loc[51,'1']="아이스"
	df1.loc[51,'2']="그린티"
	df1.loc[51,'3']="라떼"
	df1.loc[52,'3']="그린티라떼"
	df1.loc[53,'2']="그린티"
	df1.loc[53,'3']="라떼"
	df1.loc[54,'2']="아이스x"
	df1.loc[54,'3']="초콜릿x"
	df1.loc[55,'2']="콜드브루"
	df1.loc[55,'3']="밀크티"
	df1.loc[56,'2']="핫"
	df1.loc[56,'3']="초콜릿"
	df1.loc[57,'2']="아이스"
	df1.loc[57,'3']="초콜릿"
	df1.loc[58,'2']="레몬"
	df1.loc[58,'3']="스파클링"
	df1.loc[59,'2']="자몽"
	df1.loc[59,'3']="스파클링"
	df1.loc[60,'2']="베리"
	df1.loc[60,'3']="스파클링"
	df1.loc[61,'2']="청포도"
	df1.loc[61,'3']="스파클링"
	df1.loc[62,'3']="딸기플라워밀크쉐이크"
	df1.loc[63,'3']="딸기프룻티펀치"
	df1.loc[64,'3']="딸기치즈큐브쉐이크"
	df1.loc[65,'3']="딸기요거트그래놀라"
	df1.loc[66,'3']="딸기라떼"
	df1.loc[67,'3']="딸기주스"
	df1.loc[68,'2']="딸기"
	df1.loc[68,'3']="주스"
	df1.loc[69,'2']="키위"
	df1.loc[69,'3']="주스"
	df1.loc[70,'2']="토마토"
	df1.loc[70,'3']="주스"
	df1.loc[71,'2']="루비자몽"
	df1.loc[71,'3']="주스"
	df1.loc[72,'2']="루비자몽"
	df1.loc[72,'3']="핫주스"
	df1.loc[73,'2']="오렌지"
	df1.loc[73,'3']="주스"
	df1.loc[74,'2']="프루티"
	df1.loc[74,'3']="하동"
	df1.loc[75,'2']="머스캣"
	df1.loc[75,'3']="그린티"
	df1.loc[76,'3']="민트크루"
	df1.loc[77,'2']="오렌지"
	df1.loc[77,'3']="보스"
	df1.loc[78,'2']="루이보스"
	df1.loc[78,'3']="오렌지"
	df1.loc[79,'3']="커즈마인"
	df1.loc[80,'2']="시트러스"
	df1.loc[80,'3']="캐모마일"
	df1.loc[81,'2']="퍼스트"
	df1.loc[81,'3']="브레이크"
	df1.loc[82,'3']="영그레이"
	df1.loc[83,'1']="아이스"
	df1.loc[83,'2']="루이보스"
	df1.loc[83,'3']="크림티"
	df1.loc[84,'2']="루이보스"
	df1.loc[84,'3']="크림티"
	df1.loc[85,'1']="아이스"
	df1.loc[85,'2']="캐모마일"
	df1.loc[85,'3']="프루티"
	df1.loc[86,'2']="캐모마일"
	df1.loc[86,'3']="프루티"
	df1.loc[87,'2']="파니니"
	df1.loc[87,'3']="클래식"
	df1.loc[88,'2']="파니니"
	df1.loc[88,'3']="불고기"
	df1.loc[89,'3']="허니브레드"
	df1.loc[90,'2']="수플레"
	df1.loc[90,'3']="치즈케익"
	df1.loc[91,'3']="흑당이달고나빙산"
	df1.loc[92,'3']="피치얼그레이빙산"
	df1.loc[93,'3']="요거딸기빙산"
	df1.loc[94,'3']="망고딸기동산"
	df1.loc[95,'3']="인절미팥동산"
	df1.loc[96,'3']="찹찹딸기라떼보틀"
	df1.loc[97,'1']="홀)"
	df1.loc[97,'2']="수플레"
	df1.loc[97,'3']="치즈케익"
	df1.loc[98,'2']="애플시나몬"
	df1.loc[98,'3']="허니브레드"
	df1.loc[99,'1']="까사링고"
	df1.loc[99,'2']="베리"
	df1.loc[99,'3']="케익"
	df1.loc[100,'1']="그린티"
	df1.loc[100,'2']="티"
	df1.loc[100,'3']="라떼"
	df1.loc[101,'2']="그린티"
	df1.loc[101,'3']="티라떼"
	df1.loc[102,'0']="잉글리시"
	df1.loc[102,'1']="블랙퍼스트"
	df1.loc[102,'2']="티"
	df1.loc[102,'3']="라떼"
	df1.loc[103,'1']="잉글리시"
	df1.loc[103,'2']="블랙퍼스트"
	df1.loc[103,'3']="티라떼"
	df1.loc[104,'3']="BLT샌드위치"
	df1.loc[105,'3']="샌드위치"
	df1.loc[105,'2']="BLT"
	df1.loc[106,'3']="그라니때"
	df1.loc[106,'2']="단팥통통"
	df1.loc[107,'3']="그라니때"
	df1.loc[107,'2']="통통"
	df1.loc[107,'1']="단팥"
	df1.loc[108,'3']="그라니때"
	df1.loc[108,'2']="쑥떡쑥떡"
	df1.loc[109,'3']="그라니때"
	df1.loc[109,'2']="쑥떡"
	df1.loc[109,'1']="쑥떡"
	df1.loc[110,'3']="그라니때"
	df1.loc[110,'2']="플라이하이"
	df1.loc[111,'3']="그라니때"
	df1.loc[111,'2']="하이"
	df1.loc[111,'1']="플라이"
	df1.loc[112,'3']="뱅쇼"
	df1.loc[112,'2']="히비스커스"
	df1.loc[113,'2']="레몬"
	df1.loc[113,'3']="Sparkling"
	df1.loc[114,'2']="자몽"
	df1.loc[114,'3']="Sparkling"
	df1.loc[115,'2']="베리"
	df1.loc[115,'3']="Sparkling"
	df1.loc[116,'2']="청포도"
	df1.loc[116,'3']="Sparkling"

	menu=df1[['0','1','2','3']].astype(str).sum(axis=1)
	menu = menu.str.replace('nan', '')
	m2=menu.unique()
	Allmenu = pd.DataFrame(m2, columns = ["AllMenu"])

	for i in range(0,len(df.index)):
		for i2 in range(0,len(df1.index)):
			if df1.loc[i2,'0'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'0'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'1'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'1'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'2'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'2'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'3'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'3'] = df.loc[i,"총리스트"]
	
	df3=df2.sort_index()
	match=df3[['0','1','2','3']].astype(str).sum(axis=1) #match -> array 형식 astype -> 문자로 변환 
	match = match.str.replace('nan', '') # 난값을 공백
	match = match.unique() # 중복메뉴 (아이스 4개행 중복 걸러줌)
	imgtxt = pd.DataFrame(match, columns = ["imgtxt"])

	str03=""
	
	for i3 in range(0,len(imgtxt)):

		str03+=imgtxt.loc[i3,"imgtxt"] + "\n"

	return HttpResponse(str03)






def index03(request):

	candidate = Candidate.objects.all()

	no1 = Candidate.objects.filter(party_number = 3)
	no1[0].party_number 
	image_db01=no1[0].image_file

	image_db=str(image_db01)
	client = vision.ImageAnnotatorClient()
	    
	file_name = os.path.join(
	        os.path.dirname('C:'), 
	                            '/Users/student/mysite02/media/'+image_db)

	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)


	response = client.text_detection(image=image)
	texts = response.text_annotations
	       
	my_list = list()

	for text in texts:
		result = text.description
		my_list.append(result)
	    
	data = my_list[0]

	data1 = data.replace('\n',' ')
	data2 = data1.replace('(',' ')
	data3 = data2.replace(')',' ')
	data4 = data3.replace('/',' ')
	data5 = data4.split(' ')

	df = pd.DataFrame(data5, columns=["총리스트"])

	df1 = pd.DataFrame(columns=["0","1","2","3"])
	df2 = pd.DataFrame(columns=["0","1","2","3"])

	df1.loc[0, '3'] ="아메리카노"
	df1.loc[1, '2'] ="아이스"
	df1.loc[1, '3'] ="아메리카노"
	df1.loc[2, '2'] ="아이스"
	df1.loc[2, '3'] ="카페라떼"
	df1.loc[3, '3'] ="카페라떼"
	df1.loc[4, '1'] ="아이스"
	df1.loc[4, '2'] ="바닐라라떼"
	df1.loc[4, '3'] ="마끼아또"
	df1.loc[5, '1'] ="아이스"
	df1.loc[5, '2'] ="카라멜라떼"
	df1.loc[5, '3'] ="마끼아또"
	df1.loc[6, '2'] ="카라멜라떼"
	df1.loc[6, '3'] ="마끼아또"
	df1.loc[7, '3'] ="마끼아또"
	df1.loc[7, '2'] ="라떼"
	df1.loc[7, '1'] ="카라멜"
	df1.loc[8, '2'] ="바닐라라떼"
	df1.loc[8, '3'] ="마끼아또"
	df1.loc[9, '1'] ="바닐라"
	df1.loc[9, '2'] ="라떼"
	df1.loc[9, '3'] ="마끼아또"
	df1.loc[10, '1'] ="화이트초콜릿"
	df1.loc[10, '2'] ="라떼"
	df1.loc[10, '3'] ="마끼아또"
	df1.loc[11, '3'] ="카푸치노"
	df1.loc[12, '2'] ="헤이즐넛"
	df1.loc[12, '3'] ="카푸치노"
	df1.loc[13, '2'] ="오리지널"
	df1.loc[13, '3'] ="드립커피"
	df1.loc[14, '1'] ="아이스"
	df1.loc[14, '2'] ="오리지널"
	df1.loc[14, '3'] ="드립커피"
	df1.loc[15, '2'] ="카페"
	df1.loc[15, '3'] ="모카"
	df1.loc[16, '3'] ="카페모카"
	df1.loc[17, '2'] ="아이스"
	df1.loc[17, '3'] ="카페모카"
	df1.loc[18, '2'] ="화이트초콜릿라떼"
	df1.loc[18, '3'] ="마끼아또"
	df1.loc[19, '1'] ="아이스"
	df1.loc[19, '2'] ="화이트초콜릿라떼"
	df1.loc[19, '3'] ="마끼아또"
	df1.loc[20, '2'] ="콜드브루"
	df1.loc[20, '3'] ="아메리카노"
	df1.loc[21, '2'] ="콜드브루"
	df1.loc[21, '3'] ="원액"
	df1.loc[22, '2'] ="니트로"
	df1.loc[22, '3'] ="콜드브루"
	df1.loc[23, '2'] ="콜드브루"
	df1.loc[23, '3'] ="라떼"
	df1.loc[24, '3'] ="그라니때"
	df1.loc[24, '2'] ="콘파나"
	df1.loc[24, '1'] ="모카"
	df1.loc[25, '1'] ="카라멜"
	df1.loc[25, '2'] ="콘파나"
	df1.loc[25, '3'] ="그라니때"
	df1.loc[26, '3'] ="그라니때"
	df1.loc[26, '2'] ="망고요거트"
	df1.loc[27, '3'] ="그라니때"
	df1.loc[27, '2'] ="요거트"
	df1.loc[27, '1'] ="망고"
	df1.loc[28, '3'] ="그라니때"
	df1.loc[28, '2'] ="플레인요거트"
	df1.loc[29, '3'] ="그라니때"
	df1.loc[29, '1'] ="플레인"
	df1.loc[29, '2'] ="요거트"
	df1.loc[30, '3'] ="그라니때"
	df1.loc[30, '2'] ="자바칩민트"
	df1.loc[31, '3'] ="그라니때"
	df1.loc[31, '2'] ="에스프레소콘파나"
	df1.loc[32, '3'] ="그라니때"
	df1.loc[32, '2'] ="콘파나"
	df1.loc[32, '1'] ="에스프레소"
	df1.loc[33, '3'] ="그라니때"
	df1.loc[33, '2'] ="스트로베리요거트"
	df1.loc[34, '3'] ="그라니때"
	df1.loc[34, '2'] ="요거트"
	df1.loc[34, '1'] ="스트로베리"
	df1.loc[35, '3'] ="그라니때"
	df1.loc[35, '2'] ="스트로베리"
	df1.loc[36, '3'] ="그라니때"
	df1.loc[36, '2'] ="블루베리요거트"
	df1.loc[37, '3'] ="그라니때"
	df1.loc[37, '2'] ="요거트"
	df1.loc[37, '1'] ="블루베리"
	df1.loc[38, '3'] ="그라니때"
	df1.loc[38, '2'] ="복숭아"
	df1.loc[39, '3'] ="그라니때"
	df1.loc[39, '2'] ="그린티"
	df1.loc[40, '3'] ="그라니때"
	df1.loc[40, '2'] ="찰인절미"
	df1.loc[40, '1'] ="레드빈"
	df1.loc[41, '3'] ="그라니때"
	df1.loc[41, '2'] ="흑임자"
	df1.loc[41, '1'] ="레드빈"
	df1.loc[42, '3'] ="레드빈흑임자그라니때"
	df1.loc[43, '3'] ="그라니때"
	df1.loc[43, '2'] ="쑥"
	df1.loc[43, '1'] ="레드빈"
	df1.loc[44, '3'] ="레드빈쑥그라니때"
	df1.loc[45, '3'] ="그라니때"
	df1.loc[45, '2'] ="민트"
	df1.loc[45, '1'] ="레몬"
	df1.loc[46, '3'] ="그라니때"
	df1.loc[46, '2'] ="민트"
	df1.loc[46, '1'] ="자바칩"
	df1.loc[47, '3'] ="아이스티"
	df1.loc[48, '3'] ="아이스티"
	df1.loc[48, '2'] ="라즈베리"
	df1.loc[49, '3'] ="아이스티"
	df1.loc[49, '2'] ="복숭아"
	df1.loc[50, '3'] ="그린티라떼"
	df1.loc[50, '2'] ="아이스"
	df1.loc[51,'1']="아이스"
	df1.loc[51,'2']="그린티"
	df1.loc[51,'3']="라떼"
	df1.loc[52,'3']="그린티라떼"
	df1.loc[53,'2']="그린티"
	df1.loc[53,'3']="라떼"
	df1.loc[54,'2']="아이스x"
	df1.loc[54,'3']="초콜릿x"
	df1.loc[55,'2']="콜드브루"
	df1.loc[55,'3']="밀크티"
	df1.loc[56,'2']="핫"
	df1.loc[56,'3']="초콜릿"
	df1.loc[57,'2']="아이스"
	df1.loc[57,'3']="초콜릿"
	df1.loc[58,'2']="레몬"
	df1.loc[58,'3']="스파클링"
	df1.loc[59,'2']="자몽"
	df1.loc[59,'3']="스파클링"
	df1.loc[60,'2']="베리"
	df1.loc[60,'3']="스파클링"
	df1.loc[61,'2']="청포도"
	df1.loc[61,'3']="스파클링"
	df1.loc[62,'3']="딸기플라워밀크쉐이크"
	df1.loc[63,'3']="딸기프룻티펀치"
	df1.loc[64,'3']="딸기치즈큐브쉐이크"
	df1.loc[65,'3']="딸기요거트그래놀라"
	df1.loc[66,'3']="딸기라떼"
	df1.loc[67,'3']="딸기주스"
	df1.loc[68,'2']="딸기"
	df1.loc[68,'3']="주스"
	df1.loc[69,'2']="키위"
	df1.loc[69,'3']="주스"
	df1.loc[70,'2']="토마토"
	df1.loc[70,'3']="주스"
	df1.loc[71,'2']="루비자몽"
	df1.loc[71,'3']="주스"
	df1.loc[72,'2']="루비자몽"
	df1.loc[72,'3']="핫주스"
	df1.loc[73,'2']="오렌지"
	df1.loc[73,'3']="주스"
	df1.loc[74,'2']="프루티"
	df1.loc[74,'3']="하동"
	df1.loc[75,'2']="머스캣"
	df1.loc[75,'3']="그린티"
	df1.loc[76,'3']="민트크루"
	df1.loc[77,'2']="오렌지"
	df1.loc[77,'3']="보스"
	df1.loc[78,'2']="루이보스"
	df1.loc[78,'3']="오렌지"
	df1.loc[79,'3']="커즈마인"
	df1.loc[80,'2']="시트러스"
	df1.loc[80,'3']="캐모마일"
	df1.loc[81,'2']="퍼스트"
	df1.loc[81,'3']="브레이크"
	df1.loc[82,'3']="영그레이"
	df1.loc[83,'1']="아이스"
	df1.loc[83,'2']="루이보스"
	df1.loc[83,'3']="크림티"
	df1.loc[84,'2']="루이보스"
	df1.loc[84,'3']="크림티"
	df1.loc[85,'1']="아이스"
	df1.loc[85,'2']="캐모마일"
	df1.loc[85,'3']="프루티"
	df1.loc[86,'2']="캐모마일"
	df1.loc[86,'3']="프루티"
	df1.loc[87,'2']="파니니"
	df1.loc[87,'3']="클래식"
	df1.loc[88,'2']="파니니"
	df1.loc[88,'3']="불고기"
	df1.loc[89,'3']="허니브레드"
	df1.loc[90,'2']="수플레"
	df1.loc[90,'3']="치즈케익"
	df1.loc[91,'3']="흑당이달고나빙산"
	df1.loc[92,'3']="피치얼그레이빙산"
	df1.loc[93,'3']="요거딸기빙산"
	df1.loc[94,'3']="망고딸기동산"
	df1.loc[95,'3']="인절미팥동산"
	df1.loc[96,'3']="찹찹딸기라떼보틀"
	df1.loc[97,'1']="홀)"
	df1.loc[97,'2']="수플레"
	df1.loc[97,'3']="치즈케익"
	df1.loc[98,'2']="애플시나몬"
	df1.loc[98,'3']="허니브레드"
	df1.loc[99,'1']="까사링고"
	df1.loc[99,'2']="베리"
	df1.loc[99,'3']="케익"
	df1.loc[100,'1']="그린티"
	df1.loc[100,'2']="티"
	df1.loc[100,'3']="라떼"
	df1.loc[101,'2']="그린티"
	df1.loc[101,'3']="티라떼"
	df1.loc[102,'0']="잉글리시"
	df1.loc[102,'1']="블랙퍼스트"
	df1.loc[102,'2']="티"
	df1.loc[102,'3']="라떼"
	df1.loc[103,'1']="잉글리시"
	df1.loc[103,'2']="블랙퍼스트"
	df1.loc[103,'3']="티라떼"
	df1.loc[104,'3']="BLT샌드위치"
	df1.loc[105,'3']="샌드위치"
	df1.loc[105,'2']="BLT"
	df1.loc[106,'3']="그라니때"
	df1.loc[106,'2']="단팥통통"
	df1.loc[107,'3']="그라니때"
	df1.loc[107,'2']="통통"
	df1.loc[107,'1']="단팥"
	df1.loc[108,'3']="그라니때"
	df1.loc[108,'2']="쑥떡쑥떡"
	df1.loc[109,'3']="그라니때"
	df1.loc[109,'2']="쑥떡"
	df1.loc[109,'1']="쑥떡"
	df1.loc[110,'3']="그라니때"
	df1.loc[110,'2']="플라이하이"
	df1.loc[111,'3']="그라니때"
	df1.loc[111,'2']="하이"
	df1.loc[111,'1']="플라이"
	df1.loc[112,'3']="뱅쇼"
	df1.loc[112,'2']="히비스커스"
	df1.loc[113,'2']="레몬"
	df1.loc[113,'3']="Sparkling"
	df1.loc[114,'2']="자몽"
	df1.loc[114,'3']="Sparkling"
	df1.loc[115,'2']="베리"
	df1.loc[115,'3']="Sparkling"
	df1.loc[116,'2']="청포도"
	df1.loc[116,'3']="Sparkling"

	menu=df1[['0','1','2','3']].astype(str).sum(axis=1)
	menu = menu.str.replace('nan', '')
	m2=menu.unique()
	Allmenu = pd.DataFrame(m2, columns = ["AllMenu"])

	for i in range(0,len(df.index)):
		for i2 in range(0,len(df1.index)):
			if df1.loc[i2,'0'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'0'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'1'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'1'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'2'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'2'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'3'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'3'] = df.loc[i,"총리스트"]
	
	df3=df2.sort_index()
	match=df3[['0','1','2','3']].astype(str).sum(axis=1) #match -> array 형식 astype -> 문자로 변환 
	match = match.str.replace('nan', '') # 난값을 공백
	match = match.unique() # 중복메뉴 (아이스 4개행 중복 걸러줌)
	imgtxt = pd.DataFrame(match, columns = ["imgtxt"])

	

	str04={0:"가"}
	for i4 in range(0,len(imgtxt)):
		str04[i4]=imgtxt.loc[i4,"imgtxt"]
	# str04={0:"가"}
	# for i4 in range(0,len(imgtxt)):

	# 	str04[i4]=imgtxt.loc[i4,"imgtxt"]

	return render(request , 'elections/index.html' , str04)

def index04(request):


	con = cx_Oracle.connect("dator/me@localhost:1521/XE")

	cur=con.cursor()

	cur.execute("SELECT menu FROM data_no_rain ORDER BY NoRainResult")
	stt=()
	sttdf = pd.DataFrame(columns=["순위메뉴"])
	i6=0

	for row in cur:
		stt+=row
		sttdf.loc[i6,"순위메뉴"]=stt[i6]
		i6+=1

	result_finish = pd.DataFrame(columns=["최종결과","순위"])


	for i7 in range(0,len(imgtxt.index)):
		for i8 in range(0,len(sttdf.index)):
			if sttdf.loc[i8,'순위메뉴'] == imgtxt.loc[i7,"imgtxt"]:
				result_finish.loc[i8,'최종결과'] = imgtxt.loc[i7,"imgtxt"]
				result_finish.loc[i8,'순위']=i8

	result_finish01=result_finish.sort_index()


	sttt=""
	for i9 in range(0,len(result_finish01.index)):
		sttt+=result_finish01.iloc[i9,0]
		sttt+="\n"

	print(sttt)



	return HttpResponse(sttt)

def index05(request):

	candidate = Candidate.objects.all()

	no1 = Candidate.objects.filter(party_number = 4) #party_number는 게시물올릴때 번호 다른걸로 바뀌줄수있음
	no1[0].party_number 
	image_db01=no1[0].image_file

	image_db=str(image_db01)
	client = vision.ImageAnnotatorClient()
	    
	file_name = os.path.join(
	        os.path.dirname('C:'), 
	                            '/Users/student/mysite02/media/'+image_db)

	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)


	response = client.text_detection(image=image)
	texts = response.text_annotations
	       
	my_list = list()

	for text in texts:
		result = text.description
		my_list.append(result)
	    
	data = my_list[0]

	data1 = data.replace('\n',' ')
	data2 = data1.replace('(',' ')
	data3 = data2.replace(')',' ')
	data4 = data3.replace('/',' ')
	data5 = data4.split(' ')

	df = pd.DataFrame(data5, columns=["총리스트"])

	df1 = pd.DataFrame(columns=["0","1","2","3"])
	df2 = pd.DataFrame(columns=["0","1","2","3"])

	df1.loc[0, '3'] ="아메리카노"
	df1.loc[1, '2'] ="아이스"
	df1.loc[1, '3'] ="아메리카노"
	df1.loc[2, '2'] ="아이스"
	df1.loc[2, '3'] ="카페라떼"
	df1.loc[3, '3'] ="카페라떼"
	df1.loc[4, '1'] ="아이스"
	df1.loc[4, '2'] ="바닐라라떼"
	df1.loc[4, '3'] ="마끼아또"
	df1.loc[5, '1'] ="아이스"
	df1.loc[5, '2'] ="카라멜라떼"
	df1.loc[5, '3'] ="마끼아또"
	df1.loc[6, '2'] ="카라멜라떼"
	df1.loc[6, '3'] ="마끼아또"
	df1.loc[7, '3'] ="마끼아또"
	df1.loc[7, '2'] ="라떼"
	df1.loc[7, '1'] ="카라멜"
	df1.loc[8, '2'] ="바닐라라떼"
	df1.loc[8, '3'] ="마끼아또"
	df1.loc[9, '1'] ="바닐라"
	df1.loc[9, '2'] ="라떼"
	df1.loc[9, '3'] ="마끼아또"
	df1.loc[10, '1'] ="화이트초콜릿"
	df1.loc[10, '2'] ="라떼"
	df1.loc[10, '3'] ="마끼아또"
	df1.loc[11, '3'] ="카푸치노"
	df1.loc[12, '2'] ="헤이즐넛"
	df1.loc[12, '3'] ="카푸치노"
	df1.loc[13, '2'] ="오리지널"
	df1.loc[13, '3'] ="드립커피"
	df1.loc[14, '1'] ="아이스"
	df1.loc[14, '2'] ="오리지널"
	df1.loc[14, '3'] ="드립커피"
	df1.loc[15, '2'] ="카페"
	df1.loc[15, '3'] ="모카"
	df1.loc[16, '3'] ="카페모카"
	df1.loc[17, '2'] ="아이스"
	df1.loc[17, '3'] ="카페모카"
	df1.loc[18, '2'] ="화이트초콜릿라떼"
	df1.loc[18, '3'] ="마끼아또"
	df1.loc[19, '1'] ="아이스"
	df1.loc[19, '2'] ="화이트초콜릿라떼"
	df1.loc[19, '3'] ="마끼아또"
	df1.loc[20, '2'] ="콜드브루"
	df1.loc[20, '3'] ="아메리카노"
	df1.loc[21, '2'] ="콜드브루"
	df1.loc[21, '3'] ="원액"
	df1.loc[22, '2'] ="니트로"
	df1.loc[22, '3'] ="콜드브루"
	df1.loc[23, '2'] ="콜드브루"
	df1.loc[23, '3'] ="라떼"
	df1.loc[24, '3'] ="그라니때"
	df1.loc[24, '2'] ="콘파나"
	df1.loc[24, '1'] ="모카"
	df1.loc[25, '1'] ="카라멜"
	df1.loc[25, '2'] ="콘파나"
	df1.loc[25, '3'] ="그라니때"
	df1.loc[26, '3'] ="그라니때"
	df1.loc[26, '2'] ="망고요거트"
	df1.loc[27, '3'] ="그라니때"
	df1.loc[27, '2'] ="요거트"
	df1.loc[27, '1'] ="망고"
	df1.loc[28, '3'] ="그라니때"
	df1.loc[28, '2'] ="플레인요거트"
	df1.loc[29, '3'] ="그라니때"
	df1.loc[29, '1'] ="플레인"
	df1.loc[29, '2'] ="요거트"
	df1.loc[30, '3'] ="그라니때"
	df1.loc[30, '2'] ="자바칩민트"
	df1.loc[31, '3'] ="그라니때"
	df1.loc[31, '2'] ="에스프레소콘파나"
	df1.loc[32, '3'] ="그라니때"
	df1.loc[32, '2'] ="콘파나"
	df1.loc[32, '1'] ="에스프레소"
	df1.loc[33, '3'] ="그라니때"
	df1.loc[33, '2'] ="스트로베리요거트"
	df1.loc[34, '3'] ="그라니때"
	df1.loc[34, '2'] ="요거트"
	df1.loc[34, '1'] ="스트로베리"
	df1.loc[35, '3'] ="그라니때"
	df1.loc[35, '2'] ="스트로베리"
	df1.loc[36, '3'] ="그라니때"
	df1.loc[36, '2'] ="블루베리요거트"
	df1.loc[37, '3'] ="그라니때"
	df1.loc[37, '2'] ="요거트"
	df1.loc[37, '1'] ="블루베리"
	df1.loc[38, '3'] ="그라니때"
	df1.loc[38, '2'] ="복숭아"
	df1.loc[39, '3'] ="그라니때"
	df1.loc[39, '2'] ="그린티"
	df1.loc[40, '3'] ="그라니때"
	df1.loc[40, '2'] ="찰인절미"
	df1.loc[40, '1'] ="레드빈"
	df1.loc[41, '3'] ="그라니때"
	df1.loc[41, '2'] ="흑임자"
	df1.loc[41, '1'] ="레드빈"
	df1.loc[42, '3'] ="레드빈흑임자그라니때"
	df1.loc[43, '3'] ="그라니때"
	df1.loc[43, '2'] ="쑥"
	df1.loc[43, '1'] ="레드빈"
	df1.loc[44, '3'] ="레드빈쑥그라니때"
	df1.loc[45, '3'] ="그라니때"
	df1.loc[45, '2'] ="민트"
	df1.loc[45, '1'] ="레몬"
	df1.loc[46, '3'] ="그라니때"
	df1.loc[46, '2'] ="민트"
	df1.loc[46, '1'] ="자바칩"
	df1.loc[47, '3'] ="아이스티"
	df1.loc[48, '3'] ="아이스티"
	df1.loc[48, '2'] ="라즈베리"
	df1.loc[49, '3'] ="아이스티"
	df1.loc[49, '2'] ="복숭아"
	df1.loc[50, '3'] ="그린티라떼"
	df1.loc[50, '2'] ="아이스"
	df1.loc[51,'1']="아이스"
	df1.loc[51,'2']="그린티"
	df1.loc[51,'3']="라떼"
	df1.loc[52,'3']="그린티라떼"
	df1.loc[53,'2']="그린티"
	df1.loc[53,'3']="라떼"
	df1.loc[54,'2']="아이스x"
	df1.loc[54,'3']="초콜릿x"
	df1.loc[55,'2']="콜드브루"
	df1.loc[55,'3']="밀크티"
	df1.loc[56,'2']="핫"
	df1.loc[56,'3']="초콜릿"
	df1.loc[57,'2']="아이스"
	df1.loc[57,'3']="초콜릿"
	df1.loc[58,'2']="레몬"
	df1.loc[58,'3']="스파클링"
	df1.loc[59,'2']="자몽"
	df1.loc[59,'3']="스파클링"
	df1.loc[60,'2']="베리"
	df1.loc[60,'3']="스파클링"
	df1.loc[61,'2']="청포도"
	df1.loc[61,'3']="스파클링"
	df1.loc[62,'3']="딸기플라워밀크쉐이크"
	df1.loc[63,'3']="딸기프룻티펀치"
	df1.loc[64,'3']="딸기치즈큐브쉐이크"
	df1.loc[65,'3']="딸기요거트그래놀라"
	df1.loc[66,'3']="딸기라떼"
	df1.loc[67,'3']="딸기주스"
	df1.loc[68,'2']="딸기"
	df1.loc[68,'3']="주스"
	df1.loc[69,'2']="키위"
	df1.loc[69,'3']="주스"
	df1.loc[70,'2']="토마토"
	df1.loc[70,'3']="주스"
	df1.loc[71,'2']="루비자몽"
	df1.loc[71,'3']="주스"
	df1.loc[72,'2']="루비자몽"
	df1.loc[72,'3']="핫주스"
	df1.loc[73,'2']="오렌지"
	df1.loc[73,'3']="주스"
	df1.loc[74,'2']="프루티"
	df1.loc[74,'3']="하동"
	df1.loc[75,'2']="머스캣"
	df1.loc[75,'3']="그린티"
	df1.loc[76,'3']="민트크루"
	df1.loc[77,'2']="오렌지"
	df1.loc[77,'3']="보스"
	df1.loc[78,'2']="루이보스"
	df1.loc[78,'3']="오렌지"
	df1.loc[79,'3']="커즈마인"
	df1.loc[80,'2']="시트러스"
	df1.loc[80,'3']="캐모마일"
	df1.loc[81,'2']="퍼스트"
	df1.loc[81,'3']="브레이크"
	df1.loc[82,'3']="영그레이"
	df1.loc[83,'1']="아이스"
	df1.loc[83,'2']="루이보스"
	df1.loc[83,'3']="크림티"
	df1.loc[84,'2']="루이보스"
	df1.loc[84,'3']="크림티"
	df1.loc[85,'1']="아이스"
	df1.loc[85,'2']="캐모마일"
	df1.loc[85,'3']="프루티"
	df1.loc[86,'2']="캐모마일"
	df1.loc[86,'3']="프루티"
	df1.loc[87,'2']="파니니"
	df1.loc[87,'3']="클래식"
	df1.loc[88,'2']="파니니"
	df1.loc[88,'3']="불고기"
	df1.loc[89,'3']="허니브레드"
	df1.loc[90,'2']="수플레"
	df1.loc[90,'3']="치즈케익"
	df1.loc[91,'3']="흑당이달고나빙산"
	df1.loc[92,'3']="피치얼그레이빙산"
	df1.loc[93,'3']="요거딸기빙산"
	df1.loc[94,'3']="망고딸기동산"
	df1.loc[95,'3']="인절미팥동산"
	df1.loc[96,'3']="찹찹딸기라떼보틀"
	df1.loc[97,'1']="홀)"
	df1.loc[97,'2']="수플레"
	df1.loc[97,'3']="치즈케익"
	df1.loc[98,'2']="애플시나몬"
	df1.loc[98,'3']="허니브레드"
	df1.loc[99,'1']="까사링고"
	df1.loc[99,'2']="베리"
	df1.loc[99,'3']="케익"
	df1.loc[100,'1']="그린티"
	df1.loc[100,'2']="티"
	df1.loc[100,'3']="라떼"
	df1.loc[101,'2']="그린티"
	df1.loc[101,'3']="티라떼"
	df1.loc[102,'0']="잉글리시"
	df1.loc[102,'1']="블랙퍼스트"
	df1.loc[102,'2']="티"
	df1.loc[102,'3']="라떼"
	df1.loc[103,'1']="잉글리시"
	df1.loc[103,'2']="블랙퍼스트"
	df1.loc[103,'3']="티라떼"
	df1.loc[104,'3']="BLT샌드위치"
	df1.loc[105,'3']="샌드위치"
	df1.loc[105,'2']="BLT"
	df1.loc[106,'3']="그라니때"
	df1.loc[106,'2']="단팥통통"
	df1.loc[107,'3']="그라니때"
	df1.loc[107,'2']="통통"
	df1.loc[107,'1']="단팥"
	df1.loc[108,'3']="그라니때"
	df1.loc[108,'2']="쑥떡쑥떡"
	df1.loc[109,'3']="그라니때"
	df1.loc[109,'2']="쑥떡"
	df1.loc[109,'1']="쑥떡"
	df1.loc[110,'3']="그라니때"
	df1.loc[110,'2']="플라이하이"
	df1.loc[111,'3']="그라니때"
	df1.loc[111,'2']="하이"
	df1.loc[111,'1']="플라이"
	df1.loc[112,'3']="뱅쇼"
	df1.loc[112,'2']="히비스커스"
	df1.loc[113,'2']="레몬"
	df1.loc[113,'3']="Sparkling"
	df1.loc[114,'2']="자몽"
	df1.loc[114,'3']="Sparkling"
	df1.loc[115,'2']="베리"
	df1.loc[115,'3']="Sparkling"
	df1.loc[116,'2']="청포도"
	df1.loc[116,'3']="Sparkling"

	menu=df1[['0','1','2','3']].astype(str).sum(axis=1)
	menu = menu.str.replace('nan', '')
	m2=menu.unique()
	Allmenu = pd.DataFrame(m2, columns = ["AllMenu"])

	for i in range(0,len(df.index)):
		for i2 in range(0,len(df1.index)):
			if df1.loc[i2,'0'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'0'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'1'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'1'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'2'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'2'] = df.loc[i,"총리스트"]
			elif df1.loc[i2,'3'] == df.loc[i,"총리스트"]:
				df2.loc[i2,'3'] = df.loc[i,"총리스트"]
	
	df3=df2.sort_index()
	match=df3[['0','1','2','3']].astype(str).sum(axis=1) #match -> array 형식 astype -> 문자로 변환 
	match = match.str.replace('nan', '') # 난값을 공백
	match = match.unique() # 중복메뉴 (아이스 4개행 중복 걸러줌)
	imgtxt = pd.DataFrame(match, columns = ["imgtxt"])



	con = cx_Oracle.connect("dator/me@localhost:1521/XE")

	cur=con.cursor()

	cur.execute("SELECT menu FROM data_no_rain ORDER BY NoRainResult DESC")
	stt=()
	sttdf = pd.DataFrame(columns=["순위메뉴"])
	i6=0

	for row in cur:
		stt+=row
		sttdf.loc[i6,"순위메뉴"]=stt[i6]
		i6+=1

	result_finish = pd.DataFrame(columns=["최종결과","순위"])


	for i7 in range(0,len(imgtxt.index)):
		for i8 in range(0,len(sttdf.index)):
			if sttdf.loc[i8,'순위메뉴'] == imgtxt.loc[i7,"imgtxt"]:
				result_finish.loc[i8,'최종결과'] = imgtxt.loc[i7,"imgtxt"]
				result_finish.loc[i8,'순위']=i8

	result_finish01=result_finish.sort_index()


	sttt=""
	for i9 in range(0,len(result_finish01.index)):
		sttt+=result_finish01.iloc[i9,0]
		sttt+="\n"

	print(sttt)



	return HttpResponse(sttt)
