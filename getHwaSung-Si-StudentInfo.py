#getHwaSun-Si-StudentInfo.py
#화성시 17~19세 인구수 데이터
#(구)HwStu.py
import csv
class HwStu():
    def __init__(self):
        self.readf = []
        #형식 : [{'area': '봉담읍', 'Add-area': '경기도 화성시 봉담읍', '17세': 869, '18세': 922, '19세': 1045, '총 학생수': 2836},...]
        self.all_values = []
    #엑셀파일에서 데이터 가져옴
    def getHwStu(self):
        f = open ('highschooldata\studentdata.csv','r')
        rdr = csv.reader(f)
        for line in rdr:
            self.readf.append(line)
        f.close
    #가져온 데이터 정리
    def Arrdata(self):
        count = 0
        dic={}
        for arr in self.readf:
            if len(arr[2])>3:
                arr[2]=arr[2][0]+arr[2][-3:]
            if len(arr[0])==12 and count == 0:
                #지역(읍, 면, 동 단위)
                dic['area'] = arr[0][3:6]
                #지역 주소
                dic['Add-area'] = arr[0][7:9]+'도 '+arr[0][9:11]+'시 '+arr[0][3:6]
                #17세 인구
                dic['17세'] = int(arr[2])
                count = 1
            elif len(arr[0])==12 and count == 1:
                #18세 인구
                dic['18세'] = int(arr[2])
                count = 2
            elif len(arr[0])==12 and count == 2:
                #19세 인구
                dic['19세'] = int(arr[2])
                count = 0
                #17~19세 총 인구 수
                dic['총 학생수'] = dic['17세']+dic['18세']+dic['19세']
                self.all_values.append(dic)
                dic={}
            elif len(arr[0])==13 and count == 0:
                dic['area'] = arr[0][3:7]
                dic['Add-area'] = arr[0][8:10]+'도 '+arr[0][10:12]+'시 '+arr[0][3:7]
                dic['17세'] = int(arr[2])
                count = 1
            elif len(arr[0])==13 and count == 1:
                dic['18세'] = int(arr[2])
                count = 2
            elif len(arr[0])==13 and count == 2:
                dic['19세'] = int(arr[2])
                count = 0
                dic['총 학생수'] = dic['17세']+dic['18세']+dic['19세']
                self.all_values.append(dic)
                dic={}
               

if __name__ == "__main__":
    a =HwStu()
    a.getHwStu()
    a.Arrdata()
    print(a.all_values)
    print(len(a.readf))
    print(len(a.all_values))