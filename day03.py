# 파이썬은 모든 변수를 객체로 취급한다.
# dictionary 에 대해 배웁니다. 범용적으로 가장 많이 사용
# [] -> list도 많이 쓰지만 [{}] list 안에 딕셔너리를 많이 씁니다.
# [{key : value}, {}] <- 이런식으로 dict을 많이 씁니다.
# 선언 : {key : value} , dict()
# 슬라이싱이과 같은 문법은 안통함
# 딕셔너리는 시퀀스가 아니기 때문에 순서가 없다.
# 순서 X, 키 중복 X, 수정 O, 삭제 O

tmpDict = {
    'name' : 'nsjung' ,
    'phone': '01026238169' ,
    'birth': '930409'
}
print('type -', type(tmpDict), tmpDict)

# in 연산자 - 키 유무를 확인
print('key 검사 -', 'name' in tmpDict)

tmpDict = {
    '메로나' : [300, 20],  # value를 list형태로 넣음 가격, 수량
    '비비빅' : [400, 20],
    '죠스바' : [100, 50]
}
# 메로나의 가격정보를 확인하고 싶으면 ? key에 있는 가격 정보를 확인
print('메로나의 가격은 {}입니다.'.format(tmpDict['메로나'][0])) # format으로 표현 가능
print('메로나의 수량은 {}개 입니다.'.format(tmpDict['메로나'][1]))

# 새로운 데이터를 추가하고 싶다면 ?
tmpDict['메로나'] = [500, 50]
print('data - ', tmpDict)

# 메로나의 가격을 10% 인상하고 싶다면 ?
melonaLst = tmpDict['메로나']
print('melona value - ', type(melonaLst), melonaLst)
melonaLst[0] = melonaLst[0] * 1.1
print('data -', tmpDict)

tmpDict = {
    'Name'      : '섭섭해' ,
    'City'      : 'Seoul' ,
    'Age'       : 50 ,
    'Grade'     : 'A+' ,
    'Status'    : True
}
# key값 수정
tmpDict['Name'] = '정남선'
print('data -', tmpDict)

#key값 확인
print('print - ', tmpDict['Name'])

# 함수 형식으로 만들려면 아래와 같이 list가 튜플 안에 들어가는 형식으로 만들어줘야 한다. 문법임
# case 02.
tmpDict = dict([
    ('city','seoul'), ('age', 50)   
])

print('type -', type(tmpDict), tmpDict)

# case 03, 이런식으로 만들면 콜론 안쓰고 = 을 써야됨
tmpDict = dict(
    city    = 'seoul' ,
    age     = 50
)
print('type - ', type(tmpDict), tmpDict)
print('key를 이용한 값 출력 - ', tmpDict['city'])
print('key를 이용한 값 출력 - ', tmpDict.get('Age', 'dafault')) # Age가 없으면 dafault 출력
# get함수 사용, 이꼴(=)을 쓸때는 변수형 식으로 되기 때문에 key 값을 이용한 출력 가능
# 그리고 해당 값이 없을때 오류가 나지 않는다. none 이라고 뜸

tmpDict['name'] = '정남선' # 키가 동일하면 insert 와 같은 기능
tmpDict.update({'name' : '정남선'}) # update 함수를 사용해서 윗줄과 동일하게 가능
print('data - ', tmpDict)

# zip() 함수, 각각의 데이터 타입을 하나로 모을 수 있음
# case 04
keys = ('apple', 'pear', 'peach')
values = (1000, 1500, 2000)

zipDict = dict(zip(keys, values)) # 전제조건 : len가 맞아야됨, 그리고 zip으로 묶으면 16진수로 표현되기 때문에 dict로 묶어야됨
print('type - ', type(zipDict), zipDict)

# 만약 zip이라는 함수가 없었따면 ? 아래와 같이 짜야된다.
zipDict = {}
for idx in range(len(keys)) :
    zipDict[keys[idx]] = values[idx]
print('type - ', type(zipDict), zipDict)

# dictionary를 루프를 돌리고 싶다면?
# dict - keys(), values(), items() 를 쓰면 된다.

for key in zipDict.keys() :              # 키값을 이용해 값 꺼내기
    print('{} : {}'.format(key, zipDict.get(key)))
for value in zipDict.values():           # 값만 꺼내기
    print(value)
for key , value in zipDict.items() :     # 키, 값 다 꺼내기
    print('{} : {}'.format(key, value))

