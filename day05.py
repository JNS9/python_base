
# 반복구문
import random

word = 'Beautiful'
for w in word :
    print(w, end='\t')
print()

for idx, w in enumerate(word) :
    print(idx, w, end='\t')
print()

myInfo = {
    'name'  : 'seop' ,
    'Age'   : '50' ,
    'City'  : 'Seoul'
}

for key in myInfo :
    print(key, myInfo[key] , end='\t')
print()

for key , value in myInfo.items() :
    print(key, value , end='\t')
print()

numbers = [14, 3, 4, 7, 6, 23, 24, 59, 23, 19, 8]
# break, continue
if 24 in numbers :
    print('True')
else :
    print('False')

for idx, num in enumerate(numbers) :
    if num == 24 :
        # continue          # 조건에 부합하면 건너뛰고 반복하는 명령어
        print(idx, 'Found!!')
        # break             # 이 위치에 continue를 쓰면 아무 의미가없음, 이미 출력한 다음이기 때문
    else :
        print(idx, 'Not Found!!')

#for ~ in ~ else :
for num in numbers :
    if num == 23 :
        print('Found!!')
        break
else :
    print('Not Found!!')

# 이중 루프구문
# 2 * 1 ~ 9
# 3 * 1 ~ 9

for row in range(2,10) :
    if row == 5:
        continue
    for col in range(1,10) :
        print('{} * {} = {}'.format(row, col, (row*col)) , end=('\t'))
    print()

# 문자열 처리를 위한 for ~
str = \
'''
저는 파이썬을 강의 중인 강사 임정섭입니다.
주소는 서울시 입니다.
나이는 숫자에 불과합니다.
'''
# sentences = str.split('\n')
# print('type - ', type(sentences), sentences)
sentences = []
words = []
for s in str.split('\n') :
    sentences.append(s)
    for w in s.split() :
        words.append(w)
print('sentences - ' , sentences , len(sentences))
print('words - ' , words, len(words))

apt = [
    ['101호' , '102호'] ,
    ['201호' , '202호'] ,
    ['301호' , '302호']
]
for row in apt :
    for col in row :
        print(col)
    print('*' * 50)

#분류 정확도 확인
y_test = [1, 0, 2, 1, 0]   # 정답
y_pred = [1, 0, 2, 0, 0]   # 예측값

acc = 0
for idx in range(len(y_pred)) :
    fit = y_test[idx] == y_pred[idx]
    acc += int(fit) * 20
print('acc - ' , acc , '%', sep='')

# 난수(random)

nan01 = random.random()
print('0 ~ 1 : ' , nan01)

nan02 = random.randint(1, 10)
print('범위 사이의 정수 : ' , nan02)

dataset = list(range(1, 1001))
print('dataset - ' , dataset)

train_data = random.choices(dataset , k = 10)
print(train_data)


'''
while 구문 형식
 - 초기식
 - while(조건식)
        <loop body>
        증감식
while로할수있는건 for loop로도 할 줄 알아야되고 그 반대도 할 줄 알아야댐~~~
 '''

print()
n = 5
lst = ['apple' , 'banana' , 'mango']
while lst :
    print(lst.pop()) # get을 써서 apple부터 출력 가능

'''
1~ 100 까지 5의 배수의 합 출력하기
add) 3의 배수이면서 5의 배수가 아닌 합을 출력하기
while ~ 구문 활용
'''

# abc = []
# for i in range(1,101) :
#     if i % 5 == 0 :
#         i += 5
#
# while range(1,101) :
#     if i % 5 == 0 :
#         i += 5
#
# print(i)

cnt = fiveMul = total = 0
while cnt <= 100 :
    if cnt % 5 == 0 :
        fiveMul += cnt
    if cnt % 3 == 0 and cnt % 5 != 0 :
        total += cnt
    cnt+= 1
print('5의 배수의 합' , fiveMul)
print('3의 배수이면서 5의 배수가 아닌 합' ,total)


# while ~ else
lst = ['apple' , 'banana' , 'mango' , 'pear']
guess = 'orange'
idx = 0
while idx < len(lst) :
    if guess == lst[idx] :
        print('Found!!')
        break
    idx += 1
else :
    print('Not Found')

#from study.util import syntax
#syntax.greeting()
from study.util.syntax import greeting , sayEcho
greeting()
sayEcho('에코')

from study.util.user_function import *
result_sum = my_sum(10,20,30)
print('return value - ' , result_sum)

result_coins = print_coins()
print('return value - ' , result_coins)

print_coins()

# result_tuple = noArgsReturnValue()
# print('return tuple - ' , result_tuple)

a, b = noArgsReturnValue()
print('return tuple - ' , a, b)

argsNoReturn('jslim')

result = default_param(10, 20)
print('default param - ' , result)
result = default_param(10, 20, False)
print('default param - ' , result)

#가변인수를 가지는 함수 호출
# caller
argsTuple('kim')
argsTuple('kim' , 'lim')
argsTuple('kim' , 'lim' , 'lee')

# dict type - caller
kwargsDict(name = 'jslim')
kwargsDict(name = 'jslim' , name1 = 'parksu')
kwargsDict(name = 'jslim' , name1 = 'parksu' , name2 = 'jung')

personInfo(78, 178,
           name = 'jslim',
           address = 'seoul',
           gender = 'm')

dataX = 5
print('함수 호출 전 - ' , dataX) # 카피되어 넘어오기 때문에 원본에 영향 안미침
call_by_value(dataX)
print('함수 호출 후 - ' , dataX)

dataX = 5
dataL = [10, 20]
print('함수 호출 전 - ' , dataL)
call_by_reference(dataX, dataL)
print('함수 호출 후 - ' , dataL)

# 함수가 함수를 인자로 받아서 해당 함수를 수행하는 구문
print()
userStatistic('sum', 1,2,3,4,5,6,7,8)
userStatistic('mean', 1,2,3,4,5,6,7,8)

# 변수의 scope
# local variable VS global variable

global_tmp = 100

def variableScope(x) :
    global global_tmp
    global_tmp += x
    return global_tmp

print(variableScope(100))
print(global_tmp)

def my_sqrt(x) :
    return x ** 2

lst = list(map(my_sqrt , range(1, 10))) # map : 반복 호출
print('lst - ' , lst)

str = list(zip('hello' , 'seops' , 'world')) # zip 묶어주는거
print('str - ' , str )

# www.naver.com 이런식으로 출력
urls = ['naver' , 'google' , 'samsung']
url_list = makeUrl(urls)
print(url_list)

def makeUrl(x) :
    pass