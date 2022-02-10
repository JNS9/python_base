

''' 1
윤년의 조건
- 4의 배수이고 100의 배수가 아니거나 400의 배수일 때

'''
import random

''' 2
input() 함수를 이용해서 연도와 월을 입력받아
해당년도가 윤년일 경우 2월 달의 마지막일은 29
평년일 경우 2월 달의 마지막일은 28일 
출력 형식 : xxxx년 xx월 마지막일은 xx일 입니다.
'''

# year = int(input("연도를 입력하세요."))
# month = int(input("월을 입력하세요."))
# m = [1, 3, 5, 7, 8, 10, 12]
# if month == 2 :
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
#         print("{} 월 {} 일은 29일 입니다.".format(year, month))
#     else :
#         print("{} 월 {} 일은 28일 입니다.".format(year, month))
# elif month in m :
#     print("{} 월 {} 일은 31일 입니다.".format(year, month))
# else :
#     print("{} 월 {} 일은 30일 입니다.".format(year, month))


# 3 다중 조건문
# 100 ~ 85 : '우수' , 84 ~ 70 : '보통' , 69 이하 : '저조' <- 조건이 2개를 초과할 때
# if ~ elif ~ else 를 사용할 수 있다.

score = 85
if score >= 85 :
    print('우수')
elif 85 > score or score >= 70 :
    print('보통')
else :
    print('저조')


# 4 ,  3항 연산자
# 변수 = '참' if (조건식) else '거짓'
# 숫자가 6 이상일 때 2를 곱하고 5 이하일 때 2를 더하는 구문을 만드세요

#num = int(input())
#result = num * 2 if num >= 5 else num + 2
#print(result)

#num = int(input())
#if num >= 5 :
#    result = num * 2
#elif num < 5 :
#    result = num + 2

#print(result)



# 5 키값이 아니라 밸류값을 가져오고 싶을 때 values
tmpDict = {
    'name' : 'nsjung' ,
    'city' : 'seoul' ,
    'grade': 'A'
}

print('name' in tmpDict)
print('nsjung' in tmpDict.values())

# 6 시간이 입력되었을 때 입력된 시간이 정각인지 아닌지를 구분하고 싶다면 ?
# 14:12 , 12:00
# time = '14:13'

#time = int(input.split(':'))
time = '14:12'
if time.endswith('00') :
    print('정각입니다.')
else :
    print('정각이 아닙니다.')

# 7
# 011 SK, 016 KTF , 019 , LGU
# 011-1234-1234
# 통신사 번호를 식별하고 싶다면 ?

phoneNumber = ('011-1234-1234')
result = 'SK' if phoneNumber.startswith('011') else 'KTF' if phoneNumber.startswith('016') else 'LGU' if phoneNumber.startswith('019') else '식별할 수 없습니다.'
print(result)

if phoneNumber.startswith('011') :
    print('SK')
elif phoneNumber.startswith('016') :
    print('KTF')
elif phoneNumber.startswith('019') :
    print('LGU')
else :
    print('식별할 수 없습니다.')

# 8 변수 = '참' if (조건) else '거짓' if (조건) else '거짓'
# 주민번호 > 성별 > xxxxxx - 1xxxxxx 1,3 남자 , 2,4 여자

# idnum = '930409-4xxxxxx'
# gender = idnum.split('-')[1]
# result = '남자' if gender[0] == '1' or gender[0] =='3' else '여자' if gender[0] == '2' or gender[0] =='4' else '식별 불가'
# print(result)

# idnum = '930409-2xxxxxx'
# gender = idnum.split('-')[1]
# if gender[0] == '1' or gender[0] == '3' :
#     print('남자입니다.')
# elif gender[0] == '2' or gender[0] == '4' :
#     print('여자입니다.')
# else :
#     print('식별할 수 없습니다.')

# 주민번호 >> 성별 >> xxxxxx-1xxxxxx 1,3-남 2,4-여
# 지역코드 00~08 : 서울지역

idnum = '930409-1061111'

gender = idnum.split('-')[1]
result = '남자' if gender[0] == '1' or gender[0] == '3' else '여자'
location = '서울' if int(gender[1:3]) in range(0,9) else '지방'
print(result, location)

