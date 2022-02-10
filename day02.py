# 문자열이 제공하는 함수
# 파이썬의 모든 변수의 타입은 객체(instance)로 취급된다.


str01 = ''
str02 = str() #인스턴스 생성 구문
print('type - ', type(str01))

phoneNumber = "010-2623-8169"
str03 = phoneNumber.split("-") # split이라는 함수를 소유하고 있는 주체가 폰넘버라는 주체이다.
print('type - ', type(str03))
print('data -', str03)

seqTxt = "Talk is cheap. Show me the code!!"
print('seqText - type, len', type(seqTxt), len(seqTxt)) # len은 함수의 길이를 출력
print('dir - ', dir(seqTxt)) # dir은 객체가 내장하고 있는 함수를 보는 명령어
# 내장하고 있는 함수중에 __함수__ 형식으로 된 친구들이 있다. 이것들은 시퀀스 데이터이다.

# 시퀀스 데이터는 인덱싱 및 슬라이싱이 가능하다. __iter__
# [start : end -1 : step]
print(seqTxt[0]) # 인덱싱 (정해진 값만 가져오기)
print(seqTxt[0 : 4]) #슬라이싱 (범위를 줘서 값가져오기), -1이 들어가기 때문에 4글자를 가져오고 싶으면 0:4로 해야된다.
print(seqTxt[-6 : -2]) #뒤에값만 출력
print(seqTxt[-6:-1])

#만약 홀만 출력하고 싶다면?
exStr = "홀짝홀짝홀짝홀짝홀짝홀짝홀짝"
print('exStr 홀 -', exStr[::2]) #홀만 가져오기
print('exStr 홀 -',exStr[0:len(exStr):2]) #위와 같이 생략도 가능하고 지금처럼 출력도 가능
print('exStr 짝 -',exStr[1::2])
print('exStr 짝 -',exStr[::-1]) # 뒤에서부터 거꾸로

# 문자열이 가지고 있는 함수 소개
strSlicing = 'nice Python'
print('Capitalize - ', strSlicing.capitalize()) # 첫번째 letter만 대문자로 만들고 나머지는 소문자로 만드는 함수

phoneNumber = "010-2623-8169"
print('replace - ', phoneNumber.replace('-',' '))

url = 'http://www.naver.com'
# com만 출력하는 다양한 방법
print('url slicing -', url[-3:])
print('url slicing -', url[url.find('com') : ])
print('url slicing -', url.find('com')) # 17 출력
print('url slicing -', url[len(url)-3 : ])

urlLst = url.split('.')
print('urlLst type -', type(urlLst), urlLst)

companyName = '    samsong   '
print('len - ', len(companyName))
print('data - ', companyName, len(companyName.strip()), companyName.lstrip(), companyName.rstrip()) #좌우공백없애는 함수strip
#lstrip 왼쪽공백 없애기, rstrip 오른쪽 공백없애기 , 문자와 문자 사이 공백은 못없앰

#upper(), lower() 문자 전체를 대문자, 소문자로 바꾸기
print('upper -', companyName.upper())

# 확장자가 xls , xlsx 파일인지 여부를 확인하고 싶다면 ? .endswith
fileName = 'report.xls'
print(fileName.endswith(('xls','xlsx')))

# 파일 이름이 report 인지 판단하고 싶다면 ?
print('report 파일인지 여부 - ' , fileName.startswith('report'))

# 문자열 in 연산자를 이용해서 문자열을 판별할 수 있다.
frutTxt = 'apple banana fineapple mango grape melon'
print('in operator -', 'Apple'.lower() in frutTxt)

drinking = 'cocacola'
# c가 몇번 들어가는지 count, l이 몇번째에 들어가는지 find, a가 몇번째들어가는지 출력index(한개밖에 출력못함)
print(len(drinking) , drinking.count('c') , drinking.find('l') , drinking.index('a'))

'''
list(중요)
 - array 아님
 - 순서가 있음, 중복이 허용됨, 수정, 삭제가 가능
 - index는 0부터 시작
 - list 선언 방법은 2가지 대괄호와 [], 클래스로 선언 list()
 - 현업에서는 [{key : value} , {}] 현업에서는 dict 딕셔너리에 들어가는 리스트가 활용도가 높음
'''

lst = [1,2,3,4]
print('type - ' , type(lst), lst)
print('dir - ' , dir(lst)) # 얘도 인덱싱 슬라이싱 가능
print('indexing - ', lst[0])
print('slicing - ', lst[:]) #전체 슬라이싱

