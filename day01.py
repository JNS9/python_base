# 주석문
# 모듈(함수 + 변수)
# library

# 기본출력 구문 - print()
print('Python Starting...')
print()
print('''우리는 파이썬 기본 문법을 배우고 있습니다
추후에 진행될 데이터 사이언스 및 인공지능을 위한 과정이고
전, 파이썬을 사랑합니다...''') # 멀티라인 커맨드를잡을때 ''' 세개를 사용
print()
print("namsun's Python~~") # " 중간에 문자열을 쓰고 싶으면 더블커텐션 사용
print('speak out. "student" ') # 더블커텐션을 포함한 문자열을 쓰고 싶으면 싱글커테션(')을 사용
print()
print("오늘은","혈맥강사를","만나서","파이썬을","배웁니다~~~") # 중간에 데이터를 구분해서 출력 가능(")사용시


print('P','Y','T','H','O','N', sep='')
#separator option 을 사용하면 데이터가 공백 없이 붙어서 나옴,
print('010','2623','8169', sep='-')  # 글자 사이에 구분자를 넣을 수도 있음
print('same0525','naver.com',sep='@')

# end option (두 줄 이상의 print 문을 한 줄로 출력하고 싶을 때, 다음에 오는 문장을 붙여줌)
print('welcome To',end='')
print('namsun World')

# file option ( 출력 결과를 콘솔에 출력 하지 않고 파일에 출력)

# format 사용(d, s, f) -> 쓰는 순서대로 할당, 옵션으로 순서를 지정할 수도 있음
print('남선님의 나이는 : {} 이고 성별은 {} 입니다.'.format(30, '남자'))
print('남선님의 나이는 : {1} 이고 성별은 {0} 입니다.'.format('남자', 30))

# format 사용(%d, %s, %f) -> f(실수) ,s(문자열), %d(정수)
print('남선님의 나이는 : %d 이고 성별은 %s 입니다.' % (30, '남자'))

# 자리수 지정!!
print('%10s' % ('nice' , ))  # 총 10자 앞에서 6글자 띄고 4글자 쓰는듯
print('%-10s' % ('nice' , )) #뒤부터 10자 출력
print('%5s' % ('pythonstudy' , ))  # 문자열은 5자리로 절삭안됨
print('%.5s' % ('pythonstudy' , )) # 점을 찍어서 5자리 절삭

# %d
print('%d %d' % (1,2))
print('%4d' % (42))
print('%-4d' % (42))

# %f 기본으로 6자리까지만 출력되고 뒤에는 반올림
print('%1.2f' % (3.1415926,)) # %1.2 는 정수부.소수부 로 정수부와 소수부 출력 자리수르 지정 가능

# 변수 ?
'''
내장된 변수 타입들이 있음
python Built-in types
Numeric
sequence
Text sequence
Set
Mapping
Bool
파이썬에는 배열이 존재하지 않고 추후 배울 numpy에서 ndarray 타입이 파이썬의 배열이다
'''
'''
변수를 선언하는 다양한 방법
(변수) camel case : numberOfCollegeGraduates (변수의 처음은 소문자고 연결된 단어들의 첫글자만 대문자)
(클래스) pascal case : NumberOfCollegeGraduates (변수의 처음부터 첫글자는 다 대문자)
(변수) snake case : number_of_collge_graduates (변수를 언더바로 연결시킴 , 다 소문자)

주의) 
변수는 숫자로 시작할 수 없고, 특수문자 _, $ 허용된다.
대소문자를 구별한다.
예약어는 변수로 사용할 수 없다.
'''

print('변수 - ')
age = 10
Age = 20
print(age, Age, type(age), type(Age)) # 위에서 언급한 Numeric을 의미한다. (숫자)

# keyword.py
# keyword.함수() , keyword.변수
import keyword
kw = keyword.kwlist
print('type - ', type(kw)) # list형 , sequence 타입
print('data -' , kw)

# 변수 바인딩( = 연산자를 이용해서 할당)
year = '2022'
month = '1'
day = '25'
print(year, month, day, type(year), type(month), type(day))
print('오늘은 {}년 {}월 {}일 입니다.'.format(year, month, day))

intValue   = 123
floatValue = 3.14
boolValue  = True # 논리값
strValue   = 'nsjung'
print('type -', type(intValue), type(floatValue), type(boolValue), type(strValue))

# 형변환
print(str(intValue) + strValue)
# 파이썬은 모든 변수를 boolean 으로 만들 수 있다.
name ='nsjung'
print(bool(name), type(bool(name))) #값이 들어가면 1 true, 안들어가면 0 false
print(int(bool(name)), type(int(bool(name))))

# list type 스칼라값 저장
list = ['이지희', '강진성', '장성원']
print('type - ', type(list))
print('data - ', list)

#dict(key, value) type  / 다중값을 담는 변수 타입 dictionary

dict = {
    "name" : "machine Learning",
    "version" : 2.0
}
print('type - ', type(dict))
print('data - ', dict)

# tuple  / ,(컴마) 포맷팅을 할 때 ,컴마를 안찍으면 int형으로 나옴
tuple = (3,)
print('type - ', type(tuple))
print('data - ', tuple)

# set type
set = {3, 5, 7}
print('type - ', type(set))
print('data - ', set)

# str type(중요)
str01 = "I am Python"
str02 = 'I am Python'
str03 = '''
this is a
multi line comment'''
str04 = """this is a
        multi line comment"""
print(type(str01), type(str02), type(str03), type(str04))
print(str03)

# 딕셔너리랑 세트의 타입 차이가 머지