# 9 숫자 넣기 게임
# from random import randint
# answer = random.randint(1, 100)
# print('answer - ', answer)
# guess = int(input('1 ~
# 10 번의 기회를 주면서 숫자를 맞추는 게임을 만드세요
# 입력값이 숫자보다 높으면 숫자보다 높습니다. 출력
# 낮으면 낮다고 출력, 맞추면 맞췄습니다. 시도횟수 = 라고 출력

#from random import randint
#answer = random.randint(1, 100)
#print(type(answer))
#print(answer)

#tries = 0
#while tries < 10 :
#    tries += 1
#    print(tries)
#    guess = int(input('1 ~ 100 사이 숫자를 입력하세요'))
#    if guess == answer or tries == 10 :
#        break
#    elif guess > answer :
#        print('더 작은 숫자를 입력해주세요')
#    else :
#        print('더 큰 숫자를 입력해주세요')
#print('정답 : {} , 시도횟수 : {}'.format(answer, tries))

'''
파이썬 반복문 : for ~, while 
 - break , continue 를 이용해 반복구문에서 다른 작업을 할 수 있다.
 - for 변수 in <열거형> : <- 튜플 딕셔너리 리스트 레인지 등 블럭만드는 변수
    <loop body>
 - for ~
   else : 
 - for(초기식 : 조건식 : 증감식) {
    <loop body>
  }

 초기식 선언
 - while(조건식) {
    <loop body>
    초기식 증감
   }

'''

# 1에서 10 사이 정수를 홀수만 출력해보기

for idx in range(1,10,2) :
    if idx < 10 :
        print(idx)
    else :
        break


# 성적 5번 입력받고 평균 구하기

scores = [55, 70, 60, 90, 40]
for idx in range(len(scores)) :
    print(scores[idx], end='\t')
print()
sum = 0
for el in scores :
    sum += el
    average = sum / len(scores)
print(sum, average)

# 반려견 이름 입력 받기 , exit 이면 탈출 하고 그때까지 쓴 내용 출력

# dogNames = []
# while True :
#     if 'exit' not in dogNames :
#         name = dogNames.append(input('이름 입력'))
#     else :
#         break
# print(dogNames)

# 올림픽 4년 마다 개최 2020년에서 2050년 올림픽이 개최되는 년도를 한 줄에 5개씩 출력

# olympic = range(2020,2050)

# value = []
# for idx in range(2020,2050,4) :
#     # if idx % 4 == 0 :
#     value.append(idx)
# print(value)

cnt = 0
for year in range(2000, 2051, 4) :
    cnt += 1
    if cnt%5 == 0 :
        print(year , end = '\n')
    else :
        print(year , end = '\t')


# 1부터 9까지의 숫자 중 2의 배수만 제곱해서 출력

tmpLst = [1,2,3,4,5,6,7,8,9,10]
lst = []
for idx in tmpLst :
    if idx % 2 == 0 :
        idx = lst.append(idx)
print(lst)


# 위 문제를 3항 연산자로 만들기

tmplst = [1,2,3,4,5,6,7,8,9,10]
LLst = []
Lst = [LLst.append(idx) for idx in tmplst if idx % 2 == 0]
print(LLst)

# 세 글자 이상인 문자만 출력
tmpLst = ['I', 'am', 'studying', 'PYTHON', 'language', '!!']
lst = []
for data in tmpLst :
    if len(data) >= 3 :
        lst.append(data)
print(lst)

# 대문자만 출력

lst = []
for data in tmpLst :
    if data.isupper() :
        lst.append(data)
print(lst)

# 확장자를 제외하고 파일 이름만 출력
tmpLst = ['greeting.py' ,
          'ex01.py',
          'intor.hwp',
          'bigdata.doc',
          'machine_learning.jupyter']

lst = []
for data in tmpLst :
    lst.append(data.split('.')[0])
print(lst)

tmpSet = {1,2,3,}
tmpSSet = {'name' : 'nsjung'}
print(type(tmpSet), type(tmpSSet))

set02 = set([1,2,3,4,5])
set03 = set([3,4,5,6,7])

print(set02.intersection(set03))
print(set02.union(set03))
print(set02.difference(set03))

set02.add(6)
print(set02)
set02.update([7,8,9,10])
print(set02)
set02.clear()
print(set02)


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



from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

today = date.today()
print(type(today), today)
print(today.year, today.month, today.day)

day_time = datetime.today()
print(type(day_time), day_time)
