#API : https://openapi.gg.go.kr/Schoolstdntcntsecndhd
#URL : https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=3&rows=10&sortColumn=&sortDirection=&infId=8GRSB88F2QW4RJ3MG95I23516519&infSeq=2&order=&loc=
#고등학교 별 학생수 파악

import config
import requests
from bs4 import BeautifulSoup
import time
class HighschoolStuNum:
    def __init__(self):
        #형식 : [{'region': '경기도 평택시', 'SIGUN_CD': '41220', 'schoolname': '평택여자고등학교', 'GRD1': '359', 'GRD2': '323', 'GRD3': '350', 'SumStu': '359323350'},..]
        self.all_values = []
    def getStuNum(self):
        for i in range(1,121):
            response=requests.get('https://openapi.gg.go.kr/Schoolstdntcntsecndhd?KEY={0}&pIndex={1}&pSize=100'.format(config.API_KEY_HISTUNUM, i),headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
            soup=BeautifulSoup(response.text,'html.parser')
            #페이지 별 항목 갯수
            row = soup.select('row')
            #기준년도
            STD_YY = soup.select('STD_YY')
            #시,군 코드
            SIGUN_CD = soup.select('SIGUN_CD')
            #학교가 속해있는 지역(시,구)
            Region_NM = soup.select('REGION_NM')
            #학교 이름
            SCHOOL_NM = soup.select('SCHOOL_NM')
            #학교 등급 
            SCHOOL_RK_CD = soup.select('SCHOOL_RK_CD')
            #1학년 학생수
            GRD1_CNT = soup.select('GRD1_CNT')
            #2학년 학생수
            GRD2_CNT = soup.select('GRD2_CNT')
            #3학년 학생수
            GRD3_CNT = soup.select('GRD3_CNT')
            for j in(range(0,len(row))):
                if STD_YY[j].text=='2019' and SCHOOL_RK_CD[j].text=='04': 
                        dic = {}
                        #학교가 속해있는 지역(시,구)
                        dic['region']=Region_NM[j].text
                        #학교가 속해있는 지역 코드
                        dic['SIGUN_CD']=SIGUN_CD[j].text
                        #학교 이름
                        dic['schoolname']=SCHOOL_NM[j].text
                        #1학년 수
                        dic['GRD1']=int(GRD1_CNT[j].text)
                        #2학년 수
                        dic['GRD2']=int(GRD2_CNT[j].text)
                        #3학년 수
                        dic['GRD3']=int(GRD3_CNT[j].text)
                        #총 학생수(특수학생, 유급생 미포함)
                        dic["SumStu"]=dic['GRD1']+dic['GRD2']+dic['GRD3']
                        self.all_values.append(dic)
            time.sleep(0.5)
if __name__ == "__main__":        
    a = HighschoolStuNum()
    a.getStuNum()
    #값 : 475?
    print(len(a.all_values))