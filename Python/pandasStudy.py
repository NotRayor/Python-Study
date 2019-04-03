import numpy as np
import pandas as pd
from sphinx.addnodes import index

a = [1,2,3,4,5,6]
a_array = np.array(a)
a_series = pd.Series(a)

print(a_series)

a = [[1,2,3],[4,5,6]]
a = [[1,2,3],[4,5,6]]
a_array = np.array(a)
a_series = pd.Series(a)

print(a_series)

b = pd.Series([1,3,5,np.nan, 6,8])
print(b)


#Series 인덱싱 날짜로 변경
dates = pd.date_range('20181201',  periods = 5)
a = pd.Series([10000,20000,30000,40000,50000], index = dates)

print(a)
print(a['2018-12-05'])

# index = [] 로 별도로 지정해줄 수도 있다.
mine = pd.Series([10,20,30], index = ['naver','skt','kt'])
wife = pd.Series([10,30,30], index = ['kt','naver','skt'])

print("내주식")
print(mine)
print("아내주식")
print(wife)

family = mine + wife
print(family)

#DataFrame
#2차원 형태의 자료구조..
# 딕셔너리를 아래로 펼쳐놓는 느낌이다.
raw_data = {'col0' : [1,2,3,4],
            'col1' : [10,20,30,40],
            'col2' : [100,200,300,400]}
data = pd.DataFrame(raw_data)
print(data)
print(data['col1'])

df = pd.DataFrame({ 'A' : 1,
                    'B' : pd.Timestamp('19961115'),
                    'C' : pd.Series(1, index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4, dtype='int32'),
                    'E' : pd.Categorical(['test','train','test','train']),
                    'F' : 'foo'})

print(df)
print(df.dtypes)
print(df.head(2))
print(df.tail(2))

data = {'temperature' : [29,34,36,32,30],
        'humidity' : ['mid', 'high','high','mid','low'],
        'weather' : ['cloudy','sunny','rainy','sunny','cloudy']}
print(data)

a = pd.DataFrame(data)
print(a)

#인덱스로 쓰일 날짜
date = ['2015-11-15','2015-11-16','2015-11-17','2015-11-18','2015-11-19']

#변수의 순서
features = ['temperature','humidity','weather']

b = pd.DataFrame(data, columns=features, index=date)
print(b)
print(b['temperature'])
print("\n")
print(b.loc['2015-11-15'])

# windy 항목 추가, 딕셔너리 추가하는 것처럼 하면 된다.
windy = ['yes','no','yes','yes','yes']
b['windy'] = windy
print(b)

#temperature 30도 이하, weather sunny면,
#나가서 논다는 데이터!
b['play'] = (b['temperature'] < 30) & (b['weather'] == 'sunny')
print(b)

a = pd.DataFrame(b)
print(id(a), id(b))

#Data join
A = pd.DataFrame({'color':['green','yellow','red'], 'num':[1,2,3]})
B = pd.DataFrame({'color':['green','yellow','pink'], 'size':['S','M','L']})

# A와 B 동시에 등장하는 포인트들을 조인??
C = pd.merge(left=A, right=B, how='inner')
print(C)

C = pd.merge(left=A, right=B, how='outer')
print(C)

C = pd.merge(left=A, right=B, how='left')
print(C)

C = pd.merge(left=A, right=B, how='right')
print(C)

# 파일을 읽어 표로 뿌린다!
movie_file = 'data/movie.txt'
# row 행 가로줄 , 파일의 열 column 열... 세로줄
movie_cols = ['moive_id', 'title']
movies = pd.read_table(movie_file, sep='|', header=None,
                       names=movie_cols,
                       usecols=[0,1])

print(movies.head())


import matplotlib.pylot as plt

plt.rcParams['figure.figsize'] = (4,4,)
plt.rcParams['font.size'] = 10

# basic line plot
myarray = np.array([1,2,3])








