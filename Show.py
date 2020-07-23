#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np
import csv
class Show():
    def __init__(self):
        #지역
        self.arr = []
        #학생수-학생수용수
        self.sd=[]
        #인구만명당 학교수
        self.ps=[]
        #학생천명당 학교수
        self.ss=[]
        #학교수
        self.sn=[]
        #행정구역단위
        self.rd=[]
        self.compare = []
        fC = open ('highschooldata\csvCompare.csv','r')
        rdr = csv.reader(fC)
        
        for line in rdr:
            k=[]
            self.arr.append(line[0])
            k.append(int(line[1]))
            k.append(float(line[2][:5]))
            k.append(float(line[3][:5]))
            k.append(int(line[4]))
            k.append(line[5])
            self.compare.append(k)
        fC.close
        for i in self.compare:
            self.sd.append(i[0])
            self.ps.append(i[1])
            self.ss.append(i[2])
            self.sn.append(i[3])
            self.rd.append(i[4])
    
        self.df = pd.DataFrame({'학생수-학생수용수':self.sd,'인구만명당 학교수':self.ps,'학생천명당 학교수':self.ss,'학교수':self.sn,'행정구역단위':self.rd},index=self.arr)
        self.dfTown=self.df[self.df['행정구역단위'].isin(['Town'])]
        self.dfDistrict=self.df[self.df['행정구역단위'].isin(['District'])]
        self.dfCity=self.df[self.df['행정구역단위'].isin(['City'])]
#읍,면,동 지표 보기
class ShowTown(Show):
    def ShowDSMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='Town':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        #학생수 - 학생수용수 Top 10구하기
        i=[]
        sdj=sdT.copy()
        for j in range(0,10):
            k=sdj.index(max(sdj))
            sdj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(sdT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in sdT:
            sum+=i
        avg=sum/len(sdT)    
        #시각화    
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-100, 12000], xlabel='학생수-학생 수용 수', ylabel='지역',title='학생수-학교 학생 수용 수 Top10')
        
        plt.show()
    def ShowDSMin(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='Town':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        #학생수 - 학생수용수 Bot 10구하기
        i=[]
        sdj=sdT.copy()
        for j in range(0,10):
            k=sdj.index(min(sdj))
            sdj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(sdT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in sdT:
            sum+=i
        avg=sum/len(sdT)    
        #시각화    
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-6000, 600], xlabel='학생수-학생 수용 수', ylabel='지역',title='학생수-학생 수용 수 Bot 10')
        
        plt.show()
    def ShowPSMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='Town':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #인구만명당 학교수 Top10 구하기
        i=[]
        psj=psT.copy()
        for j in range(0,10):
            k=psj.index(max(psj))
            psj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(psT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in psT:
            sum+=i
        avg=sum/len(psT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.5, 20], xlabel='인구만명당 학교수', ylabel='지역',title='인구만명당 학교수 Top 10')
        
        plt.show()
    def ShowSSMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='Town':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학생천명당 학교수 Top10 구하기
        i=[]
        ssj=ssT.copy()
        for j in range(0,10):
            k=ssj.index(max(ssj))
            ssj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(ssT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in ssT:
            sum+=i
        avg=sum/len(ssT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.5, 30], xlabel='학생천명당 학교수', ylabel='지역',title='학생천명당 학교수 Top 10')
        
        plt.show()
    def ShowSNMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='Town':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학교수 Top10 구하기
        i=[]
        snj=snT.copy()
        for j in range(0,10):
            k=snj.index(max(snj))
            snj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(snT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in snT:
            sum+=i
        avg=sum/len(snT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.5, 30], xlabel='학교수', ylabel='지역',title='학교수 Top 10')
        
        plt.show()     
