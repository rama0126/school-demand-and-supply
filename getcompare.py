#compare.py
#지역 별 학생수와 학생수용수 비교
import csv
import numpy as np
class demand_supply():
    def __init__(self):
        #Ex : ['region','Supply','The number of highschool']
        self.readfP = []
        #Ex : ['region', 'Stu_Pop', 'city', 'district', 'town']
        self.readfS = []
        #Ex : {'화성봉담읍' : [2934, 78889]...}
        self.dedic = {}
        #{'region': '가평군', 'demand-supply': 594, 'school-pop': 23.408239700374533, 'school-stupop': 2.3408239700374533, 'schoolnum': 5}
        self.val =[]
    #엑셀파일에서 데이터 가져옴
    def getdata(self):
        #각 지역 학생수용수 정보
        fP = open (r'highschooldata\csvSupply.csv','r')
        rdr = csv.reader(fP)
        for line in rdr:
            self.readfP.append(line)
        fP.close()
        #각 시도별 학생인구
        fS = open (r'highschooldata\csvSI.csv','r')
        rdr = csv.reader(fS)
        for line in rdr:
            self.readfS.append(line)
        fS.close()
    #수요 데이터를 공급 데이터와 양식 맞춤
    def syndemand(self):
        countS = 0
        countP = 0
        countCS = 0
        countCP = 0
        countDS = 0
        countDP = 0
        forHS=0
        forHP=0
        forDS=0
        forDP=0
        dic = {}
        fS = self.readfS
        for i in range(1,len(fS)):
            
            dic[fS[i][3]]=[]
            #district(구)가 없으면 제외
            if fS[i][4]!='None':
                dic[fS[i][4]]=[]
            
            if fS[i][-1] == '장단출장소':
                dic[fS[i][3][:2]+'군내면']=[]

            else:dic[fS[i][3][:2]+fS[i][-1]]=[]

        for i in range(1,len(self.readfS)):
            #시
            if i==len(fS)-1:
                countCS+=int(fS[i][1])
                countCP+=int(fS[i][2])
                dic[fS[i][3]].append(countCS)
                dic[fS[i][3]].append(countCP)
            elif fS[i][3]==fS[i-1][3] and i!=1:
                countCS+=int(fS[i-1][1])
                countCP+=int(fS[i-1][2])
            elif fS[i][3]!=fS[i-1][3] and i!=1:
                countCS+=int(fS[i-1][1])
                countCP+=int(fS[i-1][2])
                dic[fS[i-1][3]].append(countCS)
                dic[fS[i-1][3]].append(countCP)
                countCS = 0
                countCP = 0
             #구   
            if i==len(fS)-1 and fS[i][4]!='None':
                countDS+=int(fS[i][1])
                countDP+=int(fS[i][2])
                dic[fS[i][4]].append(countDS)
                dic[fS[i][4]].append(countDP)
            elif fS[i][4]==fS[i-1][4] and i!=1 and fS[i][4]!='None'and fS[i-1][4]!='None':
                countDS+=int(fS[i-1][1])
                countDP+=int(fS[i-1][2])
            elif fS[i][4]!=fS[i-1][4] and i!=1 and fS[i][4]=='None'and fS[i-1][4]!='None':
                countDS+=int(fS[i-1][1])
                countDP+=int(fS[i-1][2])
                dic[fS[i-1][4]].append(countDS)
                dic[fS[i-1][4]].append(countDP)
                countDS = 0
                countDP = 0
            elif fS[i][4]!=fS[i-1][4] and i!=1 and fS[i][4]!='None'and fS[i-1][4]!='None':
                countDS+=int(fS[i-1][1])
                countDP+=int(fS[i-1][2])
                dic[fS[i-1][4]].append(countDS)
                dic[fS[i-1][4]].append(countDP)
                countDS = 0
                countDP = 0
              #읍,면,동  
            if fS[i][-1][-2:] in ['1동','2동','3동','4동','5동','6동','7동','8동']:
                countS += int(fS[i][1])
                countP += int(fS[i][2])
            elif fS[i][-1] == '화도읍':
                forHS += int(fS[i][1])
                forHP += int(fS[i][2]) 
            elif fS[i][-1] == '화도읍동부출장소':
                forHS += int(fS[i][1])
                forHP += int(fS[i][2])
                dic[fS[i-1][3][:2]+'화도읍'].append(forHS)
                dic[fS[i-1][3][:2]+'화도읍'].append(forHP)
           
            elif fS[i][-1] == '장단출장소':
                dic[fS[i-1][3][:2]+'군내면'].append(int(fS[i][1]))
                dic[fS[i-1][3][:2]+'군내면'].append(int(fS[i][2]))
                

            else:
                if countS==0:
                    dic[fS[i][3][:2]+fS[i][-1]].append(int(fS[i][1]))
                    dic[fS[i][3][:2]+fS[i][-1]].append(int(fS[i][2]))
                else :
                    dic[fS[i-1][3][:2]+fS[i-1][-1][:-2]+'1동'].append(countS)
                    dic[fS[i-1][3][:2]+fS[i-1][-1][:-2]+'1동'].append(countP)
                    countS=0
                    countP=0
                    dic[fS[i][3][:2]+fS[i][-1]].append(int(fS[i][1]))
                    dic[fS[i][3][:2]+fS[i][-1]].append(int(fS[i][2]))
        self.dedic = dic

#각 지역별 학교 수와 학생수용수(현재 학생수)를 구함
    def compare(self):
        #['region', 'Stu_Pop', 'Pop', 'city', 'district', 'town']
        fS = self.readfS
        #['region','Supply','The number of highschool']
        fP = self.readfP
        #{'화성봉담읍' : [2934, 78889]...}
        dedic = self.dedic
        

        #첫번째 값 제외
        val=[]
        for j in range(1,len(fP)):
        
            for i in dedic.keys():
                if i==fP[j][0] and len(dedic[i])==2:
                    dic={}
                    
                    dic['region']=fP[j][0]
                    #수요와 공급 : 학생인구 - 학생수용수 
                    dic['demand-supply']=int(dedic[i][0])-int(fP[j][1])
                    #인구수 비래 학교 수 : 학교수/인구수*10000
                    if int(fP[j][2])==0:
                        dic['school-pop']=0
                    else:
                        dic['school-pop'] = int(fP[j][2])/int(dedic[i][1])*10000
                    #학생수 비래 학교 수 : 학교수/학생수*1000
                    if int(fP[j][2])==0:
                        dic['school-stupop']=0
                    else:
                        dic['school-stupop'] = int(fP[j][2])/int(dedic[i][0])*1000
                    #학교 수
                    dic['schoolnum']=int(fP[j][2])
                    #지역 급
                    if fP[j][0][-1]=='시' or fP[j][0][-1]=='군':
                        dic['regionDiv']='City'
                    elif fP[j][0][-1]=='구':
                        dic['regionDiv']='District'
                    elif fP[j][0][-1]=='읍' or fP[j][0][-1]=='면' or fP[j][0][-1]=='동':
                        dic['regionDiv']='Town'
                    val.append(dic)
        self.val = val        
        

    def Save_data_CSV(self):
        fileWrite = open('highschooldata\csvCompare.csv', 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(fileWrite)
        for i in self.val:
            v = [i['region'],i['demand-supply'], i['school-pop'],i['school-stupop'],i['schoolnum'],i['regionDiv']]
            csvWriter.writerow(v)
        
        fileWrite.close

if __name__ == "__main__":        
    a= demand_supply()
    a.getdata()
    a.syndemand()
    a.compare()
    a.Save_data_CSV()

