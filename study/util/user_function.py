'''
- 인자 없고, 리턴 없는 함수
- worker
def a() :
    statement
-caller
a()


- 인자 있고, 리턴 없는 함수
def b(x, y, z)
    statement
- caller
b(10, Treu, 'jslim')


- 인자 없고, 리턴 있는 함수
def c() :
    statement
    return value (모든 변수의 타입 허용)
-caller
returnvalue = c()


- 인자 있고, 리턴 있는 함수
def d(x)
    statment
    return value
- caller
returnValue = d(10)

'''

# 인자와 리턴 둘 다 있음
def my_sum(x, y, z) :
    sum = x + y + z
    return sum

# 인자는 없고 리턴도 없음
def print_coins() :
    for idx in range(100) :
        print('coin~~ T.T')

# 인자가 없고 리턴만 있음
def noArgsReturnValue() :
    return (10, 20)

# 인자가 있고 리턴이 없음
def argsNoReturn(x) :
    print('인자는 있고 리턴이 읍다')

def default_param(x, y, z =True) :
    data = 0
    if z :
        data = x * y
    else :
        data = x + y
    return data

# 함수 선언시 가변인수를 정의할 수 있다.
def argsTuple(*args) :
    for idx in range(len(args)) :
        print(args[idx], end=('\t'))
    print()

def kwargsDict(**args) : # **가 2개면 dict , *-> 1개면 tuple
    for key, value in args.items() :
        print('{} , {}' .format(key , value))
    print("*" * 50)

def personInfo(*info, **args) :
    weight, height = info
    print('weight - ', weight)
    print('height - ', height)
    for key, value in args.items() :
        print('{} , {}' .format(key , value))

# mutable(원본에 영향을 미친다) - immutable(원본에 영향을 미치지 않는다)
# mutable   - list, dict
# immutable - number, str, tuple


def call_by_value(tmp_number) :
    tmp_number = tmp_number * 100
    print('inner function - ' , tmp_number)

def call_by_reference(tmp_number, tmp_list):
    tmp_number = tmp_number + 100
    tmp_list.append(tmp_number)

def userStatistic(func, *data) :
    from statistics import mean
    if func == 'sum' :
        print(sum(data))
    if func == 'mean' :
        print(mean(data))

def makeUrl(lst : list) :
    result = []
    for url in lst :
        result.append('www.'+url+'com')
    return result