#구 지표 보기        
class ShowDistrict(Show):
    def ShowDSMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='District':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        #학생수 - 학생수용수 Top 5구하기
        i=[]
        sdj=sdT.copy()
        for j in range(0,5):
            k=sdj.index(max(sdj))
            sdj[k] = 0            
            i.append(k)
           
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(sdT[l])
        
        #평균값 구하기
        sum=0
        avg=0
        for i in sdT:
            sum+=i
        avg=sum/len(sdT)
        #시각화    
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows

        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        
        
        
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        
        
        ax.set(xlim=[-100, 8000], xlabel='학생수-학생 수용 수', ylabel='지역',title='학생수-학생 수용 수 Top 5')
       
        
        

        

        plt.show()
        
    def ShowDSMin(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='District':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        #학생수 - 학생수용수 Bot 5구하기
        i=[]
        sdj=sdT.copy()
        for j in range(0,5):
            k=sdj.index(min(sdj))
            sdj[k] = 200000            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(sdT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in sdT:
            sum+=i
        avg=sum/len(sdT)    
        #시각화    
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-6000, 5000], xlabel='학생수-학생 수용 수', ylabel='지역',title='학생수-학생 수용 수 Bot 5')
        
        plt.show()
    def ShowPSMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='District':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #인구만명당 학교수 Top5 구하기
        i=[]
        psj=psT.copy()
        for j in range(0,5):
            k=psj.index(max(psj))
            psj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(psT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in psT:
            sum+=i
        avg=sum/len(psT)    
        #시각화
        fig, ax = plt.subplots()
            
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.05, 0.8], xlabel='인구만명당 학교수', ylabel='지역',title='인구만명당 학교수 Top 5')
        
        plt.show()
    def ShowPSMin(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='District':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #인구만명당 학교수 Bot 5 구하기
        i=[]
        psj=psT.copy()
        for j in range(0,5):
            k=psj.index(min(psj))
            psj[k] = 100            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(psT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in psT:
            sum+=i
        avg=sum/len(psT)    
        #시각화
        fig, ax = plt.subplots()
            
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.02, 0.5], xlabel='인구만명당 학교수', ylabel='지역',title='인구만명당 학교수 Bot 5')
        
        plt.show()
    def ShowSSMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='District':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학생천명당 학교수 Top5 구하기
        i=[]
        ssj=ssT.copy()
        for j in range(0,5):
            k=ssj.index(max(ssj))
            ssj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(ssT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in ssT:
            sum+=i
        avg=sum/len(ssT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.1, 3], xlabel='학생천명당 학교수', ylabel='지역',title='학생천명당 학교수 Top 5')
        
        plt.show()
    def ShowSSMin(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='District':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학생천명당 학교수 Bot5 구하기
        i=[]
        ssj=ssT.copy()
        for j in range(0,5):
            k=ssj.index(min(ssj))
            ssj[k] = 10            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(ssT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in ssT:
            sum+=i
        avg=sum/len(ssT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.1, 1.5], xlabel='학생천명당 학교수', ylabel='지역',title='학생천명당 학교수 Bot 5')
        
        plt.show()
    def ShowSNMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='District':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학교수 Top5 구하기
        i=[]
        snj=snT.copy()
        for j in range(0,5):
            k=snj.index(max(snj))
            snj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(snT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in snT:
            sum+=i
        avg=sum/len(snT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-1, 50], xlabel='학교수', ylabel='지역',title='학교수 Top 5')
        
        plt.show()
    def ShowSNMin(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='District':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학교수 Bot5 구하기
        i=[]
        snj=snT.copy()
        for j in range(0,5):
            k=snj.index(min(snj))
            snj[k] = 100            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(snT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in snT:
            sum+=i
        avg=sum/len(snT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-1, 20], xlabel='학교수', ylabel='지역',title='학교수 Bot 5')
        
        plt.show()
#시 군 지표 보기
class ShowCity(Show):
    def ShowDSMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='City':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        #학생수 - 학생수용수 Top 10구하기
        i=[]
        sdj=sdT.copy()
        for j in range(0,10):
            k=sdj.index(max(sdj))
            sdj[k] = 0            
            i.append(k)
           
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(sdT[l])
        
        #평균값 구하기
        sum=0
        avg=0
        for i in sdT:
            sum+=i
        avg=sum/len(sdT)
        #시각화    
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows

        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        
        
        
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        
        
        ax.set(xlim=[-100, 15000], xlabel='학생수-학생 수용 수', ylabel='지역',title='학생수-학생 수용 수 Top10')
       
        
        

        

        plt.show()
        
    def ShowDSMin(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='City':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        #학생수 - 학생수용수 Bot 10구하기
        i=[]
        sdj=sdT.copy()
        for j in range(0,10):
            k=sdj.index(min(sdj))
            sdj[k] = 20000            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(sdT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in sdT:
            sum+=i
        avg=sum/len(sdT)    
        #시각화    
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-100, 5000], xlabel='학생수-학생 수용 수', ylabel='지역',title='학생수-학생 수용 수 Bot 10')
        
        plt.show()
    def ShowPSMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='City':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #인구만명당 학교수 Top10 구하기
        i=[]
        psj=psT.copy()
        for j in range(0,10):
            k=psj.index(max(psj))
            psj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(psT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in psT:
            sum+=i
        avg=sum/len(psT)    
        #시각화
        fig, ax = plt.subplots()
            
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.05, 1], xlabel='인구만명당 학교수', ylabel='지역',title='인구만명당 학교수 Top 10')
        
        plt.show()
    def ShowPSMin(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='City':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #인구만명당 학교수 Bot 10 구하기
        i=[]
        psj=psT.copy()
        for j in range(0,10):
            k=psj.index(min(psj))
            psj[k] = 100            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(psT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in psT:
            sum+=i
        avg=sum/len(psT)    
        #시각화
        fig, ax = plt.subplots()
            
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.02, 0.5], xlabel='인구만명당 학교수', ylabel='지역',title='인구만명당 학교수 Bot 10')
        
        plt.show()
    def ShowSSMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='City':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학생천명당 학교수 Top10 구하기
        i=[]
        ssj=ssT.copy()
        for j in range(0,10):
            k=ssj.index(max(ssj))
            ssj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(ssT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in ssT:
            sum+=i
        avg=sum/len(ssT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.1, 3], xlabel='학생천명당 학교수', ylabel='지역',title='학생천명당 학교수 Top 10')
        
        plt.show()
    def ShowSSMin(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='City':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학생천명당 학교수 Bot10 구하기
        i=[]
        ssj=ssT.copy()
        for j in range(0,10):
            k=ssj.index(min(ssj))
            ssj[k] = 10            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(ssT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in ssT:
            sum+=i
        avg=sum/len(ssT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-0.1, 1.5], xlabel='학생천명당 학교수', ylabel='지역',title='학생천명당 학교수 Bot 10')
        
        plt.show()
    def ShowSNMax(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='City':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학교수 Top10 구하기
        i=[]
        snj=snT.copy()
        for j in range(0,10):
            k=snj.index(max(snj))
            snj[k] = 0            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(snT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in snT:
            sum+=i
        avg=sum/len(snT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-1, 50], xlabel='학교수', ylabel='지역',title='학교수 Top 10')
        
        plt.show()
    def ShowSNMin(self):
        arrT=[]
        sdT=[]
        psT=[]
        ssT=[]
        snT=[]
        arrTpl=[]
        plT=[]
        for i in range(0,len(self.arr)):
            if self.rd[i]=='City':
                arrT.append(self.arr[i])
                sdT.append(self.sd[i])
                psT.append(self.ps[i])
                ssT.append(self.ss[i])
                snT.append(self.sn[i])
        
        #학교수 Bot10 구하기
        i=[]
        snj=snT.copy()
        for j in range(0,10):
            k=snj.index(min(snj))
            snj[k] = 100            
            i.append(k)
            
            
        for l in i:
            arrTpl.append(arrT[l])
            plT.append(snT[l])
        #평균값 구하기
        sum=0
        avg=0
        for i in snT:
            sum+=i
        avg=sum/len(snT)    
        #시각화
        fig, ax = plt.subplots()
        
        #한글로 볼려면 https://hangeul.naver.com/2017/nanum에서 다운받을 것
        plt.rc('font', family='NanumGothic') # For Windows
        # Add a vertical line, here we set the style in the function call
        ax.axvline(avg, ls='--', color='r')
        ax.barh(arrTpl, plT)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')
        ax.set(xlim=[-1, 20], xlabel='학교수', ylabel='지역',title='학교수 Bot 10')
        
        plt.show()
if __name__ == "__main__":  
    a = ShowTown()
    a.ShowDSMax()
    a.ShowDSMin()
    a.ShowPSMax()
    
    a.ShowSSMax()
    
    a.ShowSNMax()