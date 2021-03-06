#getSynchroHischooldata.py
#getHighschoolInfo(HiIn.py)와 getStudentsNum.py(StuNum.py)에서 얻은 데이터 통합
#(구) SynHidata.py
import getHighschoolInfo as HI
import getStudentsNum as HN
import csv
class synchro_HighInfo_Add():
    def __init__(self):
        self.Hn = HN.HighschoolStuNum()
        self.Hn.getStuNum()
        self.Hi = HI.HighschoolInfo()
        self.Hi.getSchoolInfo()
        self.synchro_values = []
    def synchro(self):
        for i in self.Hn.all_values:
            for j in self.Hi.all_values:
                if i['schoolname'] == j['schoolname']:
                    dic = {}
                    dic['schoolname'] = i['schoolname']
                    dic['SIGUN_CD'] = i['SIGUN_CD']
                    dic['schoolAdd'] = j['schoolAdd']
                    dic['region']=i['region']
                        #1학년생 수
                    dic['GRD1']=i['GRD1']
                        #2학년생 수
                    dic['GRD2']=i['GRD2']
                        #3학년생 수
                    dic['GRD3']=i['GRD3']
                        #총 학생 수(유급생, 특수학생 제외)
                    dic['SumStu']=i['SumStu']
                    self.synchro_values.append(dic)
                    break
    def synchro_data_Save_TXT(self):
        #HighschoolData.txt로 데이터 저장
        f = open("highschooldata\HighschoolData.txt", 'w')
        for i in self.synchro_values:
            f.write('{0}\n'.format(i))
        f.close()
        #에러찾기
    def FindError(self):
        Num = self.Hn.all_values
        Add = self.Hi.all_values
        NumCInd = []
        AddCInd = []
        AddNaLi=[]
        NumNaLi=[]
        numbersAd=[]
        numbersNu=[]
        for i in range(0,len(Num)):
            NumNaLi.append(Num[i]['schoolname'])
            for j in range(0,len(Add)):
                AddNaLi.append(Add[j]['schoolname'])
                if Num[i]['schoolname']==Add[j]['schoolname']:
                    NumCInd.append(i)
                    AddCInd.append(j)
        AddCInd.sort()
        NumCInd.sort()
        for l in range(0,475):
            numbersAd.append(l)
        for n in range(0,474):
            numbersNu.append(n)
        s1 = set(AddCInd)
        s2 = set(numbersAd)
        AddEInd = list(s2-s1)
        AddEInd.sort()
        s1 = set(NumCInd)
        s2 = set(numbersNu)
        NumEInd = list(s2-s1)
        NumEInd.sort()
        # for m in AddEInd:
        #     print("{0}, AddNaLi Index:{1}".format(AddNaLi[m], m))
        # print("________________")

        # 
        # for o in NumEInd:
        #     print("{0}, NumNaLi Index:{1}".format(NumNaLi[o], o))
        # 값:
        # 광명공업고등학교, AddNaLi Index:8
        # 수원전산여자고등학교, AddNaLi Index:139
        # 홍천고등학교, AddNaLi Index:218
        # 산본공업고등학교, AddNaLi Index:333
        # 경기글로벌통상고등학교, AddNaLi Index:355
        # 근명여자정보고등학교, AddNaLi Index:359
        # 시화공업고등학교, AddNaLi Index:429
        # 가평고등학교, AddNaLi Index:474
        # ________________
        # 용인홍천고등학교, NumNaLi Index:118
        # 경기폴리텍고등학교, NumNaLi Index:157
        # 한봄고등학교, NumNaLi Index:215
        # 경기스마트고등학교, NumNaLi Index:222
        # 경기게임마이스터고등학교, NumNaLi Index:338
        # 경기항공고등학교, NumNaLi Index:344
        # 근명고등학교, NumNaLi Index:357
        # 정현고등학교, NumNaLi Index:416

        #Error: (직접 인터넷에 쳐봄)
        Errors = []
        #광명공업고등학교 ==> 경기항공고등학교 AddNaLi[8]=NumNaLi[344]
        Errors.append([344,8])
        #수원전산여자고등학교 ==> 한봄고등학교 AddNaLi[139]=NumNaLi[215]
        Errors.append([215,139])
        #홍천고등학교 ==> 용인홍천고등학교 AddNaLi[218]=NumNaLi[118]
        Errors.append([118,218])
        #산본공업고등학교 ==> 경기폴리텍고등학교 AddNaLi[333]=NumNaLi[157]
        Errors.append([157,333])
        #경기글로벌통상고등학교 ==> 경기게임마이스터고등학교 AddNaLi[355]=NumNaLi[338]
        Errors.append([338,355])
        #근명여자정보고등학교 ==> 근명고등학교 AddNaLi[359]=NumNaLi[357]
        Errors.append([357,359])
        #시화공업고등학교 ==> 경기스마트고등학교 AddNaLi[429]=NumNaLi[222]
        Errors.append([222,429])
        for [i,j] in Errors: 
            dic = {}
            dic['schoolname'] = Num[i]['schoolname']
            dic['SIGUN_CD'] = Num[i]['SIGUN_CD']
            dic['schoolAdd'] = Add[j]['schoolAdd']
            dic['region']=Num[i]['region']
            #1학년생 수
            dic['GRD1']=Num[i]['GRD1']
            #2학년생 수
            dic['GRD2']=Num[i]['GRD2']
            #3학년생 수
            dic['GRD3']=Num[i]['GRD3']
            #총 학생 수(유급생, 특수학생 제외)
            dic['SumStu']=Num[i]['SumStu']
            self.synchro_values.append(dic)
        

        #정현고등학교 NumNaLi[416] Add:경기도 화성시 산척동 산133-1
        dic = {}
        dic['schoolname'] = Num[416]['schoolname']
        dic['SIGUN_CD'] = Num[416]['SIGUN_CD']
        dic['schoolAdd'] = '경기도 화성시 산척동 산133-1'
        dic['region']= Num[416]['region']
        #1학년생 수
        dic['GRD1']=Num[416]['GRD1']
        #2학년생 수
        dic['GRD2']=Num[416]['GRD2']
        #3학년생 수
        dic['GRD3']=Num[416]['GRD3']
        #총 학생 수(유급생, 특수학생 제외)
        dic['SumStu']=Num[416]['SumStu']
        self.synchro_values.append(dic)
    
    #csv파일로 저장
    def Save_data_CSV(self):
        values=self.synchro_values
        for i in values:
            a = i['schoolAdd'].split(' ')
            #행정구역 단위 : 시,군
            i['city']=a[1]
            if i['city'] in ['고양시', '성남시', '수원시', '용인시', '안산시', '안양시']:
                #행정구역 단위 : 구
                i['district'] = a[2]
                #행정구역 단위 : 읍면동
                i['town'] = a[3]
                
            else:
                #행정구역 단위 : 구, '구'가 없으므로 'None'표시
                i['district'] = 'None'
                #행정구역 단위 : 읍면동
                i['town'] = a[2]
        #values = [{'schoolname': '효성고등학교', 'SIGUN_CD': '41130', 'schoolAdd': '경기도 성남시 수정구 심곡동 321번지 효성 고등학교', 'region': '경기도 성남시 수정구', 'GRD1': 220, 'GRD2': 206, 'GRD3': 253, 'SumStu': 679, 'city': '성남시', 'district': '수정구', 'town': '심곡동'},
            
        #csv파일로 저장    
        fileWrite = open('highschooldata\csvHI.csv', 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(fileWrite)
        k=values[3].keys()
        csvWriter.writerow(k)
        for i in values:
            j = i.values()
            csvWriter.writerow(j)
        fileWrite.close
if __name__ == "__main__":        
    a = synchro_HighInfo_Add()
    a.synchro()
    a.FindError()
    a.synchro_data_Save_TXT()
    a.Save_data_CSV()
    