lst = [1,2,3,4, 'nsjung' , ['show', 'me', 'the', 'code']] # 여러가지 타입을 list에 담을 수 있다.
print(lst[-1][1:3], type(lst[-1]))

# list는 연산도 가능하다.
x = [1,2,3,4]
y = [4,5]
z = x + y
print('type -' , type(z) , z)
z[0] = 0 # z list의 첫번째 값에 0을 추가
print('type -' , type(z) , z)

#list가 가지고 있는 함수
z.append(7) # 뒤에다가 값을 추가
print('append - ', z)

z.insert(0,6) # 내가 원하는 인덱스 순서에 값을 추가
print('insert - ', z)

z.sort() # 오름차순으로 정렬
print('sort - ', z)

z.reverse() # 내림차순으로 정렬
print('reverse -', z)

z.pop(0) # 0번째 인덱스 값을 없애고 꺼냄 (잘라내기)
print('pop -', z)

del z[0]
print('del -', z)

# 인덱스 순서가 아니라 1이라는 value(값)을 의미한다. 가장처음만나는 값만 제거 여러개 지울려면 루프문 돌려야됨
z.remove(0)
print('remove -', z)

# append() & extend() 차이
lst01 = [1,2,3]
lst02 = [4,5]

lst01.append(lst02) # list를 그대로 붙여넣는다.
print('append - ', lst01)

lst01.extend(lst02) #값으로 추가한다.
print('extend - ', lst01)

# inner list
# [ [], [] ]
inner_lst = ['a', 'b', 'c']
outer_lst = [10, 3.14, True, 'string', inner_lst]
print('type -', type(outer_lst))
print('inner lst -' , type(outer_lst[-1][0]), outer_lst[-1][0])

#range() : 숫자를 순차적으로 생성해주는 객체
tmpRange = range(1, 11)
print('range -', type(tmpRange), tmpRange)
print('indexing' , tmpRange[0:2], tmpRange[1]) # 인덱싱 슬라이싱 둘 다 가능

# in
print('in - ', 11 in tmpRange)

# 제어구문, 반복구문
# for ~ in : (반복)
# if ~ in  : (조건제어)
for idx in tmpRange :
    print(idx, end='\t')
print()

import random as r     # random을 r 로 부를거야라고 정해주는거
tmpLst = []
for idx in range(5) :
    tmpLst.append(r.randint(1,5))
print('data -', tmpLst )

if 4 in tmpLst :
    print('in ok')
else :
    print('not in')

'''
list comprehension
 - list 안에 for 구문을 포함
 - 변수 = [ 실행문 for 변수 in sequence형 객체 ]
'''

x = [2,4,1,5,3]

result = []
for value in x :                  # for문을 이용한 코드
    sqrt = value ** 2
    result.append(sqrt)
print('x -', x)
print('result - ', result)

result = [value**2 for value in x] # comprehension 이용한 간결한 코드
print('comprehension - ', result)

'''
튜플(tuple)
 - 선언 : (), tuple ()
 - 순서 0 , 중복 0 , 수정 x , 삭제 x - 불변(immutable) 
 - 읽기 전용
 - indexing, slicing 가능
'''

#tpl = (3)
tpl = 1,2,3,4,5,6
print('type - ', type(tpl), tpl)
print('indexing , slicing - ', tpl[0], type(tpl[0]), tpl[0:2], type(tpl[0:2]))


# tpl[0] = 10 - error
# 캐스팅(형변환)을 통한 데이터 조작은 가능하다.
lst = list(tpl)         # 리스트형으로 바꾸는건 가능
print('tpl type - ', type(lst), lst)

lst[0] = 10
tpl = tuple(lst)                # 다시 튜플로 바꾸기
print('tpl type - ', type(tpl), tpl)


#for value in range(2,100,2) :
#   print(value)

even_data = tuple(range(2, 100, 2))
print('type - ', type(even_data), even_data)

# packing & unpacking
packing = ('이지희', '변윤섭', '장성원', '정남선', '노희명')  # packing
x1, x2, x3, x4, x5 = packing                            # unpacking 패킹 데이타를 각각의 변수에 할당하는거
# x1, x2, x3, *x4 = packing 또는 x1, x2, *x3, x4 = packing  <- *(에스트리크)에 할당한다 남은 값들을,
# 이러면 패킹된 값과 변수값의 수가 일치 하지 않아도 저장됨, 저장된 값들은 list형식으로 저장
print('type - ', x1, x2, x3, x4, x5)