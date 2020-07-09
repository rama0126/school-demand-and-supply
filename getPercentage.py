#getPercentage.py
#경기도 내 각 시, 구별 고등학생/인구수 비율
#(구)Perce.py
import csv
class Percen():
    def __init__(self):
        self.readf = []
        #형식 : [{'area': '수원시', 'per': 3.93}, {'area': '수원시 장안구', 'per': 4.18},...]
        self.all_values = []
    #엑셀파일에서 데이터 가져옴
    def getPopPer(self):
        f = open (r'highschooldata\residentperstudent.csv','r')
        rdr = csv.reader(f)
        for line in rdr:
            self.readf.append(line)
        f.close
    #가져온 데이터 정리
    def Arrdata(self):
        dic={}
        for arr in self.readf:
            if len(arr[0])==9:
                #ex:수원시 권선구
                dic['region']=arr[0][6:8]+'시 '+arr[0][:3]
                #고등학생/인구 비율
                dic['per']=float(arr[1])
                self.all_values.append(dic)
                dic={}
            elif len(arr[0])==8:
                #ex:의정부시
                dic['region']=arr[0][:4]
                dic['per']=float(arr[1])
                self.all_values.append(dic)
                dic={}
            elif len(arr[0])==10:
                #ex:고양시 일산동구
                dic['region']=arr[0][7:9]+'시 '+arr[0][:4]
                dic['per']=float(arr[1])
                self.all_values.append(dic)
                dic={}
            elif len(arr[0])==7:
                #ex:화성시
                dic['region']=arr[0][:3]
                dic['per']=float(arr[1])
                self.all_values.append(dic)
                dic={}

if __name__ == "__main__":
    a = Percen()
    a.getPopPer()
    a.Arrdata()
    print(a.all_values)
    #값 : 52(경기도 포함)
    print(len(a.readf))
    #값 : 51(경기도 미포함)
    print(len(a.all_values))