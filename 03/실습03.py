#%%
f = open('C:/강의자료/2019-1학기/통계학과특강/work/03/data/20190724102105.csv')
data = f.readlines()
f.close()

#%%
df = {}
for line in data :
    if line[0:2] == '일시' : 
        print(line[0:2])
        continue

    line = line.replace('\n', '')
    item = line.split(',')
    df[item[0]] = float(item[1])

print(df)

#%%
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

x = list(range(len(df)))
x2 = df.keys()
y = [int(i) for i in df.values()]

plt.plot(x,y,c='r', lw=2, ls=':', marker='x')
plt.title('부산시 강수량 현황')
plt.xticks(x, x2, rotation=90)
plt.xlabel('년도')
plt.ylabel('강수량')

#%%
plt.bar(x,y)
plt.xticks(x, x2, rotation=90)
plt.title('부산시 강수량 현황')

#%%
plt.barh(x,y)

#%%
plt.pie(y, labels=x2)

#%%

plt.scatter(x,y)
plt.xticks(x,x2, rotation=90)
plt.ylim([0,2500])