# pop 데이터를 없애고 빼기
print('pop - ', zipDict.pop('apple'))
print('data - ', zipDict)

zipDict.clear()
print('clear - ', zipDict)

# dict는 len만 맞으면 리스트형, 튜플형 둘다 다된다. 혼합도 된다.



'''
set : 집합의 자료형
 - 선언 : {} , set()
 - 순서 x, 중복 x
 - 인덱싱, 슬라이싱 x
'''

tmpSet = {1,2,3,3,3,3,'nsjuns'} # key value '이런식' 의 값이 안들어가 있으면(1,2,3) set이다.

print('type -', type(tmpSet), tmpSet)
# iter가 있기 때문에 순서는 없지만 루프문은 돌릴 수 있다. 하지만 인덱싱은 할 수 없음

gender = ['남','남','여','남','남','여','남','남','여']
sgender = set(gender)
print('중복 제거 -', type(sgender) , sgender)

set01 = set('nsjung')
print(set01)

set02 = set([1,2,3,4,5])
set03 = set([3,4,5,6,7])

print('intersection - ' , set02.intersection(set03)) # 겹치는 것만 출력 (교집합)
print('union -', set02.union(set03)) # 합집합
print('difference - ', set02.difference(set03)) # 차집합
set02.add(6)
print('add - ', set02) # 6 추가

set02.update([7,8])     # 복수의 값 추가
print('update - ', set02)

set02.remove(6)     # 특정값 삭제
print('remove - ' , set02)

set02.clear()
print('clear - ' , set02)

'''
boolean Type
- True | False
- 논리연산자(not, and, or) 
- 비교연산자(~, &, |)
- "" , [], (), {}, 0, None -> boolean에서는 false 값으로 판단
'''

print('boolean - ', bool(0))
print('boolean - ', type([]), bool([])) # 캐스팅을 사용할 수 있따.

trueFlag = True
falseFlag = False
#논리곱 and &
print('T and T - ' , trueFlag & trueFlag)
print('T and F - ' , trueFlag and falseFlag)
print('F and T - ' , falseFlag and trueFlag)
print('F and F - ' , falseFlag and falseFlag)
print()
#논리합 or |
print('T and T - ' , trueFlag | trueFlag)
print('T and F - ' , trueFlag or falseFlag)
print('F and T - ' , falseFlag or trueFlag)
print('F and F - ' , falseFlag or falseFlag)

print('not - ' , not trueFlag)
print('int - ' , int(trueFlag))
print('int - ' , int(falseFlag))

'''
날짜

'''

from datetime import date, datetime, timedelta      # timedelta는 시간 조절
from dateutil.relativedelta import relativedelta    #relativedelta는 날짜 조절
from dateutil.parser import  parse

# timedelta -> week, day, hour, minute, second
# relativedelta -> year, month
#특정한 날짜를 생성하고 싶으면 ? parse

today = date.today()
print('type - ', type(today), today)
print(today.year, today.month, today.day)

day_time = datetime.today()
print('type - ', type(day_time), day_time)
print(day_time.hour, day_time.minute, day_time.second, day_time.microsecond)

# pip install python-dateutil
# conda install python-dateutil

today   = date.today()
day     = timedelta(days=-1)
print('하루 전 날짜 - ', type(today), type(day) , today+day)

today   = date.today()
day     = relativedelta(months=-2)
print('두 달 전 날짜 - ' , type(today) , type(day), today+day)

myDate = parse("2022-01-27")
print('type - ' , type(myDate) , myDate)

myDate = datetime(2019, 12, 25)
print('type - ' , type(myDate) , myDate)

# 날짜 타입을 문자열 포맷으로 지정할 수 있다 %m %d %y , %h %m %s
# strftime (날짜 -> 문자) , strptime (문자 -> 날짜)
print('format - ' , myDate.strftime("%m-%d-%y"))
print('format - ' , type(myDate.strftime("%m-%d-%y")) , myDate.strftime('%m-%d-%y'))
str = '2019-12-25'
print('문자 -> 날짜 - ' , type(datetime.strptime(str, '%Y-%m-%d')))

'''
사용자 입력
-input()
'''
name = input('Enter your Namae : ')
age = int(input('Enter your Age : '))
height = float(input('Enter your Height : '))
marriage = bool(input('Enter your Marriage :'))
print('input Name - ' , type(name) , name )
print('input Age - ' , type(age) , age )
print('input Height - ' , type(height) , height )
print('input Marriage - ' , type(marriage) , marriage )
print('end-------------------------------------')


