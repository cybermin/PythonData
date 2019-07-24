
# coding: utf-8

# ### 주피터 노트북으로 Python 시작하기 [기본그래프 그리기]
# ### 함수

# In[1]:

file = open('도별미세먼지.csv', 'r')
data = file.readlines()

dic={}
for line in data :
    lst = line.replace('\n','').split(',')
    dic[lst[0]] = int(lst[1])

print(dic)


# In[2]:

def areaDust(dic , area) :
    return dic[area]

print('지역 선택 ')
print(list(dic.keys()))

while True :
    area = input('지역을 입력하세요(종료 q) : ')
    
    if area.lower() == 'q' : break
        
    print(area, '의 미세먼지 :', areaDust(dic, area))


# In[21]:

#기본 그래프 
import matplotlib.pyplot as plt

x = list(range(len(dic)))
y = list(dic.values())

print('\n')
print('기본 그래프')
plt.plot(y)
plt.show()


# In[22]:

#기본 그래프 - x축 표시 
#한글 폰트 사용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

print('기본 그래프2')
plt.plot(y)
plt.xticks(x, list(dic.keys()))
plt.show()


# In[5]:

#기본 그래프 - 제목 
print('기본 그래프3')
plt.plot(y, 'bo-')
plt.xticks(x, list(dic.keys()))

plt.title('지역별 미세먼지 현황')
plt.xlabel('[지역]')
plt.ylabel('미세먼지')
plt.show()


# In[6]:

#기본 그래프 - 막대 그래프
print('기본 막대 그래프')
plt.bar(x,y)
plt.xticks(x, list(dic.keys()))

plt.title('지역별 미세먼지 현황')
plt.xlabel('[지역]')
plt.ylabel('미세먼지')
plt.show()


# In[12]:

#기본 그래프 - 산점도 그래프 
print('기본 막대 그래프')
plt.scatter(x,y)
plt.xticks(x, list(dic.keys()))

plt.title('지역별 미세먼지 현황')
plt.xlabel('[지역]')
plt.ylabel('미세먼지')

#plt.ylim([0, 30])
plt.show()


# In[7]:

#기본 그래프 - 원형 그래프 
print('원형 그래프')

plt.pie(y, labels=list(dic.keys()), shadow=True, startangle=90)
plt.show()


# In[24]:

#연습문제 : 부산시기온.csv
#부산시 2017년 ~2019년까지 기온 변화 시각화 
import matplotlib

file = open('부산시기온.csv', 'r')
data = file.readlines()

day = []
tempavg = []
tempmin = []
tempmax = [] 

for line in data :
    if (line[:2] == '일시') : continue 
     
    lst = line.replace('\n','').split(',')
    day.append(lst[0])
    tempavg.append(float(lst[1]))
    tempmax.append(float(lst[2]))
    tempmin.append(float(lst[3])) 
    
file.close()

#마이너스 깨지는 경우 처리
matplotlib.rcParams['axes.unicode_minus'] = False 

x = list(range(len(day)))
plt.plot(x, tempavg, label='평균', c='r', lw=1, ls='-', marker='o')
plt.plot(x, tempmax, label='최대', c='g', lw=1, ls='-.', marker='*') 
plt.plot(x, tempmin, label='최소', c='b', lw=1, ls='--', marker='x') 

plt.xticks(x, day,rotation=90)
plt.title('부산시 2017-2019 기온 변화',fontsize=15)
plt.legend()
plt.show()


# In[ ]:




# In[ ]:



