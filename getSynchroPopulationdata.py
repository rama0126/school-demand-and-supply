#getSynchroPopulationdata.py
#popul.py와 Perce.py에서 얻은 데이터를 통해 지역별 고등학생수 유추
import getPopulation as Pop
import getPercentage as Per
import csv
class synchro_Pop_Per():
    def __init__(self):
        self.Po = Pop.PopulationInfo()
        self.Po.getPopInfo()
        self.Pe = Per.Percen()
        self.Po_all_values=self.Po.all_values
        self.Pe.getPopPer()
        self.Pe.Arrdata()
        self.Pe_all_values=self.Pe.all_values
        #Ex : [{'region': '경기도 수원시 팔달구 화서1동', 'Stu_Pop': 776},...]
        self.synchro_values = []
    def synchro(self):
        index_r = []
        count=[]
        dic={}
        idd=''
    
        #지역별 같은 구, 시, 군의 인덱스값 묶기
        for r in range(0,len(self.Po_all_values)):
            if self.Po_all_values[r]['ADMZONE_DIV_NM']=='시군'or self.Po_all_values[r]['ADMZONE_DIV_NM']=='구':
                index_r.append(count)
                count=[]
                idd = str(self.Po_all_values[r]['LEGALDONG_CD'])[:5]
            if self.Po_all_values[r]['ADMZONE_DIV_NM']=='읍면동':
                if r>=1 and str(self.Po_all_values[r]['LEGALDONG_CD'])[:5]==idd:
                    count.append(r)
            if r==len(self.Po_all_values)-1:
                index_r.append(count)
        #찾은 인덱스값 리스트 딕셔너리화
        for i in index_r:
            try:
                dic[self.Po_all_values[i[0]-1]['region']]=i
            except IndexError:
                pass       
        #Perce.py의 값과 popul.py값을 가지고 지역별 고등학생수 구함
        for d in list(dic.keys()):
            for p in self.Pe_all_values:
                if p['region']==d[4:]:
                    
                    for ii in dic[d]:
                        diic={}
                        diic['region']=self.Po_all_values[ii]['region']
                        diic['Stu_Pop']=int(self.Po_all_values[ii]['population']*(p['per']/100))
                        self.synchro_values.append(diic)
    #csv파일로 저장
    def Save_data_CSV(self):
        values = self.synchro_values
        for i in values:
            a = i['region'].split(' ')
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
    
        #csv파일로 저장
        fileWrite = open('highschooldata\csvSI.csv', 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(fileWrite)
        k=values[8].keys()
        csvWriter.writerow(k)
        for i in values:
            j = i.values()
            csvWriter.writerow(j)
        fileWrite.close
        print(values)


    def synchro_data_Save_TXT(self):
        #StudentPopulation.txt로 데이터 저장
        f = open("highschooldata\StudentPopulation.txt", 'w')
        for i in self.synchro_values:
            f.write('{0}\n'.format(i))
        f.close()
        
if __name__ == "__main__":        
    a = synchro_Pop_Per()
    a.synchro()
    a.synchro_data_Save_TXT()
    a.Save_data_CSV()
    print(a.synchro_values)
    #값:547
    print(len(a.synchro_values))