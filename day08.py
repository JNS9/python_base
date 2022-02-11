'''
학습목표
 - 예외처리
 - 매직함수, 데코레이터, 제너레이터, 일급함수
 - 파일입출력
'''

#print('programming start - ')
#print('*' * 50)
#age = int(input('나이를 숫자로 입력해주세요 : '))
#print('your age is' , age , 'years old')
#print('*' * 50)
#print('programming end - ')


'''
Exception - xxxxerror 모든에러 처리
예외처리 구문
try      :
    예외가 발생할 가능성이 있는 코드를 정의하는 곳
    A
    B
except A :
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
except B :
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
else     :
    예외가 발생되지 않을 때 실행되는 곳
finally  :
    예외발생 여부와 상관없이 실행되는 곳
'''



'''
# function define - worker
def smpInput() :
    try :
        age = int(input('나이를 숫자로 입력해주세요 : '))
    except ValueError as e :
        #print(str(e))
        smpInput()
    else :
        print('your age is' , age , 'years old')
    finally :
        print('** 예외발생여부와 상관없이 무조건 수행 **')

# caller
smpInput()
print('programming end - ')
'''



'''
매개변수로 넘겨받은 각 첨자번지의 값에 제곱한 결과를
출력하려고 한다.
예외 발생을 확인하고 예외처리 구문을 추가하여 
정상적인 흐름의 함수 호출이 되도록 만들어 본다면?
'''


'''
def exceptionFunc(lst) :

        for e in lst :
            try:
                print('raw - ' , e)
                sqrt = e ** 2
                print('squared - ' , sqrt)
            except TypeError as e :
                pass

# caller
usrlst = [10, 20, 25, 'num', 40, 50]
exceptionFunc(usrlst)
'''


# 호출을 예외처리하고 싶을 때
# 사용자 정의 예외클래스를 만들 수 있다.
class UserNegativeDivisionError(Exception) :
    def __init__(self, msg):
        self.msg = msg

def positiveDivide(x,y) :
    if(y < 0) :
        raise UserNegativeDivisionError('음수로 나눌 수 없습니다.')
    else :
        return x/y

try :
    result = positiveDivide(10, -2)
    print('call positive func - ' , result)
except UserNegativeDivisionError as e :
    print(e.msg)
except ZeroDivisionError as e :
    print(e.args[0])
print('programming end - ')



# magic function
# __xxxx__()

class MagicClass(object) :
    def __init__(self):
        print('객체 생성시 호출')
    def __del__(self):
        print('객체 삭제시 호출')
    def __str__(self):
        return '이제는 주소값이 아니라 문자열이 출력'

obj = MagicClass() # 주소값이 호출되지 않으면 매직함수를 오버라이딩 하지 않았다고 생각하면 됩니다.
#print('dir - ' , dir(obj))
print(obj.__str__())


'''
 일급함수, first class
 - 변수에 함수를 저장할 수 있다.
 - 함수를 다른 함수의 인자로 전달할 수 있다.
useradd는 함수를 변수로 쓰는거고 , useradd()는 함수를 호출하는 것
'''

def userAdd(x,y) :
    return x + y

print('add - ', userAdd(10, 20))
print('function address - ' , userAdd)
f = userAdd # 함수를 변수에 저장
print('f - add - ' , f(10,20))

# 함수를 다른 함수의 인자로 전달
def userOperation(func, arg) :
    return func(arg[0] , arg[1])

def userMinus(x , y) :
    return x - y

data = (1,2)
result = userOperation(userAdd, data)
print('result add - ' , result)
result = userOperation(userMinus, data)
print('result minus - ' , result)

# 함수의 리턴값으로 다른 함수를 사용할 수 있다.
# closure (함수 내부에 자료구조를 생성하여 값을 저장해 놓는 개념)
def outer(x) :

    def inner(y) :
        return x + y

    return inner

# caller
result = outer(5)               # outer 함수에 5 넣고
print('result - ' , result(10)) # inner에 10을 넣는다고 보면됨


# generator (반복문)
# - 장점 : 빠른 수행 속도, 적은 메모리 사용으로 인한 성능 향상, 쉽게 for 루프 구문

def loopFunc(lst) :
    result = []
    for i in lst :
        result.append(i ** 2)
    return result

# caller
data = [1,2,3,4,5]
result = loopFunc(data)
print('result - ' , result)

def generatorFunc(lst) :
    for tmp in lst :
        yield tmp ** 2

# caller
result = generatorFunc(data)
print('generator type - ' , type(result))
#print('next - ' , next(result))
#print('next - ' , next(result))

for e in result :
    print(e)

lst = [tmp ** 2 for tmp in data]
print('list comprehension - ' , lst)
generator = (tmp ** 2 for tmp in data)
print('type - ' , generator)

for g in generator :
    print(g)
print('end for ~ ')
print('generator - ' , list(generator))

#for g in generator :
#    print(g)


# 파일입출력
# 순수 파이썬 기반 입출력, pandas 기반 입출력
'''
텍스트 파일
- open(file=xxxxx, mode='r|w|a') read, write, append , endcoding == xxxxx)
- with open() as file :

'''

def readTxt(path, mode) :
    file = None
    try :
        file = open(path, mode, encoding='utf-8')
        print('file type - ' , type(file) , file)
    except Exception as e :
        print(str(e))
    else :
        print('read -\n' , file.read())
    finally :
        if file != None :
            file.close()

# caller
#readTxt('./data/greeting.txt' , 'r')

# 출력
def writeTxt(path, mode) :
    file = open(path, mode, encoding = 'utf-8')
    file.write('\nHello~, Seop ^^')
    file.close()

# caller
#writeTxt('./data/test.txt', 'a' )

# define - worker
def with_open_file(path, mode, e) :
    with open(path, mode, encoding=e) as file :
#        print('read type - ', type(file.read()))
#        print('readlines type - ' , type(file.readlines()))
#        print('readline type - ' , type(file.readline()))

#        for line in file :
#            print(line.strip('\n'))

# readline() 구현
#        line = file.readline()
#        while line != '' :
#            line = file.readline()
#            print(line.strip('\n'))

# readlines() 구현
        lst = file.readlines()
        for s in lst :
            print(s.strip('\n'))

# caller
with_open_file('./data/greeting.txt' , 'r' , 'utf-8')


