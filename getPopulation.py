#getPopulation.py
#API : https://openapi.gg.go.kr/AgeAcctoPopltn?
#URL : https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=HH7N68ZBMYNCB7QE9OY927342034&infSeq=2&order=&loc=&searchWord=%EC%9D%B8%EA%B5%AC
#경기도 인구 현황
#(구)popul.py
import config
import requests
from bs4 import BeautifulSoup
import time
class PopulationInfo:
    def __init__(self):
        #형식 : [{'region': '경기도 가평군', 'ADMZONE_DIV_NM': '시군', 'population': 62566, 'LEGALDONG_CD': 4182000000},...]
        self.all_values = []
        self.region_group_Index=[]
        
    def getPopInfo(self):
        for i in range(1,906):
            response=requests.get('https://openapi.gg.go.kr/AgeAcctoPopltn?KEY={0}&pIndex={1}&pSize=100'.format(config.API_KEY_POPUL, i),headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
            soup=BeautifulSoup(response.text,'html.parser')
            #페이지 별 항목 갯수
            row = soup.select('row')
            #기준 년도
            EXAMIN_YY = soup.select('EXAMIN_YY')
            #기준 월
            EXAMIN_MT = soup.select('EXAMIN_MT')
            #행정구역명(읍,면,동), (시,군), (구)
            ADMZONE_NM = soup.select('ADMZONE_NM')
            #행정구역 단위
            ADMZONE_DIV_NM = soup.select('ADMZONE_DIV_NM')
            #총 인구수 
            TOT_POPLTN_CNT = soup.select('TOT_POPLTN_CNT')
            #법정지역코드
            LEGALDONG_CD = soup.select('LEGALDONG_CD')
            
            for j in(range(0,len(row))):
                if EXAMIN_YY[j].text=='2020' and EXAMIN_MT[j].text=='05':
                    if ADMZONE_DIV_NM[j].text=='읍면동':
                        dic = {}
                        #지역명 (읍,명,동)
                        dic['region']=ADMZONE_NM[j].text
                        #행정구역 단위
                        dic['ADMZONE_DIV_NM']=ADMZONE_DIV_NM[j].text
                        #인구수
                        dic['population']=int(TOT_POPLTN_CNT[j].text)
                        #법정지역코드
                        dic['LEGALDONG_CD']=int(LEGALDONG_CD[j].text)
                        self.all_values.append(dic)
                    elif ADMZONE_DIV_NM[j].text=='구' or ADMZONE_DIV_NM[j].text=='시군':
                        dic = {}
                        #지역명 (시군, 구)
                        dic['region']=ADMZONE_NM[j].text
                        #행정구역 단위
                        dic['ADMZONE_DIV_NM']=ADMZONE_DIV_NM[j].text
                        #인구수
                        dic['population']=int(TOT_POPLTN_CNT[j].text)
                        #법정지역코드
                        dic['LEGALDONG_CD']=int(LEGALDONG_CD[j].text)
                        self.all_values.append(dic)
            time.sleep(0.5)


if __name__ == "__main__":        
    a = PopulationInfo()
    a.getPopInfo()
    #값 : 595
    print(len(a.all_values))