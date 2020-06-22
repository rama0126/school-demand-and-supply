#URL : https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=YB0SYA9FJYDF279AS9AQ20544808&infSeq=3&order=&loc=&searchWord=%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90+%ED%98%84%ED%99%A9
#API : https://openapi.gg.go.kr/HgschlM?
#경기도 고등학교 현황
import config
import requests
from bs4 import BeautifulSoup
import time
class HighschoolInfo:
    def __init__(self):
        #형식 : [{'schoolname': '가평고등학교', 'SIGUN_CD': '41820', 'schoolAdd': '경기도 가평군 가평읍 대곡리 113번지'},...]
        self.all_values = []
        
    def getSchoolInfo(self):
        for i in range(1,6):
            response=requests.get('https://openapi.gg.go.kr/HgschlM?KEY={0}&pIndex={1}&pSize=100'.format(config.API_KEY_HIGHINFO, i),headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
            soup=BeautifulSoup(response.text,'html.parser')
            row = soup.select('row')
            schoolname=soup.select('FACLT_NM')
            SIGUN_CD = soup.select('SIGUN_CD')
            SIGUN_NM = soup.select('SIGUN_NM')
            REFINE_LOTNO_ADDR = soup.select('REFINE_LOTNO_ADDR')
            for j in(range(0,len(row))):
                dic = {}
                #학교 이름
                dic['schoolname']=schoolname[j].text
                #학교가 속해있는 지역
                dic['region']=SIGUN_NM[j].text
                #학교가 속해있는 지역 코드
                dic['SIGUN_CD']=SIGUN_CD[j].text
                #학교 주소
                dic['schoolAdd']=REFINE_LOTNO_ADDR[j].text
                self.all_values.append(dic)
            time.sleep(0.5)

if __name__ == "__main__":        
    a = RegionCode()
    a.getSchoolInfo()
    a.SIGUN_CD_Synchro()
    print(a.all_values)
    #값 :474
    print(len(a.all_values))
    print(a.SIGUN_CD_ADD)
