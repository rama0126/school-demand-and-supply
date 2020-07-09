#getdemand.py
#지역별 학생수용가능 인원값 구하기
import csv
class demand_supply():
    def __init__(self):
        #Ex : ['schoolname', 'SIGUN_CD', 'schoolAdd', 'region', 'GRD1', 'GRD2', 'GRD3', 'SumStu', 'city', 'district', 'town']
        self.readfH = []
        #Ex : ['region', 'Stu_Pop', 'Pop', 'city', 'district', 'town']
        self.readfS = []
        self.SumHiStu = {}
        self.readfE = []
    #엑셀파일에서 데이터 가져옴
    def getdata(self):
        #각 고등학교 정보
        fH = open ('highschooldata\csvHI.csv','r')
        rdr = csv.reader(fH)
        for line in rdr:
            self.readfH.append(line)
        fH.close
        #각 시도별 학생인구
        fS = open ('highschooldata\csvSI.csv','r')
        rdr = csv.reader(fS)
        for line in rdr:
            self.readfS.append(line)
        fS.close
        
        #각 법정동 - > 행정동 정보
        fE = open (r'highschooldata\regionerror.csv','r')
        rdr = csv.reader(fE)
        for line in rdr:
            self.readfE.append(line)
        fE.close
#각 지역별 학교 수와 학생수용수(현재 학생수)를 구함
    def getsupplytown(self):
        #['region', 'Stu_Pop', 'Pop', 'city', 'district', 'town']
        fS = self.readfS
        #['schoolname', 'SIGUN_CD', 'schoolAdd', 'region', 'GRD1', 'GRD2', 'GRD3', 'SumStu', 'city', 'district', 'town']
        fH = self.readfH
        dic ={}
        fE={}
        for i in self.readfE:
            fE[i[0]]=i[1]

        #첫번째 값 제외
        for i in range(1,len(fS)):
            
            dic[fS[i][3]]=[]
            #district(구)가 없으면 제외
            if fS[i][4]!='None':
                dic[fS[i][4]]=[]

            dic[fS[i][3][:2]+fS[i][-1]]=[]
            #첫번째 값 제외
        
        #['schoolname', 'SIGUN_CD', 'schoolAdd', 'region', 'GRD1', 'GRD2', 'GRD3', 'SumStu', 'city', 'district', 'town']
        for i in range(1,len(fH)):
            #시,군
            dic[fH[i][-3]].append(fH[i][7])
            #구
            if fH[i][-2]!="None":
                dic[fH[i][-2]].append(fH[i][7])
            #읍면동
            

            #오류 법정동 < 행정동(예: 신읍동 < 포정동)
            if fH[i][-1] in fE.keys():
                #부천시 중동은 제외
                if fH[i][-1]=='중동' and fH[i][-3]=='부천시':dic[fH[i][-3][:2]+fH[i][-1]].append(fH[i][7])
                #평택시 세교동은 제외
                elif fH[i][-1]=='세교동' and fH[i][-3]=='평택시':dic[fH[i][-3][:2]+fH[i][-1]].append(fH[i][7])
                #부천시 상동은 제외
                elif fH[i][-1]=='상동' and fH[i][-3]=='부천시':dic[fH[i][-3][:2]+fH[i][-1]].append(fH[i][7])
                #이천시 안흥동은 증포동
                elif fH[i][-1]=='안흥동' and fH[i][-3]=='이천시':dic[fH[i][-3][:2]+'증포동'].append(fH[i][7])
                #안산시 부곡동은 제외
                elif fH[i][-1]=='부곡동' and fH[i][-3]=='안산시':dic[fH[i][-3][:2]+fH[i][-1]].append(fH[i][7])
                #파주시 목동은 제외
                elif fH[i][-1]=='목동' and fH[i][-3]=='파주시':dic[fH[i][-3][:2]+fH[i][-1]].append(fH[i][7])
                else:
                    dic[fH[i][-3][:2]+fE[fH[i][-1]]].append(fH[i][7])
            
            #오류 @@n동(예: 행신1동, 행신2동)의 공급은 전부 1동에 포함시킴
            elif fH[i][-3][:2]+fH[i][-1][:2]+'1동' in dic.keys():
                dic[fH[i][-3][:2]+fH[i][-1][:2]+'1동'].append(fH[i][7])
            #오류 잡기: 풍덕천1동 풍덕천2동 합침 --> 성사1동
            elif fH[i][-1]=='풍덕천동':
                dic[fH[i][-3][:2]+'풍덕천1동'].append(fH[i][7])
            #오류 잡기: 수진1동 수진2동 합침 --> 수진1동
            elif fH[i][-1]=='수진동':
                dic[fH[i][-3][:2]+'수진1동'].append(fH[i][7])
            #오류 잡기: 비전1동 비전2동 합침 --> 비전1동
            elif fH[i][-1]=='비전동':
                dic[fH[i][-3][:2]+'비전1동'].append(fH[i][7])
            #오류 잡기: 정왕본동 정왕1동 정왕2동 정왕3동 합침 --> 정왕1동
            elif fH[i][-1]=='정왕동':
                dic[fH[i][-3][:2]+'정왕1동'].append(fH[i][7])
            #오류 잡기: 행신1동 행신2동 행신3동 합침 --> 행신1동
            elif fH[i][-1]=='행신동':
                dic[fH[i][-3][:2]+'행신1동'].append(fH[i][7])
            #오류 잡기: 호원1동 호원2동 합침 --> 호원1동
            elif fH[i][-1]=='호원동':
                dic[fH[i][-3][:2]+'호원1동'].append(fH[i][7])
            #오류 잡기: 화정1동 화정2동 합침 --> 화정1동
            elif fH[i][-1]=='화정동':
                dic[fH[i][-3][:2]+'화정1동'].append(fH[i][7])
            #오류 잡기: 권선1동 권선2동 합침 --> 권선1동
            elif fH[i][-1]=='권선동':
                dic[fH[i][-3][:2]+'권선1동'].append(fH[i][7])
            #오류 잡기: 신장1동 신장2동 합침 --> 신장1동
            elif fH[i][-1]=='신장동' and fH[i][-3]=='하남시':
                dic[fH[i][-3][:2]+'신장1동'].append(fH[i][7])
            #오류 잡기: 병점1동 병점2동 합침 --> 병점1동
            elif fH[i][-1]=='병점동':
                dic[fH[i][-3][:2]+'병점1동'].append(fH[i][7])
            #오류 잡기: 의정부1동 의정부2동 합침 --> 의정부1동
            elif fH[i][-1]=='의정부동':
                dic[fH[i][-3][:2]+'의정부1동'].append(fH[i][7])
            else:
                dic[fH[i][-3][:2]+fH[i][-1]].append(fH[i][7])

        

                
        for i in dic.keys():
            Sum=0
            count = 0
            for j in dic[i]:
                Sum+=int(j)
                count += 1
            self.SumHiStu[i]=[Sum,count]
        
    def Save_data_CSV(self):
        fileWrite = open('highschooldata\csvSupply.csv', 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(fileWrite)
        csvWriter.writerow(['region','Supply','The number of highschool'])
        key = list(self.SumHiStu.keys())
        value = list(self.SumHiStu.values())
        for i in range(0,len(self.SumHiStu)):
            v = [key[i],value[i][0], value[i][1]]
            csvWriter.writerow(v)
        
        fileWrite.close


        
        
               
                
               
                
                
                    


if __name__ == "__main__":        
    a = demand_supply()
    a.getdata()
    a.getsupplytown()
    a.Save_data_CSV()